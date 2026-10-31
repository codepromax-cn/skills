#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Blackboard and whiteboard photo to black-on-white printable document converter.

Turns photos of classroom blackboards, greenboards, or whiteboards into clean,
black-text-on-white-background printable PNG and A4 PDF files. Preserves original
handwriting, diagrams, formulas, and spatial layout without OCR, transcription,
or artificial retyping.

Dependencies:
    Pillow >= 10.0.0
    numpy >= 1.24.0

Usage:
    python3 blackboard_to_printable.py input_photo.jpg --out-dir output_dir
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Any, Tuple

import numpy as np
from PIL import Image, ImageFilter, ImageOps


def load_gray(path: str, max_side: int = 2500) -> Image.Image:
    """Load an image, apply EXIF orientation, convert to grayscale, and cap the longest side."""
    img = Image.open(path)
    img = ImageOps.exif_transpose(img).convert("L")
    if max(img.size) > max_side:
        scale = max_side / max(img.size)
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    return img


def estimate_background(gray: Image.Image) -> Image.Image:
    """Estimate board background illumination and gradient using large-radius Gaussian blur.

    This serves as flat-field correction, capturing non-uniform lighting, shadows,
    and eraser smudges into the background model so they do not become foreground strokes.
    """
    radius = max(gray.size) / 15.0
    return gray.filter(ImageFilter.GaussianBlur(radius))


def stroke_strength(
    gray: Image.Image,
    bg: Image.Image,
    mode: str = "auto",
) -> Tuple[np.ndarray, str]:
    """Calculate stroke contrast map against the estimated background.

    In blackboard mode, chalk is brighter than the board (g - b > 0).
    In whiteboard mode, marker ink is darker than the board (b - g > 0).
    In auto mode, background brightness determines board type.

    Returns:
        Tuple of (stroke_strength_array, detected_mode)
    """
    g = np.asarray(gray, dtype=np.float32)
    b = np.asarray(bg, dtype=np.float32)

    if mode == "auto":
        is_whiteboard = float(np.median(b)) > 127.0
        resolved_mode = "whiteboard" if is_whiteboard else "blackboard"
    elif mode == "whiteboard":
        resolved_mode = "whiteboard"
    elif mode == "blackboard":
        resolved_mode = "blackboard"
    else:
        raise ValueError(f"Unknown mode '{mode}'. Choose 'auto', 'blackboard', or 'whiteboard'.")

    if resolved_mode == "whiteboard":
        s = np.clip(b - g, 0.0, None)
    else:
        s = np.clip(g - b, 0.0, None)

    hi = float(np.percentile(s, 99.5))
    if hi > 0.0:
        s = s / hi * 255.0
    return np.clip(s, 0.0, 255.0).astype(np.uint8), resolved_mode


def otsu(x: np.ndarray) -> int:
    """Compute Otsu automatic global threshold via pure numpy implementation."""
    hist = np.bincount(x.ravel(), minlength=256).astype(np.float64)
    total = x.size
    sum_total = np.dot(np.arange(256), hist)
    sum_b = 0.0
    w_b = 0.0
    best_t, best_v = 0, -1.0

    for t in range(256):
        w_b += hist[t]
        if w_b == 0 or w_b == total:
            continue
        sum_b += t * hist[t]
        w_f = total - w_b
        m_b = sum_b / w_b
        m_f = (sum_total - sum_b) / w_f
        v = w_b * w_f * ((m_b - m_f) ** 2)
        if v > best_v:
            best_v, best_t = v, t

    return best_t


def estimate_skew(mask_img: Image.Image, max_angle: float = 5.0, step: float = 0.2) -> float:
    """Estimate image tilt angle using projection profile variance.

    Horizontal text lines maximize variance of row sums. Restricts search to
    small angles [-max_angle, max_angle] to avoid false 90-degree rotations.
    """
    small = mask_img.copy()
    small.thumbnail((600, 600))
    best_a, best_s = 0.0, -1.0
    a = -max_angle
    while a <= max_angle + 1e-9:
        r = small.rotate(a, resample=Image.BILINEAR, fillcolor=0)
        score = float(np.asarray(r, dtype=np.float32).sum(axis=1).var())
        if score > best_s:
            best_s, best_a = score, a
        a += step
    return round(best_a, 2) if abs(best_a) >= 0.3 else 0.0


