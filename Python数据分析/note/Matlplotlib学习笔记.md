  ## 1. 数据可视化的原则

信：表达准确，避免可视化的误导性

达：高效传达，有效信息直接高效传达

雅：赏心悦目，设计美观的可视化（布局，配色）

## 2. 常见图表

![[Pasted image 20260822212424.png]]

## 3. 可视化基础

### 3.1 可视化工具对比

|工具|说明|优点|缺点|
|---|---|---|---|
|matplotlib|Python 最基础可视化库|灵活强大、定制性强|代码多、风格基础|
|seaborn|基于 matplotlib 的高级接口|风格美观、统计图方便|对简单图略繁琐|
|pandas plot|快速图表，调用 .plot ()|快捷、适合 EDA|图表样式较少|


箱型图的要素说明
![[Pasted image 20260825123621.png]]

## 4. Matplotlib 基础绘图

### 4.1 绘图的通用流程

> 五种基础图表与对应函数：折线图 `plot`、条形图 `bar` / `barh`、饼图 `pie`、散点图 `scatter`、箱线图 `boxplot`。

```mermaid
flowchart LR
    A[导入 pyplot + 配置中文] --> B[figure 创建画布]
    B --> C[plot/bar/pie... 绘制数据]
    C --> D[title/xlabel/legend 装饰]
    D --> E[grid/xticks/ylim 细节调整]
    E --> F[tight_layout + show/savefig]

    %% 样式
    classDef main fill:#e8e8ff,stroke:#8a8acb,stroke-width:1px;
    class A,B,C,D,E,F main;
```

**中文字体配置**（不配置则中文显示为方框）

```python
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'      # Windows 用 SimHei，mac 用 AppleGothic
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False  # 解决负号显示为方框的问题
rcParams['font.size'] = 12
```

### 4.2 画布与常用装饰函数

| 函数 | 作用 | 常用参数 |
| :--- | :--- | :--- |
| `plt.figure()` | 创建画布 | `figsize`（英寸尺寸）、`dpi`（像素密度）、`facecolor`、`edgecolor`、`num`、`clear`、`frameon` |
| `plt.title()` | 图表标题 | `color`、`fontsize` |
| `plt.xlabel()` / `plt.ylabel()` | 坐标轴标签 | `fontsize`、`color` |
| `plt.legend()` | 图例（需绘图时传 `label`） | `loc='upper left'` 等 |
| `plt.grid()` | 网格线 | `alpha` 透明度、`linestyle`（`-` 实线 / `--` 虚线 / `:` 点线）、`axis`（`x` / `y`） |
| `plt.xticks()` / `plt.yticks()` | 刻度样式 | `fontsize`、`rotation` 旋转角度 |
| `plt.xlim()` / `plt.ylim()` | 坐标轴范围 | `(最小值, 最大值)` |
| `plt.text()` | 在指定坐标写文字 | `ha` 水平对齐（left/center/right）、`va` 垂直对齐（top/center/bottom） |
| `plt.tight_layout()` | 自动优化排版，防止标签被裁剪 | — |
| `plt.show()` | 显示图表 | — |

> **数据标签的封装**：给每个数据点标注数值是高频操作，封装成函数后可复用到任意图表。
>
> ```python
> def add_label(x_list, y_list):
>     for x, y in zip(x_list, y_list):
>         plt.text(x, y, str(y), ha='center', va='bottom')
> ```

### 4.3 折线图 plot

> **适用场景**：趋势随时间的变化。

| 参数 | 说明 |
| :--- | :--- |
| `label` | 图例名称，配合 `plt.legend()` 使用 |
| `color` | 线条颜色 |
| `linewidth` | 线宽 |
| `linestyle` | 线型：`-` 实线、`--` 虚线、`:` 点线 |
| `marker` | 数据点标记，如 `o`（圆点）、`s`（方块）、`^`（三角） |

