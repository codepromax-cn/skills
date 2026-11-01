# Clean Code 与代码重构技能 (Clean Code & Refactoring)

[English](README.md) | [简体中文](README_zh.md)

跨 AI 编程助手的通用技能，应用 Clean Code 核心工程原则与 Martin Fowler 重构模式指导代码编写、Pull Request 审查及系统性重构。

## 一键安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 将此技能安装到您的 AI 助手配置中：

```sh
# 自动检测当前使用的智能体（Cursor、Antigravity、Claude Code 等）并安装
npx skills add codepromax-cn/skills --skill clean-code

# 或针对特定智能体单独安装
npx skills add codepromax-cn/skills --skill clean-code -a cursor
npx skills add codepromax-cn/skills --skill clean-code -a antigravity
npx skills add codepromax-cn/skills --skill clean-code -a claude-code
```

添加 `--global`（或 `-g`）参数可进行全局安装（跨项目可用）。

## 核心原则速览

- **见名知意**：名称清晰表达领域意图，严格遵循编程语言本地命名规范。
- **高内聚小函数**：函数短小、职责单一且处于同一抽象层次，参数列表尽量简短。
- **卫语句（Guard Clauses）**：使用卫语句提前退出，保持主干代码扁平无深层嵌套。
- **纪律性重构**：
  - **测试安全网**：修改结构前确保测试通过；缺少测试时先编写保护性测试。
  - **微步演进**：每次仅执行单一小步重构（提炼函数、引入参数对象、分解条件式等），小步验证。
  - **准备式重构**：“先让改变变容易，再去进行容易的改变”。
- **可落地的代码审查**：准确定位代码坏味道名称（过长函数、依恋情结、基本类型偏执、数据泥团等），按严重程度（阻碍项、风险项、建议项）分级提出具体改进建议。

## 智能体系统指令

供 AI 助手加载的完整规范与系统提示词请参考 [`SKILL.md`](SKILL.md)。

## 开源协议

[MIT License](LICENSE)
