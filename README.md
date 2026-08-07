<p align="center">
  <h1 align="center">My Study Note</h1>
  <p align="center">个人技术栈沉淀 · Python 学习知识库</p>
  <p align="center">
    <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" alt="Markdown"/>
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
    <img src="https://img.shields.io/badge/Socket%20%26%20Threading-4B8BBE?style=flat-square" alt="Socket & Threading"/>
    <img src="https://img.shields.io/badge/正则表达式-3DDC84?style=flat-square&logo=regex&logoColor=white" alt="Regex"/>
    <img src="https://img.shields.io/github/last-commit/USER/REPO?style=flat-square&label=Last%20Commit" alt="Last Commit"/>
    <img src="https://img.shields.io/github/repo-size/USER/REPO?style=flat-square&label=Repo%20Size" alt="Repo Size"/>
  </p>
</p>

> 一个以 **Python** 为核心的渐进式学习仓库：从函数式编程、网络编程、并发编程到数据分析与科学计算，沉淀代码实践与结构化笔记。点击下方目录快速定位，或直接浏览各分类索引。

---

## 快速导航

- [Python 进阶实战](#python-进阶实战)
- [Python 数据分析](#python-数据分析)
- [开发环境与工具链](#开发环境与工具链)
- [仓库统计](#仓库统计)
- [目录结构](#目录结构)

---

## Python 进阶实战

**位置**：`./Python/`　**形式**：按天组织的实战代码（`.py`）+ 配套数据文件

| 模块 | 核心主题 | 文件数 |
|------|----------|:------:|
| [Day 3 · 函数式编程](./Python/day3/) | 闭包、装饰器、深浅拷贝 | 13 |
| [Day 4 · 网络与进程线程](./Python/day04/) | Socket 编程、多进程、多线程入门 | 17 |
| [Day 5 · 并发与进阶语法](./Python/day05/) | 线程同步、生成器、正则表达式 | 19 |

### Day 3 · 函数式编程

- [01 - 闭包背景介绍](./Python/day3/01_闭包背景介绍.py)　`#闭包` `#作用域`
- [02 - 闭包入门](./Python/day3/02_闭包入门.py)　`#闭包`
- [03 - nonlocal 关键字介绍](./Python/day3/03-nonlocal关键字介绍.py)　`#nonlocal`
- [04 - 装饰器入门](./Python/day3/04_装饰器入门.py)　`#装饰器`
- [05 - 装饰器装饰：无参无返回的原函数](./Python/day3/05_装饰器装饰_无参无返回的原函数.py)　`#装饰器`
- [06 - 装饰器装饰：有参无返回的原函数](./Python/day3/06_装饰器装饰_有参无返回的原函数.py)　`#装饰器`
- [07 - 装饰器装饰：无参有返回的原函数](./Python/day3/07_装饰器装饰_无参有返回的原函数.py)　`#装饰器`
- [08 - 装饰器装饰：有参有返回的原函数](./Python/day3/08_装饰器装饰_有参有返回的原函数.py)　`#装饰器`
- [09 - 装饰器装饰：可变参数](./Python/day3/09_装饰器装饰_可变参数.py)　`#装饰器` `#*args`
- [10 - 多个装饰器装饰一个函数](./Python/day3/10_多个装饰器装饰1个函数.py)　`#装饰器` `#执行顺序`
- [11 - 一个装饰器装饰多个函数](./Python/day3/11_1个装饰器装饰多个函数.py)　`#装饰器`
- [13 - 深浅拷贝·面试题](./Python/day3/13_深浅拷贝_面试题.py)　`#深拷贝` `#浅拷贝`

### Day 4 · 网络与进程线程

- [01 - 创建 Socket 对象](./Python/day04/01_创建socket对象.py)　`#socket`
- [02 - 网编案例·服务器端](./Python/day04/02_网编案例_服务器端.py)　`#TCP`
- [03 - 网编案例·客户端](./Python/day04/03_网编案例_客户端.py)　`#TCP`
- [04 - 演示编解码](./Python/day04/04_演示编解码.py)　`#encode` `#decode`
- [05 - 网编案例·模拟多任务版服务器端](./Python/day04/05_网编案例_模拟多任务版服务器端.py)　`#多任务`
- [06 - 网编案例·文件上传·服务器端](./Python/day04/06_网编案例_文件上传_服务器端.py)　`#文件传输`
- [07 - 网编案例·文件上传·客户端](./Python/day04/07_网编案例_文件上传_客户端代码.py)　`#文件传输`
- [08 - 网编案例·文件上传·服务器端模拟多任务版](./Python/day04/08_网编案例_文件上传_服务器端模拟多任务版.py)　`#文件传输`
- [09 - 演示单任务](./Python/day04/09_演示单任务.py)　`#串行`
- [10 - 演示多进程](./Python/day04/10_演示多进程.py)　`#multiprocessing`
- [11 - 带参数的多进程](./Python/day04/11_带参数的多进程.py)　`#进程参数`
- [12 - 获取进程的 pid](./Python/day04/12_获取进程的pid.py)　`#pid`
- [13 - 进程特点之数据隔离](./Python/day04/13_进程特点之数据隔离.py)　`#进程隔离`
- [14 - 进程特点之主进程等待子进程](./Python/day04/14_进程特点之主进程等待子进程结束再结束.py)　`#进程同步`
- [15 - 线程入门案例](./Python/day04/15_线程入门案例.py)　`#threading`
- [16 - 线程入门·带参数的线程](./Python/day04/16_线程入门案例带参数的线程.py)　`#threading`
- [17 - 数字排列组合](./Python/day04/17_数字排列组合.py)　`#itertools`
- 配套数据：[my.txt](./Python/day04/data/my.txt) · [test_data.txt](./Python/day04/data/test_data.txt)

### Day 5 · 并发与进阶语法

- [01 - 多线程的执行具有随机性](./Python/day05/01_多线程的执行具有随机性.py)　`#线程调度`
- [02 - 多线程特点·守护线程](./Python/day05/02_多线程特点_守护线程.py)　`#daemon`
- [03 - 多线程特点·数据共享](./Python/day05/03_多线程特点_数据共享.py)　`#全局变量`
- [04 - 多线程特点·共享全局数据错误问题](./Python/day05/04_多线程特点_共享全局数据出现错误问题.py)　`#竞态条件`
- [05 - 多线程操作·互斥锁](./Python/day05/05_多线程操作_互斥锁.py)　`#Lock` `#同步`
- [06 - 迭代器](./Python/day05/06_迭代器.py)　`#iter` `#next`
- [07 - 生成器入门·推导式写法](./Python/day05/07_生成器入门_推导式写法.py)　`#生成器`
- [08 - 生成器入门·yield 方式](./Python/day05/08_生成器入门_yield方式.py)　`#yield`
- [09 - 生成器生成批次歌词](./Python/day05/09_example_生成器生成批次歌词.py)　`#实战`
- [10 - property 装饰器用法](./Python/day05/10_property_装饰器用法.py)　`#property`
- [11 - property 类属性用法](./Python/day05/11_property_类属性用法.py)　`#property`
- [12 - 正则表达式·校验单个字符](./Python/day05/12_正则表达式_校验单个字符.py)　`#re`
- [13 - 正则替换](./Python/day05/13_正则替换.py)　`#sub`
- [14 - 正则表达式·校验多个字符](./Python/day05/14_正则表达式_校验多个字符.py)　`#量词`
- [15 - 正则表达式·校验开头和结尾](./Python/day05/15_正则表达式_校验开头和结尾.py)　`#锚点`
- [16 - 正则表达式·校验分组](./Python/day05/16_正则表达式_校验分组.py)　`#分组`
- [17 - 校验邮箱](./Python/day05/17_example_校验邮箱.py)　`#实战`
- [18 - 校验 QQ 号](./Python/day05/18_example_校验QQ号.py)　`#实战`
- [19 - 校验 HTML 标签](./Python/day05/19_example_校验html标签.py)　`#实战`
- 配套数据：[jay_lyrics.txt](./Python/day05/data/jay_lyrics.txt)

---

## Python 数据分析

**位置**：`./Python数据分析/`　**形式**：结构化笔记 + Jupyter 实践

| 笔记 | 说明 | 关键词 |
|------|------|--------|
| [Numpy 相关内容](./Python数据分析/note/Numpy相关内容.md) | NumPy 科学计算基础：ndarray 核心特征（多维、同质、高效）、标量/向量/矩阵/张量、向量化运算 | `#NumPy` `#ndarray` `#科学计算` |
| [Numpy 学习（Notebook）](./Python数据分析/code/Numpy学习.ipynb) | 随堂练习 Jupyter Notebook，与笔记配套的动手实践 | `#Jupyter` `#实战` |

> 说明：配套的 Anaconda 环境位于 `Python数据分析/.conda/`，已通过 `.gitignore` 排除，不随仓库提交。

---

## 开发环境与工具链

**位置**：`./虚拟环境venv.conda/`

| 笔记 | 说明 | 关键词 |
|------|------|--------|
| [Python 虚拟环境——venv 与 conda](./虚拟环境venv.conda/note.md) | 为什么需要虚拟环境、venv 创建与使用、conda 环境管理、依赖冲突与隔离机制（含图文） | `#venv` `#conda` `#pip` `#环境隔离` |

> 说明：笔记内嵌截图存放于 `虚拟环境venv.conda/assets/`；实际虚拟环境本体 `code/myvenv/` 已被 `.gitignore` 排除。

---

## 仓库统计

| 指标 | 数值 |
|------|:----:|
| 结构化笔记（Markdown） | 2 |
| Jupyter Notebook | 1 |
| Python 示例代码 | 49 |
| 核心模块 | 3 |
| 覆盖主题 | 闭包 / 装饰器 / Socket 网络编程 / 多线程 / 互斥锁 / 迭代器 / 生成器 / property / 正则表达式 / NumPy / 虚拟环境 |

---

## 目录结构

```
my-study-note/
├── Python/                          # Python 进阶实战
│   ├── day3/                        #    函数式编程：闭包、装饰器、深浅拷贝
│   ├── day04/                       #    网络编程、多进程、多线程
│   ├── day05/                       #    线程同步、生成器、正则
│   └── .idea/                       #    编辑器配置（不提交）
├── Python数据分析/                  # 数据分析与科学计算
│   ├── note/Numpy相关内容.md        #    NumPy 核心笔记
│   ├── code/Numpy学习.ipynb         #    配套练习
│   └── .conda/ .idea/ .vscode/      #    环境与配置（不提交）
├── 虚拟环境venv.conda/              # venv / conda 虚拟环境笔记
│   ├── note.md                      #    环境管理图文笔记
│   ├── assets/                      #    笔记截图
│   └── code/myvenv/                 #    虚拟环境本体（不提交）
├── .gitignore                       # 忽略环境/配置目录
└── README.md                        # 本文件（索引）
```

---

## 维护说明

- 本 README 由目录结构自动整理生成，新增笔记后请同步更新对应分类索引。
- Badges 中 `USER/REPO` 为占位符，发布到 GitHub 后请替换为实际仓库名（如 `username/repository`）以显示实时数据。
- 所有链接均为仓库内相对路径，保持目录结构不变即可保证链接有效。
- 仓库中两个虚拟环境目录（`Python数据分析/.conda/` 与 `虚拟环境venv.conda/code/myvenv/`）已在 `.gitignore` 中排除；其中 `虚拟环境venv.conda/` 内的 `note.md` 与 `assets/` 为笔记内容，仍正常提交。