```python
plt.figure(figsize=(10, 5))     # 画布的概念

month = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
sales = [100, 124, 234, 450, 400, 350, 400, 450, 500, 550, 600, 650]
sales2 = [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340]

# 同一张画布上画两条线，即多系列对比
plt.plot(month, sales, label='产品A', color='blue', linewidth=2)
plt.plot(month, sales2, label='产品B', color='red', marker='o', linestyle='--')

plt.title('2025年销售量趋势', color='red', fontsize=20)
plt.xlabel('月份', fontsize=16, color='purple')
plt.ylabel('销售量（万元）', fontsize=16, color='purple')
plt.legend(loc='upper left')
plt.grid(alpha=0.5, linestyle='--')
plt.xticks(fontsize=12, rotation=45)
plt.ylim(0, 700)

add_label(month, sales)         # 为每个数据点添加数值标签
add_label(month, sales2)
plt.show()
```

![[mpl_01_plot_line.png]]

### 4.4 柱状图 bar

> **适用场景**：类别之间的数值对比（纵向）。

```python
plt.figure(figsize=(10, 5))

subjects = ['语文', '数学', '英语', '物理', '化学', '生物']
scores = [80, 90, 75, 95, 85, 92]

plt.bar(subjects, scores, label='成绩', width=0.5, color='orange')   # width 控制柱子宽度
add_label(subjects, scores)

plt.legend(loc='upper left')
plt.title('期中考试平均成绩', color='red', fontsize=20)
plt.xlabel('科目', fontsize=16, color='purple')
plt.ylabel('成绩', fontsize=16, color='purple')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)   # 柱状图只需要横向网格线
plt.tight_layout()
plt.show()
```

![[mpl_02_bar.png]]

### 4.5 条形图 barh

> **适用场景**：类别名称较长、类别较多时的横向对比。注意柱状图用 `width` 调宽度，条形图用 `height`；网格线、坐标范围也要相应换成 `axis='x'`、`xlim()`。

```python
plt.figure(figsize=(10, 5))

countries = ['中国', '美国', '英国', '法国', '意大利', '西班牙']
gdp = [89, 90, 75, 95, 85, 92]

plt.barh(countries, gdp, height=0.5, color='lightblue', label='GDP')

# 横向图的标签：x 为数值、y 为类别，x 加偏移量避免文字压在柱子上
[plt.text(x + 2, y, str(x), ha='center', va='center') for x, y in zip(gdp, countries)]

plt.legend(loc='upper left')
plt.title('2025年GDP表', color='blue', fontsize=20)
plt.xlabel('GDP', fontsize=16, color='purple')
plt.ylabel('国家', fontsize=16, color='purple')
plt.xlim(0, 100)
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
```

![[mpl_03_barh.png]]

### 4.6 饼图 pie

> **适用场景**：整体的组成比例。类别超过 5—7 个时饼图会难以辨认，此时应改用条形图。

| 参数 | 说明 |
| :--- | :--- |
| `labels` | 每一块的名称 |
| `autopct` | 自动添加百分比标签，`'%.1f%%'` 表示保留一位小数并加百分号 |
| `startangle` | 起始角度，默认 0 度，常用 90 度让第一块从正上方开始 |
| `colors` | 每一块的颜色列表 |
| `wedgeprops={'width': 0.6}` | 设置圆环宽度，饼图变**环形图** |
| `pctdistance` | 百分比文字距圆心的相对距离 |
| `explode` | 突出块的偏移列表，做**爆炸式饼图** |

**1. 基础饼图**

```python
plt.figure(figsize=(10, 5))

things = ['学习', '工作', '睡觉', '吃饭', '其他']
time = [6, 4, 8, 1, 5]
colors = ['#FFC0CB', '#ADD8E6', '#DDA0DD', '#98FB98', '#FFF6B7']

plt.pie(time, labels=things, autopct='%.1f%%', startangle=90, colors=colors)
plt.title('一天的时间分布', color='blue', fontsize=20)
plt.tight_layout()
plt.show()
```

![[mpl_04_pie.png]]

**2. 环形图（甜甜圈图）**：圆心留白处可用 `plt.text()` 写总量，信息密度更高。

```python
plt.pie(time, labels=things,
        autopct='%.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops={'width': 0.6},   # 设置圆环的宽度百分比
        pctdistance=0.6              # 设置百分比数字的位置
        )
plt.title('一天的时间分布', color='blue', fontsize=20)
plt.text(0, 0, '总计24小时', ha='center', va='center', fontsize=16)
plt.tight_layout()
plt.show()
```

