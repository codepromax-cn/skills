# Handwritten Worksheet to Word (Chinese Prompts Edition)

[English](README_en.md) | [简体中文](README.md)

> Sibling English prompt package: [handwritten-worksheet-to-word](../handwritten-worksheet-to-word/README.md)

An AI agent skill featuring native Chinese instructions for restoring photos of Chinese practice worksheets (typically completed in red handwriting) into clean, editable, printable Word (`.docx`) documents.

## Install

Install this skill into your AI coding assistant:

```sh
# Auto-detects your active agent (Cursor, Antigravity, Claude Code, etc.)
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word-zh

# Or install user-wide globally
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word-zh -g
```

## Core Processing Rules

1. **Colour Decides What Stays**: Retains black printed characters; strips red handwritten answers. Black printed examples stay; red handwritten examples go.
2. **Remove Handwriting Only**: Never alters question stems, item numbering, word collocations, punctuation, or bracket positions. Never invents missing items and never copies app watermarks.
3. **Standardized Blanks**:
   - 1-character handwritten answer $\rightarrow$ `（　）` (one full-width space)
   - 2-character handwritten phrase $\rightarrow$ `（　　）` (two full-width spaces)
   - Punctuation fill-in box $\rightarrow$ empty square box `□`
   - Sentence imitation lines $\rightarrow$ underscore writing lines without handwritten punctuation
4. **Borderless Fixed-Width Tables**: Multi-column exercises use borderless tables with explicitly defined column widths to ensure cross-platform layout stability.
5. **Page-by-Page PDF Inspection**: Verifies page count, overflow margins, and complete absence of answer leaks before delivery.

## How to Use With Your Agent

Ask your assistant in Chinese or English:

> *"Please convert this worksheet into a clean, printable Word document. Strip out the handwritten red answers and restore the blanks."*

Your assistant will load the native Chinese guidelines defined in this skill to generate the `.docx` file.

## Agent System Instructions

For the complete native Chinese agent prompt, see [`SKILL.md`](SKILL.md).

## License

[MIT License](LICENSE)
