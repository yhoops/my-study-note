<p align="center">
  <h1 align="center">My Study Note</h1>
  <p align="center">个人技术栈沉淀 · Python 学习知识库</p>
  <p align="center">
    <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" alt="Markdown"/>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/NumPy-2.5-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
    <img src="https://img.shields.io/badge/pandas-3.0-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"/>
    <img src="https://img.shields.io/badge/Matplotlib-3.11-11557C?style=flat-square&logo=python&logoColor=white" alt="Matplotlib"/>
    <img src="https://img.shields.io/badge/seaborn-0.13-4C72B0?style=flat-square" alt="seaborn"/>
    <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
    <img src="https://img.shields.io/badge/Socket%20%26%20Threading-4B8BBE?style=flat-square" alt="Socket & Threading"/>
    <img src="https://img.shields.io/github/last-commit/yhoops/my-study-note?style=flat-square&label=Last%20Commit" alt="Last Commit"/>
    <img src="https://img.shields.io/github/repo-size/yhoops/my-study-note?style=flat-square&label=Repo%20Size" alt="Repo Size"/>
  </p>
</p>

> 一个以 **Python** 为核心的渐进式学习仓库：从面向对象、函数式编程、网络与并发编程，到数据结构算法、数据分析与科学计算，沉淀**随堂笔记（图文）**与**可运行示例代码**。
>
> 仓库分为两条主线：`Python/` 记录语言本体与计算机基础，`Python数据分析/` 记录 NumPy / pandas 数据分析栈。点击下方目录快速定位。

---

## 快速导航

