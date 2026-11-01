# Handwritten Worksheet to Word

[English](README.md) | [简体中文](README_zh.md)

> Sibling Chinese package: [handwritten-worksheet-to-word-zh](../handwritten-worksheet-to-word-zh/README.md)

An agent skill that turns photos of Chinese practice worksheets (typically completed with red handwriting) into clean, editable, printable Word (`.docx`) documents.

## Install

Install this skill into your AI coding assistant:

```sh
# Auto-detects your active agent (Cursor, Antigravity, Claude Code, etc.)
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word

# Or install user-wide globally
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word -g
```

## What This Skill Does

- **Colour Decides What Stays**: Strips red handwritten answers while preserving black printed text, question stems, and printed examples.
- **Strict Fidelity**: Preserves original question numbering, wording, collocations, punctuation, and brackets without OCR hallucination or rephrasing.
- **Standardized Blanks**:
  - 1-character handwritten answer $\rightarrow$ `（　）` (one full-width space)
  - 2-character handwritten phrase $\rightarrow$ `（　　）` (two full-width spaces)
  - Punctuation fill-in box $\rightarrow$ empty square box `□`
  - Underline sentence lines $\rightarrow$ underscore writing lines without handwritten punctuation
- **Borderless Table Layout**: Multi-column questions use borderless fixed-width tables rather than unstable spaces to ensure proper cross-platform alignment.
- **Verification Checklist**: Converts generated Word files to PDF to perform page-by-page inspection for overflow, missing items, or leaked answers before delivery.

## How to Use With Your Agent

Once installed, simply upload the worksheet photos to your AI assistant:

> *"Please convert this worksheet into a clean, printable Word document. Strip out the handwritten red answers and restore the blanks."*

Your assistant will automatically trigger this skill, construct the document with `python-docx`, and verify the final output.

## Agent Instructions

For the complete agent prompt loaded by AI assistants, see [`SKILL.md`](SKILL.md).

## License

[MIT License](LICENSE)
