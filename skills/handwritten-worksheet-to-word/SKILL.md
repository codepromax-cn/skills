---
name: handwritten-worksheet-to-word
description: "Turn photos of Chinese practice worksheets (typically filled in with red handwriting) into clean, editable, printable Word (.docx) documents. Strips red handwritten answers, restores blank brackets/underlines, aligns multi-column exercises with borderless tables, and preserves question order without OCR hallucination."
license: MIT
category: document-processing
tags:
  - worksheet
  - handwriting-removal
  - word
  - docx
  - education
language: en
---

# Handwritten Worksheet to Word

> Language versions: **English** | [简体中文 (Chinese)](../handwritten-worksheet-to-word-zh/SKILL.md)

This is a platform-independent skill document. Give it as-is to any AI assistant, as a skill file, system instruction, or project instruction. It is not tied to any single platform, because it names no platform-specific tools or paths.

## 1. What this skill does

Turn photos of a Chinese practice worksheet, usually already filled in with red handwriting, into a clean, editable, printable Word document.

Use it when:

- Photos of a worksheet have already been filled in by hand and need to be restored to a blank worksheet
- One worksheet was photographed in several photos and needs to be joined into a single document in order
- There is no supplied template, so the layout should follow the photos instead of being redesigned

Do not use it when:

- The user supplied a template file and asked to keep its header, seal line, footer, and page setup exactly as supplied, replacing only the body text. That is a separate template-rebuild method, not this skill.

## 2. Input and output

Input:

- One or more clear photos of a worksheet, in which both printed text and handwriting are legible
- Any special user requirements, such as title colour, paper size, or whether answers should be kept. The user's latest requirement always wins.

Output:

- One Word document (.docx) with editable text, not an image
- The document first, followed by a short note stating how many pages it has, which sections it includes, what was removed, and where it ends

## 3. Environment requirements (generic, not platform-specific)

The assistant using this skill needs the following abilities. If one specific tool is missing, use an equivalent tool available in that environment instead of declaring the task impossible:

- Read user-uploaded images and zoom into local details
- Generate and edit Word documents, for example with Python and the python-docx library, or an equivalent Word library
- Convert Word to PDF for preview and check it page by page, for example with LibreOffice or an equivalent conversion tool
- Deliver the finished file to the user for download or viewing

Keep working files and delivered files separate. Intermediate files go in a working directory. Only the finished file goes in the delivery directory, and only the finished file is sent to the user.

## 4. Core principles

1. **Colour decides what stays, not position.** Keep black printed characters. Remove red handwritten characters, even when a red character follows an example label. Keep a black example character that sits in the same kind of blank.
2. **Remove handwriting only.** Do not change the wording, question order, word pairings, punctuation positions, or bracket positions shown in the photos.
3. **Do not invent answers or questions.** Do not add questions that are not in the photos. If a character is illegible and cannot reasonably be judged, say so in the delivery note instead of quietly guessing one.
4. **Do not reproduce watermarks.** App watermarks, collection marks, and similar marks in the corner of a photo are not part of the worksheet and must not appear in the document.
5. **The print title is black by default.** Even when the title in a photo looks red, use black for the print version, unless the user explicitly asks for a coloured title.

## 5. Workflow

### Step 1: Look carefully before starting

- Order all photos by question number, not by upload order alone.
- Check whether the last line of one photo continues at the top of the next photo. If it does, those photos are consecutive pages of the same worksheet and must be joined.
- Zoom into messy areas at twice size before transcribing, especially measure words, antonyms, two-character blanks, and easily confused characters.
- When handwriting is unclear, use the noun and the common collocation to judge it. For example, the measure word for a mountain bird follows common usage. If the reading is still uncertain after that check, say so in the delivery note instead of pretending to be certain.

### Step 2: Transcribe question by question, separating print from handwriting

- Transcribe section by section and item by item. Do not skip items and do not merge different sections.
- For each item, first separate black printed characters from red handwritten characters.
- Keep the original wording, order, and punctuation. Leave every answer blank empty.

### Step 3: Leave blanks by rule

| What the photo shows | What to put in Word |
|---|---|
| A handwritten single character inside parentheses, for example a word with a handwritten character in brackets | An empty bracket with one full-width space inside, for example （　） plus the rest of the word, with the brackets in their original place |
| A handwritten two-character phrase inside parentheses, for example a descriptive phrase in brackets | An empty bracket with two full-width spaces inside, for example （　　） plus the rest of the phrase |
| A punctuation box containing a handwritten punctuation mark, for example a small square box with a comma inside | An empty square box, □, in its original place, with nothing inside it |
| A sentence-imitation item with a full-width writing line underneath and a handwritten sentence on that line | Keep the example sentence, then put a line of underscores on its own line as the writing line, and do not add the punctuation from the handwritten sentence |
| A simile or completion item where the prompt is printed and the rest is handwritten, for example a prompt ending in “like” followed by a handwritten simile | Keep the printed prompt, then put underscores inside the sentence as the fill-in blank. If the original prompt already ends with printed punctuation after the line, keep that punctuation. If the punctuation was handwritten, do not add it |
| A prompt that already has a printed full stop after its writing line, for example a prompt, a line, and a full stop | Keep the prompt, keep the underscore line, and keep the printed full stop |
| A black printed example, for example an example word, an example phrase, or an example measure word in brackets | Keep the example exactly as printed. Do not turn it into a blank |
| The same item appearing twice in the photos, for example the same measure-word phrase in two places | Keep it twice exactly as shown. Do not remove the duplicate and do not “correct” it |

