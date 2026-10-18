---
name: clean-code
description: "Use when writing code, implementing features, reviewing code, refactoring, or improving readability and maintainability. Apply practical Clean Code principles and Martin Fowler's refactoring techniques to write, review, and safely evolve code."
license: MIT
---

# Clean Code

Use this skill by default for code writing, maintenance, review, and refactoring tasks. Apply Clean Code principles and disciplined refactoring as practical engineering guidance, not rigid dogma. Preserve requested behavior, public APIs, and project conventions unless explicitly asked to change them.

## Priorities

- Follow user requirements, repository instructions, established patterns, and language idioms.
- Make the smallest change that improves the outcome. Avoid unrelated cleanup and speculative abstractions.
- If clean-code or refactoring preferences conflict with correctness, compatibility, performance, security, or conventions, follow the stronger requirement and briefly explain the tradeoff.

## Writing and changing code

- **Names**: Choose intention-revealing names matching local conventions (e.g., `camelCase`, `snake_case`, `PascalCase`).
- **Functions**: Keep functions cohesive and at a consistent level of abstraction. Extract helpers when they name a distinct concept, remove confusing nesting, or clarify intent, not just to meet line limits.
- **Parameters**: Keep parameter lists short. Group related values into parameter objects or domain records. Avoid boolean flag arguments; prefer explicit functions or named options.
- **Control flow**: Use guard clauses to exit early and keep the happy path unnested. Decompose complex conditionals and prefer idiomatic data pipelines over manual loop index manipulation.
- **State & Side Effects**: Separate queries from modifiers (Command-Query Separation). Make side effects explicit and manage resource lifecycles cleanly (context managers, `defer`, RAII, timeouts).
- **Errors & Nulls**: Handle errors idiomatically. Never silently replace meaningful nullable or error states with empty defaults that mask failure.
- **Comments & Constants**: Keep comments that explain *why* (constraints, non-obvious rationale); remove comments that merely restate code. Name constants for domain meaning, not for obvious local literals.
- **Testing**: Cover non-trivial logic and edge cases with focused tests. Verify against existing test suites and never delete or weaken assertions merely to pass.

## Refactoring discipline

- **Separate refactoring from feature changes**: Never mix structural restructuring with behavioral changes or new features in the same change. When restructuring code, keep external behavior and APIs unchanged while keeping all tests green.
- **Test safety net**: Verify existing tests pass before altering structure. If test coverage is missing or inadequate, write characterization (pinning) tests first.
- **Micro-steps**: Make small, incremental transformations (e.g., Extract Function, Introduce Parameter Object, Move Function). Run tests after every atomic change; revert immediately on failure rather than deep-debugging.
- **Preparatory refactoring**: Before adding a feature or fixing a complex bug, restructure existing code first so the addition is straightforward ("Make the change easy, then make the easy change").
- **Focused scope**: Leave code cleaner in the touched area (litter-pickup refactoring), but keep diffs strictly bounded to the requested scope. Summarize changes by named refactoring moves.

## Reviewing code & identifying smells

- **Diagnose specific smells**: Identify code smells by name (*Long Function & Large Class, Primitive Obsession, Data Clumps, Feature Envy, Shotgun Surgery & Divergent Change, Repeated Conditionals, Mutable State, Comments as Deodorant*) and suggest targeted refactoring moves.
- **Prioritize impact**: Report findings with file and line locations, ordering by severity: Blocker/Bug, Risk/Smell, Suggestion/Nit. Prioritize correctness and security before readability.
- **Actionable & non-invasive**: Provide specific rationale with concise fix examples. Do not edit code during a review request unless explicitly asked.
