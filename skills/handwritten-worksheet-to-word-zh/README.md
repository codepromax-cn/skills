# 手写练习题去手写转 Word 智能体技能

> 语言版本：[English (英文版)](../handwritten-worksheet-to-word/README.md) | **简体中文**

将拍好的中文练习题照片（通常已用红笔手写填写答案）还原为干净、可编辑、可打印的 Word (`.docx`) 文档。

## 一键安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 将此技能一键安装至您的 AI 编程助手或智能体环境：

```sh
# 自动检测当前智能体（Cursor、Antigravity、Claude Code 等）并安装
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word-zh

# 或安装至全局环境（跨项目可用）
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word-zh -g
```

## 核心处理规则

1. **颜色决定去留**：保留黑色印刷文字，去除红色手写字。黑色的例字保留，红色的答案字坚决去掉。
2. **只去手写，不改题目**：题干文字、题号顺序、词搭配、标点与括号位置严格按照片原样保留；不编题、不猜字、不带照片水印。
3. **按规范统一留空**：
   - 括号内为手写单字 $\rightarrow$ 空括号 `（　）`（内含一个全角空格）
   - 括号内为手写双字 $\rightarrow$ 空括号 `（　　）`（内含两个全角空格）
   - 标点填空方框 $\rightarrow$ 留空方框 `□`
   - 仿写/长句书写线 $\rightarrow$ 规范下划线，不带手写句中的标点
4. **无边框固定列宽表格排版**：多列题目一律使用无边框表格对齐，不使用空格硬顶，避免跨平台换行错位。
5. **PDF 逐页严格验收**：交付前自动转 PDF 逐页检查，确认无空白溢出页、无手写字泄漏残留。

## 如何在 AI 助手中使用

安装完成后，直接向 AI 助手发送拍好的试卷照片并输入指令：

> “请帮我把这套手写练习题照片还原成干净的空白练习卷（Word 文档），去掉所有的手写答案。”

AI 助手将自动加载本技能的规范，使用 `python-docx` 生成高质量文档并交付。

## 智能体系统提示词与完整规范

供 AI 智能体加载的完整系统指令规范请见 [`SKILL.md`](SKILL.md)。

## 开源协议

[MIT License](LICENSE)
