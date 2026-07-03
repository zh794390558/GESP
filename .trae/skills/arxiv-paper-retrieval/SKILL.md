---
name: arxiv-paper-retrieval
description: |
  提供 arxiv 论文获取服务，包括但不限于热点论文检索、优质潜力论文挖掘、特定领域论文筛选、论文元数据提取、论文链接生成、定期学术追踪，
  当用户提出 arxiv 论文获取、论文检索、论文推荐、学术文献查询、学术动态追踪相关需求时触发，
  可根据用户需求的领域、关键词、时间范围、排序方式，提供精准的论文检索结果并附带可点击的官方链接，
  支持利用现有工具（如 Terminal、File system、Preview）进行检索执行、结果存储和可视化展示。
allowed-tools: [HTTPRequest, DataParser, Search, URLBuilder, Docker, DuckDuckGo Search Server, File system, Terminal, Preview]
author: arxiv-paper-retrieval-skill@example.com
version: 1.0.0
---

# arxiv 论文获取Skill
## Overview
本技能专注于为各类学术研究场景（科研选题、文献综述、技术调研、学术追踪等）提供全流程 arxiv 论文获取支持，
核心价值是快速、精准地检索符合用户需求的 arxiv 论文，区分热点论文与优质潜力论文，提供完整的论文信息与可点击的官方链接，
适配不同学科领域（计算机科学、物理学、数学、生物学等）、不同时间范围（最新论文、历史经典论文）的论文获取需求，
兼顾检索效率与结果质量，确保提供的论文信息准确、链接有效，
支持利用 Terminal 执行检索命令、File system 存储检索结果、Preview 展示论文信息，提供端到端的学术资源获取体验。

## When to Use
✅ 适用场景：
1.  科研选题阶段，需要了解特定领域的最新研究动态和热点方向；
2.  文献综述撰写，需要系统性收集某一主题的相关论文；
3.  技术调研，需要获取特定技术领域的前沿论文和经典之作；
4.  学术追踪，需要定期获取某一领域或特定作者的最新论文；
5.  跨学科研究，需要从不同领域获取相关论文进行交叉分析；
6.  论文写作参考，需要查找特定方法、算法或实验的相关论文。

❌ 不适用场景：
1.  改变原有业务逻辑的代码修改（本技能仅专注于论文获取，不涉及代码修改）；
2.  非 arxiv 来源的论文获取（仅支持 arxiv 平台的论文检索与获取）；
3.  论文内容的深度分析或解读（仅提供论文基本信息与链接，不进行内容分析）；
4.  非学术论文的获取（仅专注于 arxiv 平台的学术论文）；
5.  无明确检索需求或未提供具体领域/关键词的模糊需求。

## Workflow（必须按序执行）
1.  需求拆解：询问用户获取核心信息（研究领域、关键词、时间范围、排序方式、论文类型偏好、预期结果数量）；
2.  检索策略制定：根据用户需求，确定检索关键词组合、时间筛选条件、排序规则，选择合适的检索工具；
3.  论文检索执行：利用 Terminal 执行 arxiv API 调用或官方接口查询，获取初步检索结果；
4.  结果筛选与分类：对检索结果进行筛选，区分热点论文与优质潜力论文，按相关性排序；
5.  信息整合与格式化：提取论文标题、作者、摘要、发布日期、分类、PDF 链接等信息，使用 File system 存储结构化数据；
6.  结果呈现与验证：利用 Preview 向用户展示检索结果，确保所有论文链接可点击且与论文信息一致，提供后续检索建议。

## Examples
### 示例1：输入（热点论文检索需求）
"我需要获取最近一个月内计算机视觉领域的热点论文，重点关注目标检测和图像分割方向，按引用量排序。"

### 示例1：输出（核心检索方案）
#### 一、检索目标
1.  时间范围：最近一个月内发布的论文；
2.  领域：计算机视觉（Computer Vision）；
3.  子方向：目标检测（Object Detection）、图像分割（Image Segmentation）；
4.  排序方式：按引用量从高到低排序；
5.  结果数量：前 10 篇最相关论文。

#### 二、检索策略
1.  关键词组合：使用 "computer vision" AND ("object detection" OR "image segmentation")；
2.  时间筛选：设置时间范围为最近 30 天；
3.  排序规则：按引用量（citations）降序排列；
4.  工具选择：使用 Terminal 执行 arxiv API 调用。

#### 三、具体执行步骤
1.  构建检索请求：在 Terminal 中使用 curl 命令调用 arxiv API，设置查询参数：
   ```bash
   curl -X GET "http://export.arxiv.org/api/query?search_query=cat:cs.CV+AND+(object+detection+OR+image+segmentation)&sortBy=cited&sortOrder=descending&start=0&max_results=10&timeframe=30days"
   ```