![[mpl_05_pie_donut.png]]

**3. 爆炸式饼图**：用 `explode` 把需要强调的那一块拉出来。

```python
explode = [0.1, 0, 0, 0, 0]   # 只突出第一块「学习」
plt.pie(time, labels=things, autopct='%.1f%%', startangle=90,
        colors=colors, explode=explode)
plt.title('一天的时间分布', color='blue', fontsize=20)
plt.tight_layout()
plt.show()
```

![[mpl_06_pie_explode.png]]

### 4.7 散点图 scatter

> **适用场景**：观察两个变量的相关性。与折线图的区别是**散点图没有连接线**。

| 参数 | 说明 |
| :--- | :--- |
| `s` | 点的大小 |
| `alpha` | 透明度，点重叠密集时用于观察分布密度 |
| `color` | 点的颜色 |
| `label` | 图例名称 |

**1. 最简形式**

```python
plt.figure(figsize=(10, 5))
scores = [50, 55, 60, 65, 70, 75, 80]
hours = [1, 2, 3, 4, 5, 6, 7]
plt.scatter(hours, scores)
plt.show()
```

![[mpl_07_scatter_basic.png]]

**2. 完整形式：随机数据 + 回归线**

```python
import random

plt.figure(figsize=(10, 8))

# 构造 y = 2x + 噪声 的模拟数据：gauss(0, 2) 为均值 0、标准差 2 的高斯噪声
x, y = [], []
for i in range(200):
    tmp = random.uniform(0, 10)
    x.append(tmp)
    y.append(2 * tmp + random.gauss(0, 2))

plt.scatter(x, y, color='blue', alpha=0.5, s=40, label='数据')
plt.title('X变量与Y变量的关系图')
plt.legend(loc='upper left')
plt.xlabel('X自变量')
plt.ylabel('Y因变量')
plt.grid(True, linestyle='--', alpha=0.5)

plt.plot([0, 10], [0, 20], color='red', linewidth=2)   # 用 plot 画一条参考回归线
plt.show()
```

![[mpl_08_scatter_reg.png]]

### 4.8 箱线图 boxplot

> **适用场景**：查看数据分布与识别异常值（要素说明见 3.1 的箱型图示意）。

```python
plt.figure(figsize=(8, 6))

# 模拟三门课的成绩
data = {
    '语文': [80, 90, 85, 77, 88, 92, 88, 90, 85, 92],
    '数学': [85, 95, 88, 92, 90, 85, 92, 88, 90, 92],
    '英语': [90, 85, 92, 88, 90, 85, 92, 88, 90, 92]
}

# 字典的 values 作为数据、keys 作为刻度标签
plt.boxplot(data.values(), tick_labels=data.keys())
plt.title('各科成绩分布（箱线图）')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()
```

![[mpl_09_boxplot.png]]

> **版本差异**：Matplotlib 3.9 起参数名由 `labels` 改为 `tick_labels`，旧版本传 `tick_labels` 会报 `TypeError`。

### 4.9 多子图 subplot

`plt.subplot(行数, 列数, 第几个)`：把画布切成网格，返回该格子的坐标轴对象，之后用**对象方法**绘图。

> 坐标轴对象上的方法名与 `plt.` 函数略有差异：设置刻度旋转用 `ax.tick_params(axis='x', rotation=45)`，而不是 `plt.xticks(rotation=45)`。

```python
month = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
sales = [100, 124, 234, 450, 400, 350, 400, 450, 500, 550, 600, 650]

f1 = plt.subplot(2, 2, 1)   # 2 行 2 列，第 1 个子图
f1.plot(month, sales)
f1.tick_params(axis='x', rotation=45)

f2 = plt.subplot(2, 2, 2)   # 2 行 2 列，第 2 个子图
f2.bar(month, sales)
f2.tick_params(axis='x', rotation=45)

f3 = plt.subplot(2, 2, 3)
f3.scatter(month, sales)
f3.tick_params(axis='x', rotation=45)

f4 = plt.subplot(2, 2, 4)
f4.barh(month, sales)

plt.tight_layout()          # 子图较多时必加，否则标签互相遮挡
plt.show()
```

