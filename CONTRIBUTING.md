# Contributing

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` and a sibling `skills/<skill-name>/LICENSE` copied from the repository's root `LICENSE`.
2. Use the same lowercase, hyphenated identifier for the directory and the frontmatter `name`.
3. Write a concise `description` that says what the skill does and when an agent should use it. Keep it within the Agent Skills limit of 1024 characters.
4. Keep the core instructions portable: use the common `name`, `description`, and Markdown format. Add platform-specific metadata only when it provides a real benefit, and keep the skill usable without it.
5. Link supporting references directly from `SKILL.md`. Add scripts, references, or assets only when they materially support the skill.
6. Update the catalog in `README.md` and run the validator.

## Authoring principles

- Give each skill a focused responsibility and describe its trigger clearly.
- Treat style rules as guidance where language idioms or repository conventions vary.
- Preserve explicit user requirements and existing project conventions.
- Prefer original, concise instructions over copied manuals or source material.
- Keep each skill self-contained enough to install by itself. Its `LICENSE` file and `license: MIT` frontmatter travel with it.

## Validate

Install the small development dependency set, then run:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

The GitHub Actions workflow runs the same validator on pushes and pull requests.