| 板块 | 内容 | 入口 |
|------|------|------|
| [学习路线总览](#学习路线总览) | Day 1–7 的主题与进度地图 | — |
| [Python 基础与进阶](#python-基础与进阶) | 面向对象、函数式、网络、并发、数据结构与算法 | [`Python/`](./Python/) |
| [Python 数据分析](#python-数据分析) | NumPy、pandas、Matplotlib 与实战 Notebook | [`Python数据分析/`](./Python数据分析/) |
| [开发环境与工具链](#开发环境与工具链) | venv / conda 虚拟环境管理 | [`虚拟环境venv.conda/`](./虚拟环境venv.conda/) |
| [环境复现](#环境复现) | 一键还原数据分析环境 | [`env.yml`](./Python数据分析/env.yml) |
| [仓库统计](#仓库统计) | 文件与主题数量 | — |
| [目录结构](#目录结构) | 完整目录树 | — |

---

## 学习路线总览

笔记（`.md`，含图文讲解）与代码（`.py`，可直接运行）分开存放：笔记位于 `Python/Day*/`，配套代码位于 `Python/Code/day*/`。

| 阶段 | 主题 | 随堂笔记 | 配套代码 |
|:----:|------|----------|----------|
| Day 1 | 面向对象基础：类与对象、魔法方法、继承 | [Day01_随堂笔记](./Python/Day1-2/Day01_随堂笔记.md) | 内嵌于笔记 |
| Day 2 | 面向对象进阶：封装、多态、抽象类、学生管理系统 | [Day02_随堂笔记](./Python/Day1-2/Day02_随堂笔记.md) | 内嵌于笔记 |
| Day 3 | 函数式编程：闭包、装饰器、深浅拷贝 | [day03_随堂笔记](./Python/Day3%20Day5/day03_随堂笔记.md) | [`Code/day3/`](./Python/Code/day3/) · 12 个示例 |
| Day 4 | 网络编程与多进程多线程入门 | [Day04_随堂笔记](./Python/Day4/Day04_随堂笔记.md) | [`Code/day04/`](./Python/Code/day04/) · 17 个示例 |
| Day 5 | 线程同步、迭代器与生成器、正则表达式 | [Day05_随堂笔记](./Python/Day3%20Day5/Day05_随堂笔记.md) | [`Code/day05/`](./Python/Code/day05/) · 19 个示例 |
| Day 6 | 数据结构：顺序表与链表 | [Day06_随堂笔记](./Python/Day6/Day06_随堂笔记.md) | 内嵌于笔记 |
| Day 7 | 算法：三大排序、二分查找、二叉树 | [Day07_随堂笔记](./Python/Day7/Day07_随堂笔记.md) | 内嵌于笔记 |
| 专题 | 数据分析：NumPy / pandas / Matplotlib | [`Python数据分析/note/`](./Python数据分析/note/) | [`Python数据分析/code/`](./Python数据分析/code/) · 6 个 Notebook |
| 专题 | 工程化：虚拟环境与依赖隔离 | [虚拟环境 note](./虚拟环境venv.conda/note.md) | — |

---

## Python 基础与进阶

**位置**：[`./Python/`](./Python/)　**形式**：按天组织的图文随堂笔记（`.md` + `assets/` 截图）+ 可运行示例代码（`.py`）

### Day 1–2 · 面向对象编程

**笔记位置**：[`Python/Day1-2/`](./Python/Day1-2/)

<details open>
<summary><b>Day 01 · 类与对象、魔法方法、继承</b> —— <a href="./Python/Day1-2/Day01_随堂笔记.md">打开笔记</a></summary>

- 面向对象与面向过程的区别、面向对象三大特征概览
- 入门案例：汽车类、手机类
- `self` 关键字的作用与传参机制
- 类外 / 类内 获取与设置对象属性
- 魔法方法：`__init__`（初始化）、`__str__`（对象打印）、`__del__`（对象销毁）
- 综合案例：减肥案例、烤地瓜案例（属性状态流转 + 调料列表）
- 定义类的三种书写格式
- 继承入门、单继承演示、多继承演示与 **MRO 机制**

`#面向对象` `#类与对象` `#self` `#魔法方法` `#继承` `#MRO`
</details>

<details open>
<summary><b>Day 02 · 封装、多态、抽象类与项目实战</b> —— <a href="./Python/Day1-2/Day02_随堂笔记.md">打开笔记</a></summary>

- 子类重写父类功能、子类访问父类功能（`super()`）
- 多层继承（师傅 → 徒弟 → 徒孙 的煎饼果子案例贯穿全篇）
- 封装入门：私有成员与访问控制
- 多态入门 + 多态案例：**构建英雄机对战平台**
- 抽象类案例：空调类规范子类实现
- 对象属性 vs 类属性、类方法与静态方法
- **学生管理系统**（完整项目）：学生类 → 框架搭建 → 入口文件 → 功能实现 → 学生信息的保存与加载
- 扩展：`__dict__` 属性，实现「对象 ⇄ 字典」互转

`#封装` `#多态` `#抽象类` `#类方法` `#静态方法` `#项目实战` `#__dict__`
</details>

### Day 3 · 函数式编程

**笔记**：[day03_随堂笔记](./Python/Day3%20Day5/day03_随堂笔记.md)　**代码**：[`Python/Code/day3/`](./Python/Code/day3/)

笔记大纲：闭包背景介绍 → 闭包入门（函数名即对象）→ `nonlocal` 关键字 → 装饰器入门 → 装饰器案例（登录 + 验证码，剖析多装饰器的**入栈出栈顺序**与语法糖）→ 浅拷贝与深拷贝对比实验

<details>
<summary>展开 12 个代码示例</summary>

- [01 - 闭包背景介绍](./Python/Code/day3/01_闭包背景介绍.py)　`#闭包` `#作用域`
- [02 - 闭包入门](./Python/Code/day3/02_闭包入门.py)　`#闭包`
- [03 - nonlocal 关键字介绍](./Python/Code/day3/03-nonlocal关键字介绍.py)　`#nonlocal`
- [04 - 装饰器入门](./Python/Code/day3/04_装饰器入门.py)　`#装饰器`
- [05 - 装饰器装饰：无参无返回的原函数](./Python/Code/day3/05_装饰器装饰_无参无返回的原函数.py)　`#装饰器`
- [06 - 装饰器装饰：有参无返回的原函数](./Python/Code/day3/06_装饰器装饰_有参无返回的原函数.py)　`#装饰器`
- [07 - 装饰器装饰：无参有返回的原函数](./Python/Code/day3/07_装饰器装饰_无参有返回的原函数.py)　`#装饰器`
- [08 - 装饰器装饰：有参有返回的原函数](./Python/Code/day3/08_装饰器装饰_有参有返回的原函数.py)　`#装饰器`
- [09 - 装饰器装饰：可变参数](./Python/Code/day3/09_装饰器装饰_可变参数.py)　`#装饰器` `#*args`
- [10 - 多个装饰器装饰一个函数](./Python/Code/day3/10_多个装饰器装饰1个函数.py)　`#装饰器` `#执行顺序`
- [11 - 一个装饰器装饰多个函数](./Python/Code/day3/11_1个装饰器装饰多个函数.py)　`#装饰器`
- [13 - 深浅拷贝·面试题](./Python/Code/day3/13_深浅拷贝_面试题.py)　`#深拷贝` `#浅拷贝`
</details>

### Day 4 · 网络编程与进程线程

**笔记**：[Day04_随堂笔记](./Python/Day4/Day04_随堂笔记.md)　**代码**：[`Python/Code/day04/`](./Python/Code/day04/)

笔记大纲：网络编程介绍 → 创建 Socket 对象（地址族 / Socket 类型）→ 网编案例「一句话交互」（含**端口号重用** `SO_REUSEADDR`）→ 模拟多任务服务器端 → 编解码扩展 → 文件上传案例（单任务 / 模拟多任务版）→ 多任务简介与单任务演示 → 多进程入门 → 获取进程编号 → 进程数据隔离 → 守护进程 → 线程入门

<details>
<summary>展开 17 个代码示例 + 配套数据</summary>

- [01 - 创建 Socket 对象](./Python/Code/day04/01_创建socket对象.py)　`#socket`
- [02 - 网编案例·服务器端](./Python/Code/day04/02_网编案例_服务器端.py)　`#TCP`
- [03 - 网编案例·客户端](./Python/Code/day04/03_网编案例_客户端.py)　`#TCP`
- [04 - 演示编解码](./Python/Code/day04/04_演示编解码.py)　`#encode` `#decode`
- [05 - 网编案例·模拟多任务版服务器端](./Python/Code/day04/05_网编案例_模拟多任务版服务器端.py)　`#多任务`
- [06 - 网编案例·文件上传·服务器端](./Python/Code/day04/06_网编案例_文件上传_服务器端.py)　`#文件传输`
- [07 - 网编案例·文件上传·客户端](./Python/Code/day04/07_网编案例_文件上传_客户端代码.py)　`#文件传输`
- [08 - 网编案例·文件上传·服务器端模拟多任务版](./Python/Code/day04/08_网编案例_文件上传_服务器端模拟多任务版.py)　`#文件传输`
- [09 - 演示单任务](./Python/Code/day04/09_演示单任务.py)　`#串行`
- [10 - 演示多进程](./Python/Code/day04/10_演示多进程.py)　`#multiprocessing`
- [11 - 带参数的多进程](./Python/Code/day04/11_带参数的多进程.py)　`#进程参数`
- [12 - 获取进程的 pid](./Python/Code/day04/12_获取进程的pid.py)　`#pid`
- [13 - 进程特点之数据隔离](./Python/Code/day04/13_进程特点之数据隔离.py)　`#进程隔离`
- [14 - 进程特点之主进程等待子进程](./Python/Code/day04/14_进程特点之主进程等待子进程结束再结束.py)　`#进程同步`
- [15 - 线程入门案例](./Python/Code/day04/15_线程入门案例.py)　`#threading`
- [16 - 线程入门·带参数的线程](./Python/Code/day04/16_线程入门案例带参数的线程.py)　`#threading`
- [17 - 数字排列组合](./Python/Code/day04/17_数字排列组合.py)　`#itertools`
- 配套数据：[my.txt](./Python/Code/day04/data/my.txt) · [test_data.txt](./Python/Code/day04/data/test_data.txt)
</details>

### Day 5 · 并发进阶与正则表达式

**笔记**：[Day05_随堂笔记](./Python/Day3%20Day5/Day05_随堂笔记.md)　**代码**：[`Python/Code/day05/`](./Python/Code/day05/)

笔记大纲：多线程特点（随机性 / 守护线程 / 数据共享 / 互斥锁）→ **进程与线程对比** → 迭代器入门（手写 `range`）→ 生成器介绍 → `property` 属性 → 正则表达式入门（单字符、多字符量词、开头结尾锚点、分组与反向引用、`re.sub` 替换）→ 实战校验（邮箱 / QQ 号 / HTML 单级与多级标签）

<details>
<summary>展开 19 个代码示例 + 配套数据</summary>

- [01 - 多线程的执行具有随机性](./Python/Code/day05/01_多线程的执行具有随机性.py)　`#线程调度`
- [02 - 多线程特点·守护线程](./Python/Code/day05/02_多线程特点_守护线程.py)　`#daemon`
- [03 - 多线程特点·数据共享](./Python/Code/day05/03_多线程特点_数据共享.py)　`#全局变量`
- [04 - 多线程特点·共享全局数据错误问题](./Python/Code/day05/04_多线程特点_共享全局数据出现错误问题.py)　`#竞态条件`
- [05 - 多线程操作·互斥锁](./Python/Code/day05/05_多线程操作_互斥锁.py)　`#Lock` `#同步`
- [06 - 迭代器](./Python/Code/day05/06_迭代器.py)　`#iter` `#next`
- [07 - 生成器入门·推导式写法](./Python/Code/day05/07_生成器入门_推导式写法.py)　`#生成器`
- [08 - 生成器入门·yield 方式](./Python/Code/day05/08_生成器入门_yield方式.py)　`#yield`
- [09 - 生成器生成批次歌词](./Python/Code/day05/09_example_生成器生成批次歌词.py)　`#实战`
- [10 - property 装饰器用法](./Python/Code/day05/10_property_装饰器用法.py)　`#property`
- [11 - property 类属性用法](./Python/Code/day05/11_property_类属性用法.py)　`#property`
- [12 - 正则表达式·校验单个字符](./Python/Code/day05/12_正则表达式_校验单个字符.py)　`#re`
- [13 - 正则替换](./Python/Code/day05/13_正则替换.py)　`#sub`
- [14 - 正则表达式·校验多个字符](./Python/Code/day05/14_正则表达式_校验多个字符.py)　`#量词`
- [15 - 正则表达式·校验开头和结尾](./Python/Code/day05/15_正则表达式_校验开头和结尾.py)　`#锚点`
- [16 - 正则表达式·校验分组](./Python/Code/day05/16_正则表达式_校验分组.py)　`#分组`
- [17 - 校验邮箱](./Python/Code/day05/17_example_校验邮箱.py)　`#实战`
- [18 - 校验 QQ 号](./Python/Code/day05/18_example_校验QQ号.py)　`#实战`
- [19 - 校验 HTML 标签](./Python/Code/day05/19_example_校验html标签.py)　`#实战`
- 配套数据：[jay_lyrics.txt](./Python/Code/day05/data/jay_lyrics.txt)
</details>

### Day 6 · 数据结构

**笔记**：[Day06_随堂笔记](./Python/Day6/Day06_随堂笔记.md)

- 数据结构与算法简介、数据结构的分类
- 线性结构存储数据的方式、**顺序表**的存储方式
- 线性结构之**链表**介绍（与顺序表的取舍对比）
- 自定义代码模拟链表：`SingleNode` 节点类 + `SingleLinkedList` 单链表类

`#数据结构` `#顺序表` `#单链表` `#手写实现`

### Day 7 · 算法

**笔记**：[Day07_随堂笔记](./Python/Day7/Day07_随堂笔记.md)

- **冒泡排序**：思路推导与代码实现
- **选择排序**：思路推导与代码实现
- **插入排序**：思路推导与代码实现
- **二分查找**：递归版 `binary_search_recursion()` + 非递归版 `binary_search()`
- 自定义代码模拟**二叉树**

`#排序算法` `#二分查找` `#二叉树` `#递归`

---

## Python 数据分析

**位置**：[`./Python数据分析/`](./Python数据分析/)　**形式**：结构化长篇笔记（`note/`）+ Jupyter 实践（`code/`）+ 真实数据集（`code/data/`）

### 结构化笔记

| 笔记 | 状态 | 核心大纲 |
|------|:----:|----------|
| [Numpy 相关内容](./Python数据分析/note/Numpy相关内容.md) | ✅ 完成 | ① 介绍 ② `ndarray`（多维 / 同质 / 属性 / 创建 / 数据类型 / 索引切片 / 运算与**广播机制** / 矩阵乘法 `@`）③ 常用函数：基本数学函数、统计函数（均值、中位数、方差标准差、`argmax`/`argmin`、**分位数计算原理**）、比较函数（`np.where` 嵌套、`np.select`）、去重、拼接与分割、`reshape`、排序 ④ **缺失知识点清单**（视图与内存机制、高级索引、`np.linalg`、傅里叶变换、`np.random`、文件 I/O、字符串数组、性能与向量化） |
| [Pandas 相关内容](./Python数据分析/note/Pandas相关内容.md) | ✅ 完成 | ① 简介 ② **Series**（属性、创建、显式/隐式索引、`at`/`iat`、布尔索引、去重与排序、**时间序列**重采样与滑动窗口、实战案例）③ **DataFrame**（属性、创建、数据概览）④ 数据导入导出（含嵌套 JSON 的稳妥读法）⑤ **数据清洗**（缺失值识别/剔除/填充、重复值、类型转换与 `map` 映射）⑥ **数据变形与重构**（`melt`/`pivot` 宽长表互转、字符串分列、`pd.cut` 数据分箱、索引与列名修改）⑦ **时间数据处理**（`Timestamp`、`dt` 访问器、`parse_dates`、时间切片、`Timedelta`、`date_range`、`resample`）⑧ **分组聚合**（`groupby`、多字段分组、`agg` 多指标聚合）⑨ 综合实战 |
| [Matplotlib 学习笔记](./Python数据分析/note/Matlplotlib学习笔记.md) | ✅ 完成 | ① 可视化三原则：**信**（表达准确，避免误导）、**达**（高效传达有效信息）、**雅**（布局与配色美观）② 常见图表与箱型图要素 ③ 可视化基础（matplotlib / seaborn / pandas plot 工具对比）④ **Matplotlib 基础绘图**（绘图通用流程与中文字体配置、画布与装饰函数速查、折线图 `plot`、柱状图 `bar`、条形图 `barh`、饼图 / 环形图 / 爆炸式饼图 `pie`、散点图 `scatter` 与回归参考线、箱线图 `boxplot`、多子图 `subplot`、**图表类型选择表**）⑤ 分析案例：气温趋势与降水直方图（`weather.csv`）⑥ **Seaborn 常用统计图**（`histplot` / `kdeplot` / `countplot` 单变量分布，`scatterplot` / `jointplot` 蜂窝图 / 二维 `kdeplot` 双变量关系，`barplot` 分组聚合，`pairplot` 成对关系）⑦ **项目实战：房地产市场洞察**（清洗与特征构造 → 相关性热力图 → 房价分布 → 朝向溢价箱线图）—— 全篇 25 张图均由配套 Notebook 代码实际渲染 |

### Jupyter 实践

| Notebook | 说明 | 关键词 |
|----------|------|--------|
| [Numpy 学习](./Python数据分析/code/Numpy学习.ipynb) | 与 NumPy 笔记配套的随堂练习：`ndarray` 特性、属性、创建、数据类型、索引切片、运算、常用函数 | `#NumPy` `#ndarray` `#广播` |
| [Pandas-Series 学习](./Python数据分析/code/Pandas-Series学习.ipynb) | Series 的创建、索引访问、属性与常用方法练习 | `#pandas` `#Series` |
| [Pandas-DataFrame 学习](./Python数据分析/code/Pandas-DataFrame学习.ipynb) | DataFrame 的多种创建方式与数据概览练习 | `#pandas` `#DataFrame` |
| [数据分析](./Python数据分析/code/数据分析.ipynb) | **综合主线 Notebook**：数据导入 → 清洗 → 变形分箱 → 时间处理 → 分组聚合，并落地两个完整案例 | `#实战` `#EDA` |
| [Matplotlib 学习](./Python数据分析/code/Matplotlib学习.ipynb) | 五类基础图表（折线 / 条形 / 饼 / 散点 / 箱线）+ 多子图 + 天气分析案例 + seaborn 统计图 | `#Matplotlib` `#seaborn` `#可视化` |
| [项目实战·房地产市场分析](./Python数据分析/code/项目实战-房地产市场分析.ipynb) | 10 万条二手房数据：清洗 → 特征构造 → 按问题编号（A1/A2/A6）分析并可视化 | `#实战` `#数据清洗` `#热力图` |

**三个完整实战案例**：

1. **企鹅数据分析**（`penguins.csv`，位于 [数据分析.ipynb](./Python数据分析/code/数据分析.ipynb)）—— 导入 → 缺失值处理 → `category` 特征构造 → 体重分箱（低/中/高）→ 按性别与岛屿分组统计体重均值与样本数
2. **睡眠健康数据分析**（`sleep.csv`，位于 [数据分析.ipynb](./Python数据分析/code/数据分析.ipynb)）—— 缺失过多的 `sleep_disorder` 直接删列 → 特征构造 → 年龄段 + BMI 分组，观察睡眠时长、睡眠质量与压力水平的关系
3. **房地产市场洞察与价值评估**（`house_sales.csv`，位于 [项目实战-房地产市场分析.ipynb](./Python数据分析/code/项目实战-房地产市场分析.ipynb)）—— 106118 条原始记录经去重（29416 条重复）、单位剥离与 IQR 异常值处理后保留 26135 条 → 构造地区 / 楼层类型 / 楼龄 / 价格分箱等特征 → 三个分析结论：**单价对总价影响最大**（相关系数 0.74，面积 0.45，楼龄仅 0.09）、**房价右偏**（均值 117 万 > 中位数 103 万）、**南北向仅比南向贵约 4.3%**（小样本朝向的均值不可靠）

> 前两个案例的笔记同步收录于 Pandas 笔记第 9 章；第三个案例与全部可视化图表同步收录于 Matplotlib 笔记第 5—7 章。

### 配套数据集

**位置**：[`Python数据分析/code/data/`](./Python数据分析/code/data/)

| 数据集 | 用途 |
|--------|------|
| `penguins.csv` | 企鹅综合案例（分箱、分组聚合）、seaborn 统计图示例 |
| `sleep.csv` | 睡眠健康综合案例（类型转换、分箱） |
| `weather.csv` / `weather_withna.csv` | 时间序列处理、`resample` 重采样、缺失值填充、气温趋势与降水直方图 |
| `employees.csv` | `groupby` 多字段分组与 `agg` 多指标聚合 |
| `house_sales.csv` | **房地产实战案例**（10 万条二手房数据的清洗、特征构造与可视化） |
| `new.csv` | 数据导入导出练习 |
| `data1.json` / `products.json` / `test.json` | JSON 读取与嵌套结构处理 |
| `output/employees_tail.csv` | 数据导出练习产物 |

---

## 开发环境与工具链

**位置**：[`./虚拟环境venv.conda/`](./虚拟环境venv.conda/)

| 笔记 | 大纲 | 关键词 |
|------|------|--------|
| [Python 虚拟环境——venv 与 conda](./虚拟环境venv.conda/note.md) | 为什么需要虚拟环境 → **venv**（创建 / 激活 / 退出 / 本质剖析）→ 虚拟环境的封装与共享（`requirements.txt`）→ **Conda**（跨语言兼容性问题、基本命令、发行版与生态、**Mamba** 加速方案） | `#venv` `#conda` `#pip` `#环境隔离` `#mamba` |

> 笔记内嵌截图存放于 [`虚拟环境venv.conda/assets/`](./虚拟环境venv.conda/assets/)；虚拟环境本体 `code/myvenv/` 已被 `.gitignore` 排除。

### 环境复现

数据分析板块的 conda 环境已导出为 [`Python数据分析/env.yml`](./Python数据分析/env.yml)，核心依赖：`python 3.14.6` · `numpy 2.5.1` · `pandas 3.0.5` · `matplotlib 3.11.1`。

> `env.yml` 为 seaborn 引入之前的快照，尚未包含 `seaborn`（实际使用 0.13.2）。用方式一还原后需补装：`conda install seaborn -c conda-forge`。

```bash
# 方式一：从 env.yml 完整还原（含 build 号，跨平台可能失败）
conda env create -f Python数据分析/env.yml -n study-note

# 方式二：手动创建最小环境（推荐，跨平台稳妥）
conda create -n study-note python=3.14 numpy pandas matplotlib seaborn jupyter -c conda-forge
conda activate study-note
```

> **中文显示**：绘图前需配置中文字体，否则中文标题与标签会显示为方框（Windows 用 `SimHei`，macOS 用 `AppleGothic`），并设置 `rcParams['axes.unicode_minus'] = False` 解决负号乱码，详见 Matplotlib 笔记 4.1。

`Python/` 下的示例代码仅依赖标准库（`socket`、`multiprocessing`、`threading`、`re`、`copy`、`itertools`），无需额外安装即可运行：

```bash
python Python/Code/day05/05_多线程操作_互斥锁.py
```

> 网络编程示例需**先启动服务器端、再启动客户端**（如 `02_网编案例_服务器端.py` → `03_网编案例_客户端.py`），建议开两个终端。

---

## 仓库统计

| 指标 | 数值 |
|------|:----:|
| 随堂笔记 / 结构化笔记（Markdown） | 11 |
| Jupyter Notebook | 6 |
| Python 示例代码（`.py`） | 48 |
| 笔记配图（PNG） | 68 |
| 数据集与素材（CSV / JSON / TXT） | 14 |
| 覆盖天数 | Day 1 – Day 7 + 2 个专题 |
| 覆盖主题 | 面向对象（封装 / 继承 / 多态 / 抽象类 / MRO）· 魔法方法 · 闭包 · 装饰器 · 深浅拷贝 · Socket 网络编程 · 多进程 · 多线程 · 互斥锁 · 迭代器 · 生成器 · property · 正则表达式 · 顺序表 · 单链表 · 排序算法 · 二分查找 · 二叉树 · NumPy · pandas · Matplotlib · seaborn · 数据可视化 · 虚拟环境 |

---

## 目录结构

```
my-study-note/
├── Python/                              # 主线一：Python 语言与计算机基础
│   ├── Code/                            #   可运行示例代码
│   │   ├── day3/                        #     函数式编程：闭包、装饰器、深浅拷贝（12）
│   │   ├── day04/                       #     网络编程、多进程、多线程（17 + data/）
│   │   └── day05/                       #     线程同步、生成器、正则（19 + data/）
│   ├── Day1-2/                          #   Day 01–02 随堂笔记：面向对象
│   │   ├── Day01_随堂笔记.md             #     类与对象、魔法方法、继承
│   │   ├── Day02_随堂笔记.md             #     封装、多态、抽象类、学生管理系统
│   │   └── assets/                      #     笔记截图
│   ├── Day3 Day5/                       #   Day 03 / Day 05 随堂笔记
│   │   ├── day03_随堂笔记.md             #     闭包、装饰器、深浅拷贝
│   │   ├── Day05_随堂笔记.md             #     线程同步、迭代器/生成器、正则
│   │   └── assets/
│   ├── Day4/                            #   Day 04 随堂笔记：网络编程与进程线程
│   ├── Day6/                            #   Day 06 随堂笔记：顺序表与链表
│   └── Day7/                            #   Day 07 随堂笔记：排序、二分查找、二叉树
│
├── Python数据分析/                       # 主线二：数据分析与科学计算
│   ├── note/                            #   结构化长篇笔记
│   │   ├── Numpy相关内容.md              #     NumPy 全量笔记 + 待补清单
│   │   ├── Pandas相关内容.md             #     pandas 全量笔记（9 章）
│   │   ├── Matlplotlib学习笔记.md        #     Matplotlib + seaborn 全量笔记（7 章，25 张实绘图）
│   │   └── assets/                      #     笔记配图与图表渲染产物
│   ├── code/                            #   Jupyter 实践
│   │   ├── Numpy学习.ipynb
│   │   ├── Pandas-Series学习.ipynb
│   │   ├── Pandas-DataFrame学习.ipynb
│   │   ├── 数据分析.ipynb                #     综合主线 + 两个实战案例
│   │   ├── Matplotlib学习.ipynb          #     五类基础图表 + 多子图 + seaborn
│   │   ├── 项目实战-房地产市场分析.ipynb   #     10 万条二手房数据实战
│   │   ├── data/                        #     企鹅、睡眠、天气、员工、二手房等数据集
│   │   └── output/                      #     导出产物
│   ├── env.yml                          #   conda 环境导出（可复现）
│   └── .conda/                          #   环境本体（不提交）
│
├── 虚拟环境venv.conda/                   # 专题：环境管理
│   ├── note.md                          #   venv / conda / mamba 图文笔记
│   ├── assets/                          #   笔记截图
│   └── code/myvenv/                     #   虚拟环境本体（不提交）
│
├── .gitignore                           # 忽略虚拟环境、缓存与编辑器配置
└── README.md                            # 本文件（总索引）
```

---

## 阅读建议

1. **按天顺序推进**：Day 1 → Day 7 为课程主线，先读 `Day*/` 下的 `.md` 笔记理解概念，再跑 `Code/day*/` 下的编号示例验证。
2. **代码编号即讲解顺序**：`01_` → `19_` 的编号与笔记小节一一对应，`example_` 前缀的文件为综合实战题。
3. **数据分析建议对照阅读**：`note/` 下的笔记是体系化沉淀，`code/` 下的 Notebook 是可执行的随堂过程，两者互为补充。
4. **Obsidian 用户**：本仓库同时作为 Obsidian 库使用，笔记内的图片以 `assets/` 相对路径引用，在 GitHub 与 Obsidian 中均可正常渲染。

---

## 维护说明

- 本 README 为仓库总索引，新增笔记或代码后请同步更新对应分类的表格与[目录结构](#目录结构)。
- 所有链接均为仓库内**相对路径**，保持目录结构不变即可保证链接有效；路径含空格的目录（如 `Day3 Day5`）在链接中需写作 `Day3%20Day5`。
- 虚拟环境目录（`Python数据分析/.conda/`、`虚拟环境venv.conda/code/myvenv/`）与 Python 缓存已在 `.gitignore` 中排除；`虚拟环境venv.conda/note.md` 与 `assets/` 属笔记内容，正常提交。
- `.gitignore` 中虽已声明忽略 `.idea/`、`.obsidian/`、`.claudian/`，但这些目录在早期提交中已被纳入版本控制，`.gitignore` 对**已跟踪文件无效**。若希望彻底移出仓库，需执行一次 `git rm -r --cached .idea .obsidian .claudian` 后再提交。
- 待补充内容：NumPy 笔记末尾的「缺失知识点清单」为后续学习的 TODO 列表；房地产实战中编号 A3—A5 等问题尚未展开。