![[mpl_10_subplot.png]]

### 4.10 图表类型的选择

| 图表 | 函数 | 回答的问题 |
| :--- | :--- | :--- |
| 折线图 | `plot` | 趋势随时间如何变化 |
| 柱状图 / 条形图 | `bar` / `barh` | 类别之间谁大谁小 |
| 饼图 / 环形图 | `pie` | 整体由哪些部分构成，占比多少 |
| 散点图 | `scatter` | 两个变量是否相关 |
| 箱线图 | `boxplot` | 数据分布如何，有无异常值 |
| 直方图 | `hist` | 单个数值变量落在各区间的频次 |

> **选图的顺序是「先问题、后图形」**：先明确要回答什么问题，再挑图表；反过来先选图再凑数据，容易违背「信」的原则。

## 5. 分析案例：气温与降水（weather.csv）

> 流程：**导入库 → 读入数据 → 筛选分析范围 → 按问题选图**。

```python
# 1. 导入库
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']

# 2. 导入数据
df = pd.read_csv('data/weather.csv')
df.head()

# 3.1 绘制气温的趋势变化图
df['date'] = pd.to_datetime(df['date'])      # 字符串转日期，才能按年份筛选
df = df[df['date'].dt.year == 2015]          # 只保留 2015 年
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temp_max'], label='最高气温')
plt.plot(df['date'], df['temp_min'], label='最低气温')
plt.legend(loc='upper left')
plt.title('2015年气温趋势变化图')
plt.xlabel('日期')
plt.ylabel('气温')
plt.show()
```

![[mpl_11_weather_line.png]]

> 最高温与最低温两条曲线同步呈现「中间高、两端低」的单峰形态，7—8 月为全年峰值，两条线的间距（日温差）在夏季略大于冬季。

```python
# 3.2 降水量的直方图：hist 只需要一列数值，bins 指定分组数量
plt.hist(df['precipitation'], bins=5)
plt.title('2015年降水量直方图')
plt.xlabel('降水量')
plt.ylabel('次数')
plt.show()
```

![[mpl_12_weather_hist.png]]

> 降水量呈极端**右偏分布**：绝大多数日子降水量接近 0，少数暴雨日拉长了右尾。这类分布用直方图一眼可见，用均值描述则会失真——这正是「信」的体现。

## 6. Seaborn 常用统计图

> Seaborn 是基于 Matplotlib 的高级接口（见 3.1 工具对比）：统一传 `data=DataFrame` + 列名，默认样式更美观，统计图（核密度、成对关系）开箱即用。Matplotlib 的 `title`、`grid` 等装饰函数依然通用。

```python
import seaborn as sns
penguins = pd.read_csv('data/penguins.csv')
penguins.dropna(inplace=True)      # 绘图前先清洗缺失值
penguins.info()
```

| 函数 | 图形 | 典型用途 |
| :--- | :--- | :--- |
| `histplot()` | 直方图 | 单变量频次分布，`kde=True` 叠加核密度曲线 |
| `kdeplot()` | 核密度估计图 | 连续分布的平滑形态；同时给 `x` 和 `y` 则为二维核密度 |
| `countplot()` | 计数图 | 分类变量各取值的数量 |
| `scatterplot()` | 散点图 | 两变量关系，`hue` 按组着色 |
| `jointplot(kind='hex')` | 蜂窝图 | 散点密集时用六边形网格表达密度 |
| `barplot()` | 条形图 | 分组聚合结果，默认聚合函数为均值 |
| `pairplot()` | 成对关系图 | 所有数值列两两组合的散点矩阵 |

### 6.1 单变量分布

```python
# 直方图：分类列作为 x 时，等价于按类别计数
sns.histplot(data=penguins, x='species')
```

![[sns_13_histplot_species.png]]

```python
# 核密度估计图：喙长度的平滑分布，可见明显的双峰
sns.kdeplot(data=penguins, x='bill_length_mm')
```

![[sns_14_kdeplot.png]]

