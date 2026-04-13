# GESP 题目分类工具

本项目用于处理和分类GESP（中国计算机学会青少年编程能力等级认证）的题目PDF文件，按语言和级别进行分类整理，方便教师和学生查找和使用。

## 项目功能

- **Scratch题目分类**：将Scratch（图形化编程）题目按1-4级分类
- **Python题目分类**：将Python题目按1-8级分类
- **C++题目分类**：将C++题目按1-8级分类
- **自动化处理**：通过脚本自动识别文件名中的级别信息并分类

## 目录结构

```
gesp/
├── gesp_pdfs/          # 原始PDF文件目录
├── scratch_questions/  # Scratch题目按级别分类
│   ├── level_1/        # 一级题目
│   ├── level_2/        # 二级题目
│   ├── level_3/        # 三级题目
│   └── level_4/        # 四级题目
├── python_questions/   # Python题目按级别分类
│   ├── level_1/        # 一级题目
│   ├── level_2/        # 二级题目
│   ├── level_3/        # 三级题目
│   ├── level_4/        # 四级题目
│   ├── level_5/        # 五级题目
│   ├── level_6/        # 六级题目
│   ├── level_7/        # 七级题目
│   └── level_8/        # 八级题目
├── cpp_questions/      # C++题目按级别分类
│   ├── level_1/        # 一级题目
│   ├── level_2/        # 二级题目
│   ├── level_3/        # 三级题目
│   ├── level_4/        # 四级题目
│   ├── level_5/        # 五级题目
│   ├── level_6/        # 六级题目
│   ├── level_7/        # 七级题目
│   └── level_8/        # 八级题目
├── process_scratch_pdfs.py  # Scratch处理脚本
├── process_python_pdfs.py   # Python处理脚本
├── process_cpp_pdfs.py      # C++处理脚本
└── README.md           # 项目说明文件
```

## 使用方法

### 1. 准备PDF文件
将GESP相关的PDF文件放入 `gesp_pdfs/` 目录中。

### 2. 运行处理脚本

#### 处理Scratch题目
```bash
python3 process_scratch_pdfs.py
```

#### 处理Python题目
```bash
python3 process_python_pdfs.py
```

#### 处理C++题目
```bash
python3 process_cpp_pdfs.py
```

### 3. 查看分类结果
处理完成后，可在以下目录查看按级别分类的题目：
- `scratch_questions/` - Scratch题目
- `python_questions/` - Python题目
- `cpp_questions/` - C++题目

## 技术实现

- 使用Python脚本自动处理PDF文件
- 通过正则表达式从文件名中提取级别信息
- 按级别创建目录并复制对应PDF文件
- 保持原始文件名和文件格式

## 注意事项

- 确保PDF文件名中包含明确的级别信息，例如 "Python一级"、"C++二级" 等
- 处理脚本会自动识别文件名中的级别信息，无需手动干预
- 处理完成后，原始PDF文件仍保留在 `gesp_pdfs/` 目录中

## 联系方式

如果有任何问题或建议，欢迎联系项目维护者。

---

**项目更新时间：2026-04-13**