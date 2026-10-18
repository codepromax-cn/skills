# CodeProMax Agent Skills

A catalog of reusable, cross-agent skills. Each skill has one canonical `SKILL.md` and can be installed into the native skill directory for a supported coding agent.

## Skills

| Skill | What it does |
| --- | --- |
| [clean-code](skills/clean-code/SKILL.md) | Applies practical Clean Code guidance while writing, reviewing, and refactoring code. |

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) to install skills directly into your agent's configuration.

### Quick Install by Agent

Choose your coding agent and copy its install command:

#### Claude Code
```sh
npx skills add codepromax-cn/skills --skill clean-code -a claude-code
```

#### Cursor
```sh
npx skills add codepromax-cn/skills --skill clean-code -a cursor
```

#### Kimi Code CLI
```sh
npx skills add codepromax-cn/skills --skill clean-code -a kimi-code-cli
```

#### Trae
```sh
npx skills add codepromax-cn/skills --skill clean-code -a trae
```

#### MiniMax Code
```sh
npx skills add codepromax-cn/skills --skill clean-code -a minimax-code
```

#### GitHub Copilot
```sh
npx skills add codepromax-cn/skills --skill clean-code -a github-copilot
```

#### Antigravity
```sh
npx skills add codepromax-cn/skills --skill clean-code -a antigravity
```

#### Codex
```sh
npx skills add codepromax-cn/skills --skill clean-code -a codex
```

#### Cline
```sh
npx skills add codepromax-cn/skills --skill clean-code -a cline
```

#### OpenCode
```sh
npx skills add codepromax-cn/skills --skill clean-code -a opencode
```

#### ZCode
```sh
npx skills add codepromax-cn/skills --skill clean-code -a zcode
```

#### Continue
```sh
npx skills add codepromax-cn/skills --skill clean-code -a continue
```

#### Kilo
```sh
npx skills add codepromax-cn/skills --skill clean-code -a kilo
```

#### Pi
```sh
npx skills add codepromax-cn/skills --skill clean-code -a pi
```

Add `--global` (or `-g`) to install user-wide instead of only for the current project.

### Interactive (Auto-Detect)

Run without flags to let the CLI auto-detect installed agents or prompt you interactively:

```sh
npx skills add codepromax-cn/skills --skill clean-code
```

### Install for All / Multiple Agents

Install to all supported agents in one command using the wildcard `-a '*'`:

```sh
npx skills add codepromax-cn/skills --skill clean-code -a '*'
```

Or specify all target agents explicitly:

```sh
npx skills add codepromax-cn/skills --skill clean-code \
  --agent claude-code \
  --agent codex \
  --agent antigravity \
  --agent opencode \
  --agent zcode \
  --agent pi \
  --agent cursor \
  --agent github-copilot \
  --agent cline \
  --agent continue \
  --agent kilo \
  --agent trae \
  --agent minimax-code \
  --agent kimi-code-cli
```

Run `npx skills add codepromax-cn/skills --list` to see the catalog. The CLI's supported agent list and native paths can change; consult its documentation for current targets.

## Compatibility

The skill content uses the common Agent Skills format: a folder with `SKILL.md`, YAML frontmatter containing `name` and `description`, and Markdown instructions. Agents use different project and user skill directories, so install through the CLI or follow the target agent's current documentation. The repository keeps one copy of each skill rather than maintaining agent-specific instruction forks.

DeepSeek Harness (DSH) can discover skills under `.dsh/skills/` and `.agents/skills/` when its filesystem skill provider is enabled. To use a skill with DSH, copy its folder into one of those locations; see the [DSH filesystem skill documentation](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md).

## Add a skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the folder layout, authoring conventions, and validation command.

## License

This repository is released under the [MIT License](LICENSE). Each installable skill also includes its own copy of the license so it remains licensed when distributed by itself.