```python
# 直方图 + 核密度曲线：频次与形态一起看
sns.histplot(data=penguins, x='bill_length_mm', kde=True)
```

![[sns_15_histplot_kde.png]]

```python
# 计数图：统计不同岛屿的企鹅数量
sns.countplot(data=penguins, x='island')
```

![[sns_16_countplot_island.png]]

```python
# 与直方图对比：同一份分类数据，两者柱子高度完全一致
sns.histplot(data=penguins, x='island')
```

![[sns_17_histplot_island.png]]

> **countplot 与 histplot 的区别**：`countplot` 专为分类变量设计（直接数个数）；`histplot` 面向连续变量分箱统计，遇到分类列时退化为计数，因此柱高相同，只是默认柱宽与配色不同。

### 6.2 双变量关系

```python
# 散点图：横轴体重、纵轴脚蹼长度，hue 按性别分组着色
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex')
```

![[sns_18_scatterplot_hue.png]]

```python
# 蜂窝图：jointplot 设置 kind='hex'，边缘还会附带两个变量的直方图
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm', kind='hex')
```

![[sns_19_jointplot_hex.png]]

```python
# 二维核密度图：同时给 x 和 y，用等高线表达联合分布的密集区域
sns.kdeplot(data=penguins, x='body_mass_g', y='flipper_length_mm')
```

![[sns_20_kdeplot_2d.png]]

> 三张图回答的是同一个问题（体重与脚蹼长度正相关），表达方式递进：散点看**个体**，蜂窝看**密度**，等高线看**联合分布形态**。散点重叠严重时应换用后两者。

### 6.3 分组聚合条形图

| 参数 | 说明 |
| :--- | :--- |
| `x` / `y` | 分组变量 / 被聚合的数值变量 |
| `estimator` | 聚合函数，默认 `'mean'`，可用 `'median'`、`'sum'`、`'count'` |
| `errorbar` | 误差条，默认显示置信区间，传 `None` 关闭 |

```python
# 各品种企鹅的平均喙长度，关闭误差条使图形更简洁
sns.barplot(data=penguins, x='species', y='bill_length_mm',
            estimator='mean', errorbar=None)
```

![[sns_21_barplot.png]]

> `barplot` 内部已完成「分组 + 聚合」，相当于 `df.groupby('species')['bill_length_mm'].mean()` 的可视化版本，无需先用 pandas 聚合再画图。

### 6.4 成对关系图 pairplot

```python
# 所有数值列两两配对：对角线为各变量自身分布，非对角线为散点图
sns.pairplot(data=penguins, hue='species')
```

![[sns_22_pairplot.png]]

> `pairplot` 是**探索性分析（EDA）的第一张图**：一次性看清所有数值变量的分布与两两相关性。加上 `hue` 后还能立刻判断哪些变量对分类最有区分度——图中 Gentoo（绿色）在体重与脚蹼长度上与另两类几乎完全分离。列数很多时开销较大，建议先筛选关注的列。

## 7. 项目实战：房地产市场洞察与价值评估

> 数据集：`data/house_sales.csv`，原始 106118 条 / 12 个字段，清洗后 26135 条。完整代码见 [[项目实战-房地产市场分析.ipynb]]。

```mermaid
flowchart LR
    A[导入数据 106118 条] --> B[删无用列 origin_url]
    B --> C[缺失值 dropna]
    C --> D[重复值 29416 条去重]
    D --> E[类型转换：去单位转数值]
    E --> F[异常值：面积区间 + 价格 IQR]
    F --> G[特征构造：地区/楼层/楼龄/分箱]
    G --> H[提出问题 → 聚合 → 可视化]

    %% 样式
    classDef main fill:#e8e8ff,stroke:#8a8acb,stroke-width:1px;
    class A,B,C,D,E,F,G,H main;
```

### 7.1 数据清洗与特征构造

