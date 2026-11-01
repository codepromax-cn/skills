# 黑板/白板照片转可打印文档 (Blackboard to Printable)

[English](README.md) | [简体中文](README_zh.md)

将拍摄的课堂黑板、绿板或白板照片，转化为清晰高对比度、黑字白底的可打印 PNG 以及 300 DPI A4 PDF 文档。原汁原味保留板书手写字迹、数学公式与手绘草图，无 OCR 乱码或模型排版幻觉。

## 效果对比示例 (Example)

| 原始板书照片（处理前） | 打印版效果（处理后） |
| :---: | :---: |
| ![原始黑板照片](assets/example-input.jpg) | ![可打印处理效果](assets/example-output.jpg) |

## 一键安装

将此技能安装到您的 AI 编程助手：

```sh
# 自动检测当前智能体（Cursor、Antigravity、Claude Code 等）并安装
npx skills add codepromax-cn/skills --skill blackboard-to-printable

# 或全局安装（跨项目可用）
npx skills add codepromax-cn/skills --skill blackboard-to-printable -g
```

## 独立终端使用（无需通过智能体）

您也可以直接在命令行中运行内置的 Python 转换脚本。

### 1. 安装依赖

需要 Python 3.8+，依赖 Pillow 和 NumPy：

```sh
pip install -r requirements.txt
# 或直接安装：pip install "Pillow>=10.0.0" "numpy>=1.24.0"
```

### 2. 执行转换

```sh
# 基础用法（自动检测黑板/白板，输出 PNG 与 300 DPI A4 PDF）
python3 scripts/blackboard_to_printable.py lecture.jpg --out-dir ./output

# 自定义输出文件前缀，针对浅色粉笔调低阈值偏移
python3 scripts/blackboard_to_printable.py photo.jpg --name math_lecture_01 --thresh-offset 5

# 强制白板模式与 A4 竖版排版
python3 scripts/blackboard_to_printable.py whiteboard.png --mode whiteboard --orientation portrait
```

### 3. CLI 参数速查

| 参数 | 默认值 | 说明 |
| :--- | :--- | :--- |
| `input` | *(必填)* | 输入照片路径（JPG、PNG、HEIC、WEBP 等）。 |
| `--out-dir` | `.` | 输出文件存放目录。 |
| `--name` | `None` | 输出文件名前缀（默认使用输入照片文件名）。 |
| `--mode` | `auto` | 试卷/板面类型：`auto`（根据背景亮度自动判断）、`blackboard`（黑板粉笔）或 `whiteboard`（白板马克笔）。 |
| `--thresh-offset`| `15` | 大津法阈值偏移量（增大抑制背景杂质，减小捕捉浅色微弱粉笔字）。 |
| `--orientation` | `auto` | A4 PDF 页面方向：`auto`（匹配图片宽高比）、`landscape`（横版）或 `portrait`（竖版）。 |
| `--no-deskew` | `False` | 跳过水平行基准倾斜自动校正。 |
| `--no-pdf` | `False` | 仅输出 PNG 图片，不生成 PDF。 |

## 核心算法流程

1. **平场光照校正**：使用大半径高斯模糊（$\text{radius} = \max(w, h) / 15$）构建背景照度场，消除不均匀光照、眩光点和阴影。
2. **笔画对比度提取**：计算局部亮度差（黑板粉笔为 $G - B$；白板马克笔为 $B - G$）。
3. **自适应大津法（Otsu）阈值化**：纯 NumPy 实现全局自动最优阈值分割，辅以灵敏度偏移微调。
4. **形态学开运算**：$3\times 3$ 腐蚀-膨胀滤波消除粉笔粉尘飞溅斑点和微弱反光噪点。
5. **投影倾斜校正**：通过行投影方差自动检测倾斜角度并校正为水平。
6. **300 DPI 规范 A4 导出**：自适应纸张方向居中排版，保留匀称边距。

## 智能体系统指令

供 AI 助手加载的完整规范与系统提示词请参考 [`SKILL.md`](SKILL.md)。

## 开源协议

[MIT License](LICENSE)
