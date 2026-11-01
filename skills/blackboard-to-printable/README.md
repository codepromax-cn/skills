# Blackboard to Printable

Convert classroom blackboard, greenboard, or whiteboard photos into clean, black-on-white printable PNG and 300 DPI A4 PDF files. Preserves original handwriting, mathematical formulas, and sketches without OCR hallucinations or distorted layouts.

## Install

Install this skill into your AI coding assistant:

```sh
# Auto-detects your active agent (Cursor, Antigravity, Claude Code, etc.)
npx skills add codepromax-cn/skills --skill blackboard-to-printable

# Or install user-wide globally
npx skills add codepromax-cn/skills --skill blackboard-to-printable -g
```

## Standalone CLI Usage (Without an Agent)

You can also run the bundled Python converter script directly from your terminal.

### 1. Requirements

Requires Python 3.8+ with Pillow and NumPy:

```sh
pip install -r requirements.txt
# or: pip install "Pillow>=10.0.0" "numpy>=1.24.0"
```

### 2. Run the Converter

```sh
# Basic usage (auto-detects board type, generates PNG and 300 DPI A4 PDF)
python3 scripts/blackboard_to_printable.py lecture.jpg --out-dir ./output

# Custom output base name and threshold tuning for faint chalk
python3 scripts/blackboard_to_printable.py photo.jpg --name math_lecture_01 --thresh-offset 5

# Force whiteboard mode and portrait A4 layout
python3 scripts/blackboard_to_printable.py whiteboard.png --mode whiteboard --orientation portrait
```

### 3. CLI Options Reference

| Option | Default | Description |
| :--- | :--- | :--- |
| `input` | *(required)* | Path to source photo (JPG, PNG, HEIC, WEBP, etc.). |
| `--out-dir` | `.` | Target output directory. |
| `--name` | `None` | Base filename stem for outputs (defaults to input filename stem). |
| `--mode` | `auto` | Board classification: `auto` (auto-detects background tone), `blackboard`, or `whiteboard`. |
| `--thresh-offset`| `15` | Threshold adjustment (+ lowers sensitivity, - increases sensitivity for faint chalk). |
| `--orientation` | `auto` | PDF page orientation: `auto` (matches image aspect ratio), `landscape`, or `portrait`. |
| `--no-deskew` | `False` | Skip automatic horizontal line tilt straightening. |
| `--no-pdf` | `False` | Output only the PNG image, omitting PDF generation. |

## Core Processing Pipeline

1. **Flat-Field Illumination Correction**: Uses large-radius Gaussian blur ($\text{radius} = \max(w, h) / 15$) to isolate uneven lighting, glare spots, and shadows.
2. **Stroke Contrast Isolation**: Evaluates local luminance differences ($G - B$ for chalk on dark board, $B - G$ for marker on light whiteboard).
3. **Adaptive Otsu Thresholding**: Pure NumPy Otsu global thresholding with tuneable sensitivity offset.
4. **Morphological Opening**: $3\times 3$ erode-dilate filter eliminates chalk powder dust and specular noise specks.
5. **Projection Deskewing**: Row projection variance search rotates tilted writing horizontal.
6. **Print-Ready A4 Export**: Centered 300 DPI layout with balanced margins.

## Agent Instructions

For the complete agent prompt loaded by AI coding assistants, see [`SKILL.md`](SKILL.md).

## License

[MIT License](LICENSE)
