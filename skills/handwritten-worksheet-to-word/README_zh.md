# 手写练习题去手写转 Word (Handwritten Worksheet to Word)

[English](README.md) | [简体中文](README_zh.md)

> 对应中文指令技能包：[handwritten-worksheet-to-word-zh](../handwritten-worksheet-to-word-zh/README.md)

将拍好的中文练习题照片（通常已用红笔手写填写答案）还原为干净、可编辑、可打印的 Word (`.docx`) 文档。

## 一键安装

将此技能安装到您的 AI 编程助手：

```sh
# 自动检测当前智能体（Cursor、Antigravity、Claude Code 等）并安装
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word

# 或全局安装（跨项目可用）
npx skills add codepromax-cn/skills --skill handwritten-worksheet-to-word -g
```

## 功能特点

- **颜色决定去留**：去除红色手写答案，保留黑色印刷文字、题干及黑色印刷示例。
- **严格忠实原题**：保持原题题号、顺序、词语搭配、标点与括号位置，杜绝 OCR 幻觉或自主改写。
- **规范留空标准**：
  - 手写单字 $\rightarrow$ `（　）`（一个全角空格）
  - 手写双字 $\rightarrow$ `（　　）`（两个全角空格）
  - 标点填空方框 $\rightarrow$ 留空方框 `□`
  - 句子填空线 $\rightarrow$ 规范下划线，不带手写句中的标点
- **无边框表格排版**：多列题目一律使用无边框固定列宽表格对齐，避免因空格对齐导致的跨设备错位。
- **逐页检查验收**：生成文档后转 PDF 逐页验收排版、溢出与答案清除情况后再交付。

## 如何在 AI 助手中使用

安装完成后，直接发送试卷照片并向助手提问：

> “请帮我把这套手写练习题转成干净的 Word 文档，去掉手写的红字答案并恢复空格。”

AI 助手将自动加载本技能的规范并输出高质量的 Word 练习卷。

## 智能体系统指令

供 AI 助手加载的完整规范与系统提示词请参考 [`SKILL.md`](SKILL.md)。

## 开源协议

[MIT License](LICENSE)