```python
# 1. 导入相关库并设置中文字体
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']

# 2. 导入数据 + 数据概览
df = pd.read_csv('data/house_sales.csv')
print(f"总记录数: {len(df)}")        # 106118
print(f"字段总数: {len(df.columns)}")  # 12
df.info()

# 3. 数据清洗
df.drop(columns='origin_url', inplace=True)   # 删除无用列
df.isna().sum()                               # 检查缺失
df.dropna(inplace=True)                       # 直接剔除缺失行
print(f"重复值数量: {df.duplicated().sum()}")  # 29416
df.drop_duplicates(inplace=True)

# 类型转换：字符串去掉单位后转数值，否则无法参与计算
df['area'] = df['area'].str.replace('㎡', '').astype(float)
df['price'] = df['price'].str.replace('万', '').astype(float)
df['unit'] = df['unit'].str.replace('元/㎡', '').astype(float)
df['year'] = df['year'].str.replace('年建', '').astype(int)
df['toward'] = df['toward'].astype('category')   # 朝向重复值多，转分类型省内存

# 异常值处理：面积用业务区间，价格用 IQR 法
df = df[(df['area'] < 600) & (df['area'] > 20)]
Q1, Q3 = df['price'].quantile(0.25), df['price'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['price'] > Q1 - 1.5 * IQR) & (df['price'] < Q3 + 1.5 * IQR)]
```

> **`.str` 报错排查**：若某列已是数值类型，再调用 `.str.replace()` 会抛 `AttributeError: Can only use .str accessor with string values`。清洗脚本重复执行时最易踩到，可先 `df['area'].dtype` 确认，或写成 `df['area'].astype(str).str.replace(...)`。

**新特征的构造**

| 新字段 | 构造方式 | 说明 |
| :--- | :--- | :--- |
| `district` | `df['address'].str.split('-').str[0]` | 从地址中取出地区 |
| `floor_type` | `df['floor'].str.split('（').str[0]` | 按括号分割取「低/中/高层」 |
| `floor_type2` | `df['floor'].apply(fun1)` | 用函数判断关键字，可统一处理缺失为「未知」 |
| `is_direct` | `df['city'].apply(fun2)` | 是否为一线城市（北上广深） |
| `bedrooms` | `df['rooms'].str.split('室').str[0]` | 卧室数量 |
| `living_rooms` | `df['rooms'].str.extract(r'(\d+)厅')` | 客厅数量，正则写法更简洁 |
| `building_age` | `2026 - df['year']` | 楼龄 |
| `price_labels` | `pd.cut(df['price'], bins=5, labels=[...])` | 价格分段：低/中/高/超高/超超高 |

```python
# 分割法 vs 函数法：函数法能兼容缺失值和不规范取值
def fun1(str1):
    if pd.isna(str1):
        return '未知'
    elif '低' in str1:
        return '低楼层'
    elif '中' in str1:
        return '中楼层'
    elif '高' in str1:
        return '高楼层'
    else:
        return '未知'

df['floor_type2'] = df['floor'].apply(fun1).astype(object)
df['price_labels'] = pd.cut(df['price'], bins=5,
                            labels=['低', '中', '高', '超高', '超超高']).astype(object)
df['price_labels'].value_counts()
# 中 11114 / 低 5801 / 高 5587 / 超高 2387 / 超超高 1246
```

> 价格分箱后呈「中间多、两端少」的橄榄型，说明剔除极端值后房价分布已接近正常形态。

### 7.2 A1 · 哪些变量最影响房价

> **分析主题**：特征相关性　**方法**：皮尔逊相关系数 + 热力图

```python
# 选择数值型特征计算相关系数矩阵
a = df[['price', 'area', 'unit', 'building_age']].corr()
a['price'].sort_values(ascending=False)[1:]
# unit 0.743 / area 0.453 / building_age 0.092

plt.figure(figsize=(10, 8))
sns.heatmap(a, cmap='coolwarm')     # cmap='coolwarm' 冷暖色表达正负相关
plt.title('房屋特征相关性热力图')
plt.tight_layout()
```

![[house_23_heatmap.png]]

> **结论**：单价（`unit`, 0.74）对总价的影响最大，其次是面积（`area`, 0.45），楼龄（`building_age`, 0.09）几乎无线性影响。也就是说总价主要由「地段决定的单价」而非「房子有多新」决定。

### 7.3 A2 · 全国房价的总体分布

> **分析主题**：描述性统计　**方法**：`describe()` + 直方图