2.  执行检索：运行上述命令，获取原始 JSON 格式的检索结果；
3.  结果处理：使用 Python 脚本解析 JSON 数据，提取论文元数据：
   ```python
   import json
   import requests
   
   response = requests.get("http://export.arxiv.org/api/query?search_query=cat:cs.CV+AND+(object+detection+OR+image+segmentation)&sortBy=cited&sortOrder=descending&start=0&max_results=10&timeframe=30days")
   # 解析响应数据，提取论文信息
   ```
4.  热点识别：根据引用量、发布时间、领域相关性，识别热点论文；
5.  信息整合：将检索结果存储到 File system 中的 JSON 文件，确保链接可点击；
6.  结果展示：使用 Preview 向用户展示格式化的检索结果。

#### 四、验证与工具
1.  工具使用：
   - Terminal：执行 API 调用和数据处理脚本；
   - File system：存储检索结果和中间数据；
   - Preview：展示格式化的论文信息和链接。
2.  链接验证：检查所有 PDF 链接是否可正常访问，确保与论文标题一致；
3.  结果验证：确认检索结果符合用户指定的时间范围和领域方向。

### 示例2：输入（优质潜力论文挖掘需求）
"我想了解量子计算领域的优质潜力论文，不一定是最新的，但要有长期学术价值，重点关注量子算法和量子纠错方向。"

### 示例2：输出（核心检索方案）
#### 一、检索目标
1.  领域：量子计算（Quantum Computing）；
2.  子方向：量子算法（Quantum Algorithms）、量子纠错（Quantum Error Correction）；
3.  论文类型：优质潜力论文，侧重长期学术价值；
4.  时间范围：近 2 年内发布的论文；
5.  结果数量：前 15 篇最具潜力的论文。

#### 二、检索策略
1.  关键词组合：使用 "quantum computing" AND ("quantum algorithms" OR "quantum error correction")；
2.  时间筛选：设置时间范围为近 2 年；
3.  排序方式：按相关性和引用趋势综合排序；
4.  工具选择：使用 Terminal 执行高级检索，结合 File system 存储中间结果。

#### 三、具体执行步骤
1.  初步检索：在 Terminal 中使用 Python 脚本调用 arxiv API，获取符合条件的论文：
   ```python
   import arxiv
   
   # 构建查询
   search_query = "quantum computing AND (quantum algorithms OR quantum error correction)"
   client = arxiv.Search(
       query=search_query,
       max_results=50,
       sort_by=arxiv.SortCriterion.Relevance
   )
   
   # 获取论文
   papers = list(client.results())
   ```
2.  潜力评估：使用 Python 脚本分析论文的引用趋势、作者背景、研究机构、内容创新性；
3.  分类整理：将筛选后的论文按主题分类，标注每篇论文的核心贡献和潜在价值，存储到 File system 中的结构化文件；
4.  信息整合：提取论文完整信息，生成可点击的官方链接；
5.  结果呈现：按潜力值排序，使用 Preview 向用户展示详细的论文信息和链接。

#### 四、验证与工具
1.  工具使用：
   - Terminal：执行高级检索脚本和数据分析；
   - File system：存储原始数据、分析结果和最终报告；
   - Preview：展示格式化的论文信息和链接。
2.  质量验证：确保推荐的论文具有原创性和学术价值，通过引用分析验证其潜力；
3.  链接验证：确认所有论文链接指向正确的 arxiv 页面。

## 关键规范与注意事项
1.  重构核心原则：**不改变原有业务逻辑**，本技能仅专注于论文获取与信息整合，不涉及内容修改或分析；
2.  数据来源权威：所有论文信息均来自 arxiv 官方平台，确保数据真实性和准确性；
3.  链接有效性：所有提供的论文链接必须可点击且指向正确的 arxiv 官方页面，定期验证链接有效性；
4.  结果相关性：根据用户需求精准检索，确保结果与用户指定的领域、关键词、时间范围高度相关；
5.  信息完整性：提供论文的完整元数据，包括标题、作者、摘要、发布日期、分类、PDF 链接等；
6.  工具使用规范：
   - Terminal：仅用于执行检索命令和数据分析，不执行危险操作；
   - File system：合理存储检索结果，避免占用过多存储空间；
   - Preview：确保展示的论文信息格式清晰，链接可点击；
7.  结果质量控制：对检索结果进行筛选和分类，区分热点论文与优质潜力论文，提供有价值的学术信息；
8.  速率限制遵守：遵守 arxiv API 的调用速率限制，避免过度请求导致服务被封禁。