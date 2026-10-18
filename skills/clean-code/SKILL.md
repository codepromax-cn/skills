---
name: clean-code
description: "Use when writing code, implementing features, reviewing code, refactoring, or improving readability and maintainability. Apply practical Clean Code principles while following the project's conventions and the user's requirements."
license: MIT
---

# Clean Code

Use this skill by default for code writing and maintenance tasks. Apply Clean Code principles as practical guidance, not rigid quotas. Preserve requested behavior and APIs unless the user asks to change them.

## Priorities

- Follow the user's requirements, repository instructions, established patterns, and target-language idioms.
- Make the smallest change that improves the requested outcome. Avoid unrelated cleanup and speculative abstractions.
- If a clean-code preference conflicts with correctness, compatibility, performance, security, or the project's conventions, follow the stronger requirement and briefly explain a material tradeoff.

## Writing and changing code

- Choose names that reveal intent and match local conventions. For example, Python and Rust functions commonly use `snake_case`, while their types use `PascalCase`; Go uses mixed-case identifiers, with `PascalCase` for exported names. Follow the repository's formatter and existing style where it differs.
- Keep functions cohesive and at a consistent level of abstraction. Split a function when an extracted helper names a distinct idea, removes confusing nesting, or makes reuse clearer. Do not split code just to meet a line limit.
- Keep parameters and configuration understandable. Group related values when that creates a useful domain concept; avoid wrappers that only move arguments around. Use separate functions or named options when a boolean flag obscures intent.
- Make state changes and side effects visible. Prefer pure transformations when they simplify reasoning, while using mutation when it is the natural and clear choice for the language or task.
- Use guard clauses when they make the main path easier to follow. Avoid adding branches or helpers that make simple logic harder to read.
- Keep comments that explain rationale, constraints, or non-obvious decisions. Remove comments that merely restate code, and remove stale comments only after checking that they are no longer useful.
- Handle errors according to the language and surrounding API. Do not replace meaningful nullable or error states with empty defaults that change behavior.
- Name values when doing so explains their meaning, avoids repetition, or centralizes configuration. Obvious local literals do not need constants solely to eliminate literals.
- Reduce duplication when the repeated behavior is understood and a shared implementation makes future changes safer. Avoid premature generalization.

## Reviewing code

- Report findings with file and line locations when available, prioritizing correctness and behavior risks before readability issues.
- Keep feedback specific and concise. Explain why a finding matters and suggest a focused fix.
- A review request calls for findings; do not edit code unless the user also asks for a fix or refactor.

## Refactoring code

- Preserve externally visible behavior and interfaces unless the user requests a change.
- Focus on the requested code and its necessary dependencies. Avoid opportunistic rewrites.
- Summarize the meaningful changes briefly. Do not give a Clean Code lecture unless asked.
