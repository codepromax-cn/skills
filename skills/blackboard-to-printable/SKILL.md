---
name: blackboard-to-printable
description: "Turn classroom blackboard, greenboard, or whiteboard photos into clean, black-on-white printable PNG and A4 PDF files. Preserves original handwriting, diagrams, and layout without OCR errors or hallucinations. Applies Gaussian flat-field illumination correction, adaptive Otsu thresholding, speckle noise reduction, and projection-based deskew."
license: MIT
---

# Blackboard to Printable

Convert photos of classroom blackboards, greenboards, or whiteboards into high-contrast, black-strokes-on-white-background printable documents. The process preserves authentic handwriting, complex mathematical formulas, and hand-drawn diagrams exactly as written—without OCR distortion, artificial transcription, or hallucinated content.

## When to use

- **Chalkboard & whiteboard notes**: Converting lecture board photos, classroom discussions, or conference whiteboards into clean handouts.
- **Ink-saving printing**: Removing dark blackboard backgrounds, uneven room lighting, shadows, and dirty eraser smudges so notes print clearly without draining ink.
- **Diagrams & complex notation**: Preserving custom math symbols, chemical structures, circuit diagrams, geometric sketches, and spatial layouts that OCR fails to parse.
- **Batch study material prep**: Converting lecture photo sets into structured, standardized 300 DPI A4 PDFs for digital reading or printing.

## When not to use

- **Editable text required**: When the user explicitly requests editable text (LaTeX, Word `.docx`, or Markdown transcription), use OCR or transcription tools instead.
- **Standard printed documents**: For flatbed-scanned typed paper or office forms, use standard document binarization tools.

## Core processing pipeline

1. **Orientation & Dimension Normalization**: Reads image with EXIF orientation correction via `ImageOps.exif_transpose`, converts to grayscale, and scales the longest side to 2500 px to maintain high fidelity while ensuring fast, memory-efficient processing.
2. **Flat-Field Illumination Correction**: Applies a large-radius Gaussian blur ($\text{radius} = \max(w, h) / 15$) to estimate uneven lighting, corner vignetting, glare spots, and background shading.
3. **Contrast Stroke Extraction**:
   - **Blackboard mode** (chalk brighter than board): $\text{strokes} = \max(G - B, 0)$
   - **Whiteboard mode** (marker darker than board): $\text{strokes} = \max(B - G, 0)$
   - **Auto detection**: Evaluates background luminance to select mode automatically.
   - Normalizes contrast against the 99.5th percentile to guard against extreme specular highlights.
4. **Adaptive Otsu Thresholding**: Calculates global separation threshold using Otsu's method and applies a configurable offset (default `+15`) to suppress faint ghosting and chalk haze.
5. **Morphological Noise Cleaning**: Applies morphological opening ($3\times 3$ erode then dilate) to strip isolated dust particles, chalk powder specks, and minor reflections while retaining fine stroke connections.
6. **Projection Skew Correction**: Evaluates row-sum projection profile variance across small rotation angles ($[-5.0^\circ, +5.0^\circ]$ at $0.2^\circ$ steps) to detect horizontal text baseline alignment and rotate the image straight.
7. **Print-Ready A4 PDF & PNG**: Inverts the binary mask to generate crisp black strokes on a clean white page, saving both a PNG image and a 300 DPI A4 PDF with balanced margins (auto-selecting landscape or portrait based on aspect ratio).

## Quick start

### Dependencies

Requires Python 3.8+ with Pillow and NumPy:

```sh
pip install -r requirements.txt
# or: pip install "Pillow>=10.0.0" "numpy>=1.24.0"
```

### Command line

Run the bundled conversion script [blackboard_to_printable.py](scripts/blackboard_to_printable.py):

```sh
# Basic usage (auto-detects board type, generates PNG and A4 PDF)
python3 scripts/blackboard_to_printable.py lecture_photo.jpg --out-dir ./output

# Custom output base name and threshold tuning for faint chalk
python3 scripts/blackboard_to_printable.py photo.jpg --name math_lecture_01 --thresh-offset 5

# Force whiteboard mode and portrait A4 layout
python3 scripts/blackboard_to_printable.py whiteboard.png --mode whiteboard --orientation portrait
```

### Python API

```python
from scripts.blackboard_to_printable import convert

result = convert(
    input_path="blackboard.jpg",
    out_png="output/lecture-printable.png",
    out_pdf="output/lecture-printable.pdf",
    thresh_offset=15,
    deskew=True,
    mode="auto",         # "auto", "blackboard", or "whiteboard"
    orientation="auto",  # "auto", "landscape", or "portrait"
)

print(f"Processed as {result['mode']}, deskewed by {result['angle']}°")
```

## CLI options & parameters

| Option | Default | Description |
| :--- | :--- | :--- |
| `input` | *(required)* | Path to source photo (JPEG, PNG, WEBP, HEIC, TIFF, etc.). |
| `--out-dir` | `.` | Target directory for generated output files. |
| `--name` | `None` | Custom base filename (defaults to input file stem). |
| `--mode` | `auto` | Board classification: `auto` (auto-detect by luminance), `blackboard`, or `whiteboard`. |
| `--thresh-offset` | `15` | Otsu threshold offset. Lower (e.g. `5`) for faint strokes; raise (e.g. `25`–`35`) to suppress heavy haze/reflections. |
| `--orientation` | `auto` | PDF page orientation: `auto` (matches image aspect ratio), `landscape`, or `portrait`. |
| `--max-side` | `2500` | Maximum pixel dimension for downscaling before processing. |
| `--no-deskew` | `False` | Disable automatic projection deskewing. |
| `--no-pdf` | `False` | Omit A4 PDF generation and output only the PNG. |

## Tuning guide

- **Faint or thin chalk strokes**: Set `--thresh-offset 5` or `--thresh-offset 8` to capture low-contrast handwriting.
- **Heavy reflections or chalk powder haze**: Increase `--thresh-offset 25` to `--thresh-offset 35` to clear stubborn background haze.
- **Mixed or unusual lighting**: If auto-detection chooses the wrong board type due to extreme backlighting, explicitly specify `--mode blackboard` or `--mode whiteboard`.
- **Pre-straightened photos**: If the image was already captured with a document scanner app or tripod, pass `--no-deskew` to skip rotational re-sampling.

## Bundled resources

- [scripts/blackboard_to_printable.py](scripts/blackboard_to_printable.py): Standalone CLI tool and reusable conversion library.
- [requirements.txt](requirements.txt): Minimal Python package specifications (`Pillow`, `numpy`).
