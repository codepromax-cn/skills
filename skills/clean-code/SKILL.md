---
name: clean-code
description: "Use when writing code, implementing features, reviewing code, refactoring, or improving readability and maintainability. Apply practical Clean Code principles and Martin Fowler's refactoring techniques to write, review, and safely evolve code."
license: MIT
---

# Clean Code

Use this skill by default for code writing, maintenance, review, and refactoring tasks. Apply Clean Code principles and disciplined refactoring techniques as practical engineering guidance, not rigid dogma. Preserve requested behavior, public APIs, and project conventions unless explicitly asked to change them.

## Priorities

- Follow the user's requirements, repository instructions, established patterns, and target-language idioms.
- Make the smallest change that improves the requested outcome. Avoid unrelated cleanup and speculative abstractions.
- If a clean-code or refactoring preference conflicts with correctness, compatibility, performance, security, or existing project conventions, follow the stronger requirement and briefly explain any material tradeoff.

## Refactoring rhythm and safety

- **Separate refactoring from feature changes**: Never mix structural refactoring with behavioral changes or feature additions in the same change. When restructuring code, keep external behavior and APIs unchanged while keeping all tests green. When adding functionality, build cleanly on the existing structure.
- **Maintain a test safety net**: Never refactor without automated tests. If test coverage is missing or inadequate, write characterization (pinning) tests first to capture current behavior before changing code structure.
- **Refactor in micro-steps**: Make small, incremental transformations. Run tests after every atomic change. If tests break, immediately revert to the last green state and take a smaller step rather than entering prolonged debugging.
- **Preparatory refactoring**: Before adding a new feature or fixing a complex bug, ask: "How can I restructure existing code to make this change easy?" Restructure the code first so the addition is straightforward ("Make the change easy, then make the easy change").
- **Opportunistic cleanup**: Leave code cleaner than you found it (litter-pickup refactoring) when working in an area, but keep the cleanup focused and strictly bounded to the touched context.

## Recognizing code smells

When writing, reviewing, or refactoring code, watch for these specific smells:

- **Mysterious Name**: Functions, variables, or types whose names hide intent, mislead, or require decoding.
- **Long Function & Large Class**: Functions or classes that do too much, mix abstraction levels, or violate the Single Responsibility Principle.
- **Long Parameter List & Data Clumps**: Multiple parameters that repeatedly travel together without a domain abstraction.
- **Primitive Obsession**: Relying on generic strings, numbers, or dictionaries instead of lightweight domain types or value objects.
- **Feature Envy**: A function or method that accesses the data or functions of another module more than its own.
- **Shotgun Surgery & Divergent Change**: A single logical change requires edits across many files (shotgun surgery), or one module frequently changes for multiple unrelated reasons (divergent change).
- **Repeated Conditionals / Switches**: Duplicated `switch` or `if/else` ladders across the codebase that should be replaced with polymorphism, lookup tables, or strategy objects.
- **Mutable & Shared State**: Uncontrolled mutations across shared variables or objects, making concurrent and sequential reasoning fragile.
- **Speculative Generality & Dead Code**: Unused hooks, parameters, dead branches, or premature abstractions created for hypothetical future needs.
- **Comments as Deodorant**: Comments that explain *what* convoluted code does rather than *why* a constraint or business rule exists.

## Writing and changing code

- Choose names that reveal intent and match local conventions. For example, TypeScript and JavaScript commonly use `camelCase` with `PascalCase` for types; Python and Rust use `snake_case` with `PascalCase` for types; Go uses mixed-case identifiers, with `PascalCase` for exported names. Follow the repository's formatter and existing style where it differs.
- Keep functions cohesive and at a consistent level of abstraction. Split a function when an extracted helper names a distinct concept, removes confusing nesting, or clarifies intent. Do not split code solely to satisfy arbitrary line limits.
- Keep parameters understandable. Group related values into parameter objects or domain structures when that creates a cohesive concept; avoid wrappers that only move arguments around. Avoid boolean flags that obscure intent; prefer explicit functions or named options.
- Separate queries from modifiers (Command-Query Separation): functions that return values should ideally be free of observable side effects.
- Manage resource lifecycles explicitly using idiomatic patterns (context managers, `defer`, RAII, explicit cancellation, timeouts).
- Use guard clauses to handle preconditions, invalid inputs, and error states early, flattening deeply nested control flow.
- Prefer idiomatic data pipelines (e.g., `map`, `filter`, comprehensions, iterators) over complex manual loop manipulation when they enhance readability.
- Keep comments that explain rationale, constraints, or non-obvious decisions. Remove comments that merely restate code, and remove stale comments only after checking that they are no longer useful.
- Handle errors according to the language and surrounding API. Do not replace meaningful nullable or error states with silent empty defaults that mask failure.
- Name constants when doing so explains domain meaning, centralizes configuration, or prevents brittle magic literals.
- Reduce duplication when the repeated behavior is understood and a shared implementation makes future changes safer. Avoid premature generalization.
- Cover non-trivial logic and edge cases with focused tests. Verify against existing test suites and never delete or weaken assertions merely to force tests to pass.

## Systematic refactoring moves

When restructuring code, draw from standard refactoring moves:

- **Composing functions**:
  - *Extract Function*: Turn a cohesive fragment of code into a well-named helper function.
  - *Inline Function*: Remove unnecessary indirection when a function body is as clear as its name.
  - *Extract Variable*: Introduce an explaining variable to clarify a complex subexpression or condition.
- **Simplifying conditional logic**:
  - *Decompose Conditional*: Extract condition, then-branch, and else-branch into separate explanatory functions.
  - *Replace Nested Conditional with Guard Clauses*: Return or exit early to keep the happy path unindented.
  - *Replace Conditional with Polymorphism / Lookup*: Replace repetitive type or status branching with polymorphic dispatch or dictionary lookups.
- **Organizing data & state**:
  - *Encapsulate Variable*: Hide direct access to mutable data behind functions or getters/setters when mutations need control.
  - *Introduce Parameter Object*: Bundle cohesive parameters into a dedicated structure or record.
  - *Replace Primitive with Object*: Wrap primitive types (e.g. phone number, currency, coordinate) in domain value objects.
- **Moving features & improving APIs**:
  - *Move Function / Move Field*: Relocate logic closer to the data it interacts with most (curing Feature Envy).
  - *Remove Flag Argument*: Replace boolean parameters that branch behavior with explicit, distinctly named functions.
  - *Slide Statements*: Keep related variable declarations and usage close together.

## Reviewing code

- Diagnose specific code smells by name and recommend targeted refactoring moves.
- Report findings with file and line locations, prioritizing correctness, security, and behavioral risks before structural or readability issues.
- Categorize findings by severity (e.g., Blocker/Bug, Risk/Smell, Suggestion/Nit) so the most impactful issues are addressed first.
- Keep feedback specific, objective, and concise. Explain why the smell matters and provide a minimal code example showing the refactored alternative.
- A review request calls for findings; do not edit code unless the user also asks for a fix or refactor.

## Refactoring code

- Verify that existing automated tests pass before altering structure. If missing, write characterization tests first.
- Preserve externally visible behavior and public APIs unless the user requests a change.
- Refactor in micro-steps, running tests after each atomic change to guarantee zero regressions.
- Keep diffs tightly focused on the target code and its immediate dependencies. Avoid opportunistic sprawling rewrites.
- Summarize changes briefly by naming the refactoring moves applied (e.g., "Extracted `calculate_discount()`, introduced `BillingOptions` parameter object").
