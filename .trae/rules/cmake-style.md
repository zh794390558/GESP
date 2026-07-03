---
description: "工程化通用规则，适配构建、测试、部署相关文件"
globs: ["CMakeLists.txt", "Makefile", "scripts/**/*", "tests/**/*"]
---
## 工程化规范
1. C++ 构建统一使用 CMake，禁止手写复杂 Makefile
2. Python 统一使用虚拟环境（venv/uv），隔离依赖
3. 项目目录结构标准化：
   - src/：核心源码
   - include/：C++ 头文件
   - tests/：单元/集成测试
   - scripts/：脚本工具
   - docs/：项目文档
4. 错误处理：统一错误码/异常体系，禁止静默失败
5. 日志规范：区分等级（DEBUG/INFO/WARN/ERROR），记录关键上下文