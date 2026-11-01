# Clean Code & Refactoring

[English](README.md) | [简体中文](README_zh.md)

A portable AI agent skill that applies Clean Code engineering principles and Martin Fowler's refactoring patterns to guide code writing, pull request reviews, and systematic refactoring.

## Install

Install this skill into your coding agent using the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
# Auto-detects your active agent (Cursor, Antigravity, Claude Code, etc.)
npx skills add codepromax-cn/skills --skill clean-code

# Or install for a specific agent
npx skills add codepromax-cn/skills --skill clean-code -a cursor
npx skills add codepromax-cn/skills --skill clean-code -a antigravity
npx skills add codepromax-cn/skills --skill clean-code -a claude-code
```

Add `--global` (or `-g`) to install user-wide.

## Key Principles at a Glance

- **Intention-Revealing Names**: Names reflect domain intent and adhere to local language conventions.
- **Cohesive Functions**: Small, focused functions at a single level of abstraction with short parameter lists.
- **Guard Clauses**: Unnest the happy path using early returns instead of deeply nested if-else ladders.
- **Disciplined Refactoring**:
  - **Test Safety Net**: Verify characterization/unit tests before altering structure.
  - **Micro-Steps**: Take small, incremental steps (Extract Function, Parameter Object, Decompose Conditional) and verify tests after each atomic change.
  - **Preparatory Refactoring**: "Make the change easy, then make the easy change."
- **Actionable Code Review**: Diagnose code smells by standard names (*Long Function, Feature Envy, Primitive Obsession, Data Clumps*) and prioritize findings by severity (Blocker, Risk, Suggestion).

## Agent Instructions

For the complete system prompt and behavioral guidelines loaded by AI coding assistants, see [`SKILL.md`](SKILL.md).

## License

[MIT License](LICENSE)
