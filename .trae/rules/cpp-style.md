---
description: "C++ 编码规范，适配所有 .cpp/.h/.hpp 文件"
globs: ["**/*.cpp", "**/*.h", "**/*.hpp", "src/**/*.cc"]
---
## C++ 强制规则
### 基础规范
- 统一使用 **C++17** 及以上标准编译
- 缩进使用 4 个空格，大括号风格统一（K&R 风格）
- 头文件必须添加保护：`#pragma once`（优先）或 头文件保护宏
- 禁止使用 `using namespace std;` 在头文件中

### 命名规范
- 函数/变量：小驼峰 | 下划线（calculate_sum、node_count）
- 类/结构体/枚举：大驼峰（DataProcessor、NodeConfig）
- 常量/宏：全大写+下划线（BUFFER_SIZE）
- 命名空间：小写，短且语义化（namespace utils {}）

### 代码安全与性能
- 遵循 **RAII** 原则，禁止手动管理内存（优先使用智能指针：unique_ptr/shared_ptr）
- 禁止使用裸指针传递所有权，仅用于非持有引用
- 强制使用 `const` 正确性：只读参数/函数添加 const 修饰
- 禁止使用 C 风格强制类型转换，使用 static_cast/dynamic_cast 等
- 编译开启最高警告等级（-Wall -Wextra -Werror），消除所有警告

### 最佳实践
- 声明与实现分离：头文件放声明，源文件放实现
- 优先使用 STL 容器，禁止重复造轮子
- 复杂逻辑拆分函数/类，保持函数代码行数＜50
- 禁止使用全局变量，必要时使用单例/静态成员封装