```python
df.describe()
```

| 指标 | area | price | unit | building_age |
| :--- | ---: | ---: | ---: | ---: |
| count | 26135 | 26135 | 26135 | 26135 |
| mean | 103.76 | 117.21 | 11610.13 | 12.93 |
| std | 34.00 | 60.97 | 5824.25 | 6.02 |
| min | 21.00 | 9.00 | 1000.00 | 3.00 |
| 25% | 85.01 | 72.00 | 7587.00 | 9.00 |
| 50% | 100.00 | 103.00 | 10312.00 | 11.00 |
| 75% | 123.00 | 150.00 | 14184.00 | 15.00 |
| max | 470.00 | 306.00 | 85288.00 | 50.00 |

```python
# 房价分布的直方图 + 核密度曲线
sns.histplot(df['price'], bins=20, kde=True)
plt.tight_layout()
plt.title('全国房价分布直方图')
plt.grid(axis='y', alpha=0.5, linestyle='--')
plt.show()
```

![[house_24_price_hist.png]]

> **结论**：房价呈**右偏分布**，均值（117 万）高于中位数（103 万），说明少量高价房拉高了平均值。这类分布下用**中位数**描述「典型房价」比均值更可信。

### 7.4 A6 · 朝向溢价

> **分析主题**：朝向溢价　**方法**：分组聚合 + 箱线图

```python
df['toward'].value_counts()
df.groupby('toward').agg({
    'price': ['mean', 'median'],
    'unit': ['median'],
    'building_age': ['mean']
})
```

| 朝向 | price mean | price median | unit median | building_age mean |
| :--- | ---: | ---: | ---: | ---: |
| 西南向 | 139.71 | 138.4 | 13333.0 | 14.45 |
| 南北向 | 119.47 | 104.5 | 10000.0 | 13.07 |
| 西北向 | 119.11 | 105.0 | 12290.0 | 14.47 |
| 东南向 | 115.54 | 105.0 | 10864.0 | 11.95 |
| 东北向 | 114.56 | 100.0 | 12198.0 | 13.61 |
| 南向 | 114.56 | 103.0 | 10759.0 | 12.55 |
| 东向 | 110.16 | 95.0 | 11421.0 | 13.76 |
| 西向 | 102.66 | 86.0 | 12528.0 | 14.39 |
| 东西向 | 98.94 | 82.0 | 9000.0 | 16.49 |
| 北向 | 92.53 | 75.5 | 11698.0 | 14.11 |

```python
plt.figure(figsize=(14, 5))
sns.boxplot(x='toward', y='price', data=df)
plt.tight_layout()
plt.xlabel('朝向')
plt.ylabel('价格（万元）')
plt.title('不同朝向的价格分布')
plt.grid(axis='y', alpha=0.5, linestyle='--')
plt.show()
```

![[house_25_toward_box.png]]

> **结论**：南北向（119.5 万）确实比单一南向（114.6 万）平均贵约 5 万元、溢价 4.3%，但差距远小于「南北通透」的营销宣传所暗示的幅度；北向最便宜（92.5 万），比南北向低约 27 万。
>
> **注意样本量**：西南向均值最高（139.7 万），但其样本仅百余条，箱线图上箱体宽度与离群点分布都不稳定，不宜直接下结论。**分组聚合必须同时看 `count`**，否则小样本组的均值极易误导——这正是「信」原则要防的坑。

### 7.5 分析小结

| 问题编号 | 问题 | 图表 | 结论 |
| :---: | :--- | :--- | :--- |
| A1 | 哪些变量最影响房价 | 相关性热力图 | 单价 > 面积 ≫ 楼龄 |
| A2 | 房价总体分布如何 | 直方图 + KDE | 右偏分布，中位数 103 万比均值更有代表性 |
| A6 | 南北向是否更贵 | 分组聚合 + 箱线图 | 贵约 4.3%，但小样本朝向的均值不可靠 |

> **可视化在分析中的定位**：聚合表格给出**精确数值**，图表给出**分布形态与异常信号**。两者必须配合——只看均值表会错过右偏与小样本问题，只看图则读不出具体溢价幅度。