def convert(
    input_path: str,
    out_png: str,
    out_pdf: str | None = None,
    thresh_offset: int = 15,
    deskew: bool = True,
    mode: str = "auto",
    orientation: str = "auto",
    max_side: int = 2500,
) -> dict[str, Any]:
    """Convert blackboard/whiteboard photo to high-contrast printable files.

    Args:
        input_path: Path to source image file.
        out_png: Destination path for output PNG image.
        out_pdf: Optional destination path for 300 DPI A4 PDF.
        thresh_offset: Threshold adjustment added to Otsu value (+ lowers sensitivity, - increases).
        deskew: Whether to estimate and correct small skew angles.
        mode: Board type ('auto', 'blackboard', or 'whiteboard').
        orientation: PDF page orientation ('auto', 'landscape', or 'portrait').
        max_side: Maximum dimension for processing downscale (preserves aspect ratio).

    Returns:
        dict containing execution metrics and output paths.
    """
    gray = load_gray(input_path, max_side=max_side)
    bg = estimate_background(gray)
    s, detected_mode = stroke_strength(gray, bg, mode=mode)
    t = otsu(s) + thresh_offset
    mask = Image.fromarray((s > t).astype(np.uint8) * 255)

    # Morphological opening (erode then dilate) to eliminate small isolated noise specks
    mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))

    angle = estimate_skew(mask) if deskew else 0.0
    if angle != 0.0:
        mask = mask.rotate(angle, resample=Image.BILINEAR, fillcolor=0, expand=True).point(
            lambda v: 255 if v > 127 else 0
        )

    # Invert binary mask: strokes become black (0), background becomes white (255)
    page = ImageOps.invert(mask)
    page.save(out_png)

    if out_pdf:
        # Resolve A4 dimensions @ 300 DPI (standard: 3508 x 2480 px landscape, 2480 x 3508 px portrait)
        if orientation == "portrait" or (orientation == "auto" and page.height > page.width):
            a4_size = (2480, 3508)
        else:
            a4_size = (3508, 2480)

        a4 = Image.new("L", a4_size, 255)
        m = round(min(a4.size) * 0.04)
        fit = ImageOps.contain(page, (a4.width - 2 * m, a4.height - 2 * m), Image.LANCZOS)
        a4.paste(fit, ((a4.width - fit.width) // 2, (a4.height - fit.height) // 2))
        a4.save(out_pdf, "PDF", resolution=300.0)

    return {
        "angle": angle,
        "threshold": t,
        "mode": detected_mode,
        "width": page.width,
        "height": page.height,
        "out_png": out_png,
        "out_pdf": out_pdf,
    }


def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    ap = argparse.ArgumentParser(
        description="Turn a blackboard or whiteboard photo into a black-on-white printable file"
    )
    ap.add_argument("input", help="Path to input photo (JPG, PNG, HEIC, WEBP, etc.)")
    ap.add_argument("--out-dir", default=".", help="Output directory (default: current directory)")
    ap.add_argument("--name", default=None, help="Base name for output files (default: input file name stem)")
    ap.add_argument(
        "--mode",
        choices=["auto", "blackboard", "whiteboard"],
        default="auto",
        help="Board type: 'auto' (detects background tone), 'blackboard' (chalk), or 'whiteboard' (marker)",
    )
    ap.add_argument(
        "--thresh-offset",
        type=int,
        default=15,
        help="Threshold offset added to Otsu value: lower (e.g. 5) for faint strokes, raise (e.g. 30) for heavy noise",
    )
    ap.add_argument(
        "--orientation",
        choices=["auto", "landscape", "portrait"],
        default="auto",
        help="PDF page orientation: 'auto' matches image aspect ratio, or force 'landscape'/'portrait'",
    )
    ap.add_argument(
        "--max-side",
        type=int,
        default=2500,
        help="Longest dimension cap in pixels for processing (default: 2500)",
    )
    ap.add_argument("--no-deskew", action="store_true", help="Skip automatic tilt straightening")
    ap.add_argument("--no-pdf", action="store_true", help="Output only PNG image, omit PDF")
    return ap


def main(argv: list[str] | None = None) -> int:
    """Main CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not os.path.isfile(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        return 1

    base = args.name or os.path.splitext(os.path.basename(args.input))[0]
    os.makedirs(args.out_dir, exist_ok=True)
    out_png = os.path.join(args.out_dir, f"{base}-printable.png")
    out_pdf = None if args.no_pdf else os.path.join(args.out_dir, f"{base}-printable.pdf")

    try:
        result = convert(
            input_path=args.input,
            out_png=out_png,
            out_pdf=out_pdf,
            thresh_offset=args.thresh_offset,
            deskew=not args.no_deskew,
            mode=args.mode,
            orientation=args.orientation,
            max_side=args.max_side,
        )
    except Exception as exc:
        print(f"ERROR: Conversion failed: {exc}", file=sys.stderr)
        return 1

    print(
        f"Mode: {result['mode']} | Threshold: {result['threshold']} | Deskew angle: {result['angle']:.1f}°"
    )
    print(f"PNG: {result['out_png']} ({result['width']}x{result['height']})")
    if result["out_pdf"]:
        print(f"PDF: {result['out_pdf']} (A4 @ 300 DPI)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
