# CodeProMax Agent Skills

[English](README.md) | [简体中文](README_zh.md)

A catalog of reusable, cross-agent skills. Each skill has one canonical `SKILL.md` and can be installed into the native skill directory for a supported coding agent.

## Skills

### Code Quality & Engineering

| Skill | Language | What it does |
| :--- | :---: | :--- |
| [clean-code](skills/clean-code/SKILL.md) | En | Applies Clean Code principles and Martin Fowler's refactoring patterns to write, review, and safely evolve code. |

### Document Processing & Restoration

| Skill | Language | What it does |
| :--- | :---: | :--- |
| [blackboard-to-printable](skills/blackboard-to-printable/SKILL.md) | En | Turns blackboard and whiteboard photos into clean, black-on-white printable PNG and PDF files without OCR distortion. |
| [handwritten-worksheet-to-word](skills/handwritten-worksheet-to-word/SKILL.md) | En | Restores photos of handwritten Chinese practice worksheets into clean, printable, editable Word documents (.docx). |
| [handwritten-worksheet-to-word-zh](skills/handwritten-worksheet-to-word-zh/SKILL.md) | 中文 | Restores photos of handwritten Chinese practice worksheets into clean, printable, editable Word documents (.docx) (Chinese instructions). |

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) to install skills directly into your agent's configuration.

> [!NOTE]
> **Cross-Agent Compatibility**: Web registries like [skills.sh](https://skills.sh) default to showing `-a claude-code` in their copy snippet, but all skills in this repository are **agent-agnostic** and work across Claude Code, Cursor, Antigravity, GitHub Copilot, OpenAI Codex, and more.

### 1. Auto-Detect (Recommended)

Run without the `-a` flag to let the CLI automatically detect your installed agent(s):

```sh
# Install a specific skill (e.g., blackboard-to-printable)
npx skills add codepromax-cn/skills --skill blackboard-to-printable

# Or install interactively (lists all skills and prompts for selection)
npx skills add codepromax-cn/skills
```

Add `--global` (or `-g`) to install user-wide instead of only for the current project.

### 2. Install for All Agents / All Skills

Install a skill to all supported agents at once using `-a '*'`:

```sh
npx skills add codepromax-cn/skills --skill blackboard-to-printable -a '*'
```

Or install all skills to all detected agents:

```sh
npx skills add codepromax-cn/skills --all
```

### 3. Quick Install by Agent

Specify your target agent with `-a <agent>`. Replace `<skill-name>` with any skill from the catalog (e.g. `clean-code`, `blackboard-to-printable`, `handwritten-worksheet-to-word`, `handwritten-worksheet-to-word-zh`):

| Agent | One-Line Install Command |
| :--- | :--- |
| **Claude Code** | `npx skills add codepromax-cn/skills --skill <skill-name> -a claude-code` |
| **Cursor** | `npx skills add codepromax-cn/skills --skill <skill-name> -a cursor` |
| **Antigravity** | `npx skills add codepromax-cn/skills --skill <skill-name> -a antigravity` |
| **GitHub Copilot** | `npx skills add codepromax-cn/skills --skill <skill-name> -a github-copilot` |
| **Codex** | `npx skills add codepromax-cn/skills --skill <skill-name> -a codex` |
| **Kimi Code CLI** | `npx skills add codepromax-cn/skills --skill <skill-name> -a kimi-code-cli` |
| **Trae** | `npx skills add codepromax-cn/skills --skill <skill-name> -a trae` |
| **MiniMax Code** | `npx skills add codepromax-cn/skills --skill <skill-name> -a minimax-code` |
| **Cline** | `npx skills add codepromax-cn/skills --skill <skill-name> -a cline` |
| **OpenCode** | `npx skills add codepromax-cn/skills --skill <skill-name> -a opencode` |
| **ZCode** | `npx skills add codepromax-cn/skills --skill <skill-name> -a zcode` |
| **Continue** | `npx skills add codepromax-cn/skills --skill <skill-name> -a continue` |
| **Kilo** | `npx skills add codepromax-cn/skills --skill <skill-name> -a kilo` |
| **Pi** | `npx skills add codepromax-cn/skills --skill <skill-name> -a pi` |

Run `npx skills add codepromax-cn/skills --list` to view all available skills in the repository.

## Compatibility

The skill content uses the common Agent Skills format: a folder with `SKILL.md`, YAML frontmatter containing `name` and `description`, and Markdown instructions. Agents use different project and user skill directories, so install through the CLI or follow the target agent's current documentation. The repository keeps one copy of each skill rather than maintaining agent-specific instruction forks.

DeepSeek Harness (DSH) can discover skills under `.dsh/skills/` and `.agents/skills/` when its filesystem skill provider is enabled. To use a skill with DSH, copy its folder into one of those locations; see the [DSH filesystem skill documentation](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md).

## Add a skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the folder layout, authoring conventions, and validation command.

## License

This repository is released under the [MIT License](LICENSE). Each installable skill also includes its own copy of the license so it remains licensed when distributed by itself.