### Step 4: Join multiple photos into one document

- Put the title and the class, student number, name, and grade header only once, at the top of the document. Do not repeat the title on later pages.
- Keep question numbering continuous. If the first photo ends in the middle of a section and the second photo continues that section, continue the numbering instead of restarting at one.
- End the document at the last item visible in the last photo, and tell the user where it ends. If the last item itself is cut off in the photo, say so. Do not write the rest of it.
- If the user later sends further photos, continue the existing document instead of starting a new document with a different title.

### Step 5: Layout

Default layout, when the user has not supplied a template:

- **Paper**: A4 portrait
- **Margins**: 1.8 cm top and bottom, 1.9 cm left and right
- **Body font**: SimSun (宋体), 14 pt. Section headings: SimSun, 15 pt, bold
- **Title**: centred, black, about 20 pt, bold. The class, student number, name, and grade line is centred, with blanks shown as underlines

Table layout, which is where most errors happen:

- Build every multi-column section as a borderless table. Do not align columns with spaces.
- Use a fixed table layout and state the total table width and each column width explicitly. Without fixed widths, some renderers clip the first and last cells.
- For a pinyin homophone section: 5 columns, one whole word per cell, centred in its column, with the pinyin centred above its group. A typical column width is 3.44 cm. Leave extra space before each new pinyin block so groups stay visually separate.
- Do not split a word into single-character cells. That pulls characters apart, makes words look crowded, and breaks the word as a unit.
- A word is narrower than its column. Centring it leaves a natural gap between neighbouring columns. That gap is intentional. Do not stretch words to fill the column width.
- For verb phrases, measure words, antonyms, and descriptive-phrase sections, use the column count shown in the photo, commonly 4, 3, 4, and 3 columns. Put an example label such as “Example:” on its own heading line, and do not repeat that label inside the table rows below it.
- Check every underscore writing line in the PDF preview. A writing line must stay on one line. Shorten it if it wraps to a second line.

### Step 6: Convert to PDF, check page by page, and only then deliver

Checklist. Deliver only when every item passes:

- [ ] The page count is reasonable, with no blank pages and no unexpected overflow
- [ ] Every section and item from every photo appears in order, with no missing items and no skipped numbers
- [ ] All red handwritten answers have been removed, and the finished text contains none of the handwritten answer phrases
- [ ] Brackets, square boxes, and underscore lines match the photos in position and count
- [ ] Tables are not clipped, and words are not split apart
- [ ] The title is black, unless the user asked for colour, and no photo watermark appears
- [ ] The last item in the document is the last item in the last photo, with nothing invented after it

How to check:

- Convert Word to PDF and inspect every page, not only the first page.
- Search the document text for several known handwritten answer phrases and confirm they do not appear in the finished file.
- If a problem is found, fix the document, convert to PDF again, and check again. Do not deliver with a known problem still in it.

## 6. How to present the delivery

Send the file first, then a short note of about three sentences covering:

1. How many pages it has and which sections it includes
2. What was removed, for example that all red handwriting was removed and left blank, and that watermarks were not included
3. Where the document ends, and a reminder that later photos can be joined on if the user sends them

Do not write handwritten answers in the delivery note. The user asked for a blank worksheet, so the note must not contain the answers either.

## 7. Common pitfalls

- Do not judge by the example label. Judge by colour. A black example character stays. A red example character goes.
- Do not split words into single-character grid cells to force alignment.
- Do not align multi-column questions with spaces. Spaces align differently on different devices.
- Do not remove a repeated item, and do not “correct” a repetition in the photos.
- Do not copy the photo title colour directly into the print version. The print default is black.
- Do not invent the next question after the last photo.
- Do not make a writing line so long that it wraps to a second line.

## 8. Notes for use in another assistant

- Give this document directly to the assistant as a skill file, system instruction, or project instruction. No additional file is required.
- If the assistant environment has no python-docx, use any library that can generate .docx files instead. Keep the layout numbers for paper, font size, and column width unchanged.
- If the assistant environment cannot convert to PDF, use that environment's own Word preview and check page by page instead. The checklist does not change.
- When the user sends new photos, first ask whether they continue the previous document, then continue that document instead of starting a new document with a different title.
