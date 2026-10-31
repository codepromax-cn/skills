# CodeProMax 智能体技能库 (Agent Skills)

[English](README.md) | [简体中文](README_zh.md)

可复用的跨 AI 智能体技能目录。每个技能均包含一份标准的规范文件（`SKILL.md`），可一键安装到各支持的 AI 编程助手及智能体的原生技能目录中。

## 技能目录 (Skills)

### 代码质量与工程实践 (Code Quality & Engineering)

| 技能名称 | 语言 | 功能说明 |
| :--- | :---: | :--- |
| [clean-code](skills/clean-code/SKILL.md) | 英文 | 应用 Clean Code 原则与 Martin Fowler 重构模式，规范化编写、审查并安全演进代码。 |

### 文档处理与格式还原 (Document Processing & Restoration)

| 技能名称 | 语言 | 功能说明 |
| :--- | :---: | :--- |
| [blackboard-to-printable](skills/blackboard-to-printable/SKILL.md) | 英文 | 将黑板与白板照片转化为清晰高对比度、黑字白底的打印版 PNG 与 A4 PDF，杜绝 OCR 乱码与文字走形。 |
| [handwritten-worksheet-to-word](skills/handwritten-worksheet-to-word/SKILL.md) | 英文 | 将拍好的中文练习题照片（含红笔手写答案）还原为干净、可编辑、可打印的 Word (.docx) 文档。 |
| [handwritten-worksheet-to-word-zh](skills/handwritten-worksheet-to-word-zh/SKILL.md) | 中文 | 将拍好的中文练习题照片（含红笔手写答案）还原为干净、可编辑、可打印的 Word (.docx) 文档。 |

## 安装指南 (Install)

推荐使用 [Skills CLI](https://github.com/vercel-labs/skills) 将技能直接安装到智能体配置中。

> [!NOTE]
> **跨智能体兼容性**：虽然 [skills.sh](https://skills.sh) 等网页端目录默认展示 `-a claude-code` 复制命令，但本仓库中的所有技能均**与平台无关**，原生兼容 Claude Code、Cursor、Antigravity、GitHub Copilot、OpenAI Codex 等主流助手。

### 1. 自动检测（推荐）

执行命令时不带 `-a` 参数，CLI 会自动检测当前系统或项目中已安装的 AI 助手：

```sh
# 安装指定技能（例如：blackboard-to-printable）
npx skills add codepromax-cn/skills --skill blackboard-to-printable

# 或交互式安装（列出所有技能供您勾选）
npx skills add codepromax-cn/skills
```

添加 `--global`（或 `-g`）参数可进行全局安装（作用于当前用户，跨项目可用），而非仅限当前项目。

### 2. 为所有助手安装 / 安装全部技能

使用通配符 `-a '*'` 将某个技能同时安装到所有已检测到的助手：

```sh
npx skills add codepromax-cn/skills --skill blackboard-to-printable -a '*'
```

或者使用 `--all` 一键把所有技能安装到所有支持的助手：

```sh
npx skills add codepromax-cn/skills --all
```

### 3. 按助手单独安装

通过 `-a <agent>` 指定目标助手。将 `<skill-name>` 替换为技能目录中的名称（如 `clean-code`、`blackboard-to-printable`、`handwritten-worksheet-to-word`、`handwritten-worksheet-to-word-zh`）：

| 目标智能体 | 一键安装命令 |
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

执行 `npx skills add codepromax-cn/skills --list` 可以直接查看本仓库支持的所有技能列表。

## 兼容性说明 (Compatibility)

技能内容采用通用的 Agent Skills 格式：每个技能均为一个包含 `SKILL.md` 的独立文件夹，头部包含包含 `name` 和 `description` 的 YAML Frontmatter 元数据，正文使用 Markdown 格式指令。各智能体使用的项目及用户技能目录路径不同，可通过 CLI 自动安装或参考对应助手的官方文档手动配置。本仓库每项技能均保持单一权威实现，避免维护特定助手的指令分支。

DeepSeek Harness (DSH) 开启文件系统技能提供程序后，可自动发现 `.dsh/skills/` 和 `.agents/skills/` 目录下的技能。若要在 DSH 中使用技能，只需将技能文件夹复制到上述任一目录；详见 [DSH 文件系统技能文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md)。

## 添加新技能 (Add a skill)

目录结构规范、编写原则与校验方法请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 开源协议 (License)

本仓库采用 [MIT 许可证](LICENSE) 开源。每个可单独安装的技能也附带独立的许可证副本，以便独立分发时保持授权完整。
