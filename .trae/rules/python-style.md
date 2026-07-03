---
description: "Python 编码规范，适配所有 .py 文件"
globs: ["**/*.py", "src/**/*.py", "tests/**/*.py"]
---
## Python 强制规则
### 基础规范
- 严格遵循 [PEP 8] 编码标准
- 缩进使用 4 个空格，禁止使用 Tab
- 文件编码统一为 UTF-8，行尾为 LF
- 最大行宽 120 字符，超出自动换行

### 命名规范
- 变量/函数/模块：小驼峰 | 下划线命名（user_info、get_data）
- 类名：大驼峰（UserManager）
- 常量：全大写+下划线（MAX_RETRY_COUNT）
- 私有成员：前缀单下划线（`_internal_method`）
- type hint: 所有的函数、类、变量都需要写 type hint.

### 代码质量
- **强制使用类型注解**（typing 模块：List, Dict, Optional, Union 等）
- 禁止使用裸 `except`，必须捕获具体异常类型
- 日志使用标准 `logging` 模块，禁止 `print` 用于生产环境
- 优先使用内置数据结构与标准库，减少第三方依赖
- 依赖管理使用 `requirements.txt` / `pyproject.toml`，固定版本号
- 单元测试使用 `pytest`，测试文件以 `test_` 开头

### 最佳实践
- 使用上下文管理器（with）管理文件、网络、进程资源
- 大型项目使用包结构管理代码，禁止扁平式文件堆积
- 配置文件使用 yaml/json，不硬编码在代码中
