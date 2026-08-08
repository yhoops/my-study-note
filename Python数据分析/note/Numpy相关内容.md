## 1. 介绍

numpy 是 Python 中科学计算的基础包。

它是一个 Python 库，提供多维数组对象、各种派生对象（例如掩码数组和矩阵）以及用于对数组进行快速操作的各种方法，包括数学、逻辑、形状操作、排序、选择、I/O、离散傅里叶变换、基本线性代数、基本统计运算、随机模拟等等。

## 2. ndarray

#### 2.1 ndarray的核心特征

numpy 数组(ndarray)的核心特征：
	1. 多维性：支持 0 维、1维、2维及更高维数组。
	2. 同质性：所有元素类型必须一致(通过dtype指定)
	3. 高效性：基于连续内存块存储，支持向量化运算

根据维度不同，数组可分为以下层次：

| 名称 | 维度 | 示例 | 备注 |
|-----|-----|------|-----|
| 标量 | 0维 | `5`, `3.14` | 单个数字，无行列 |
| 向量 | 1维 | `[1, 2, 3]` | 只有行或列（一维数组） |
| 矩阵 | 2维 | `[[1, 2], [3, 4]]` | 严格的行列结构（二维表） |
| 张量 | ≥3维 | `[[[1, 2], [3, 4]]]` | 高阶数组（如 RGB 图像） |

**多维性（代码验证）**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])      # 创建1维数组
print(arr)
print(f'arr的维度：{arr.ndim}')       # => 1

arr = np.array(1)                    # 创建0维数组（标量）
print(arr)
print(f'arr的维度：{arr.ndim}')       # => 0

arr = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])  # 创建2维数组
print(arr)
print(f'arr的维度：{arr.ndim}')       # => 2
```

**同质性（类型强制转换）**

```python
arr = np.array([1, "尚硅谷"])   # 不同类型会被强制转换成相同类型
print(arr)
print(arr.dtype)                # => <U1 字符串类型

arr = np.array([1, 2.3])        # 整数会被提升为浮点
print(arr)                      # => [1.  2.3]
print(arr.dtype)                # => float64
```

#### 2.2 ndarray的属性

| 属性       | 解释                       | 使用示例         |
| -------- | ------------------------ | ------------ |
| shape    | 数组的形状；行数和列数（或更高维度的尺寸）    | arr.shape    |
| ndim     | 维度数量；数组是几维的（1维，2维，3维等）   | arr.ndim     |
| size     | 总元素个数；数组中所有元素的总数         | arr.size     |
| dtype    | 元素类型；数组中元素的类型（整数，浮点等）    | arr.dtype    |
| T        | 转置；行变列，列变行               | arr.T        |
| itemsize | 单个元素占用的内存字节数             | arr.itemsize |
| nbytes   | 数组总内存占用量：size * itemsize | arr.nbytes   |
| flags    | 内存存储方式；是否连续存储（高级优化）      | arr.flags    |

**代码验证**

```python
arr = np.array([1, 2.5, 3, 4])
print(f"数组的形状：{arr.shape}")          # (4,)  1维数组
print(f"数组元素的个数：{arr.size}")        # 4
print(f"数组元素的数据类型：{arr.dtype}")   # float64
print(f"元素的转置：{arr.T}")              # 1维数组转置不明显

arr = np.array([[1, 2, "尚硅谷", 4], [1, 2, 3, 5]])
print(f"数组的形状：{arr.shape}")          # (2, 4)  2维（行数,列数）
print(f"数组元素的个数：{arr.size}")        # 8
print(f"数组元素的数据类型：{arr.dtype}")   # <U11 字符串类型
print(f"元素的转置：\n{arr.T}")            # 2维数组转置比较明显（行变列，列变行）
```

**0 维数组（标量）的属性验证**

```python
arr = np.array(1)
print(arr)                              # 1
print(f"数组的形状：{arr.shape}")         # ()  0维数组的形状
print(f"数组元素的个数：{arr.size}")       # 1
print(f"数组元素的数据类型：{arr.dtype}")  # int64
```

#### 2.3 ndarray的创建方式

| 创建方式 | 典型方法 | 适用场景 |
|--------|--------|--------|
| 基础构造 | `np.array()` | 手动构建小规模数组、复制已有数据 |
| 预定义形状填充 | `np.zeros()`、`np.ones()`、`np.full()` | 全0占位、全1初始化等固定形状数组 |
| 基于数值范围生成 | `np.arange()`、`np.linspace()` | 数值序列、时间序列、坐标网格 |
| 特殊矩阵生成 | `np.eye()`、`np.diag()` | 单位矩阵等线性代数专用矩阵 |
| 随机数组生成 | `np.random.default_rng()` | 模拟数据、初始化神经网络权重 |
| 高级构造方法 | `np.loadtxt()`、`np.fromfunction()` | 文件/字符串等非结构化数据、复杂数组 |

**1. 基础构造**：适用于手动构建小规模数组或复制已有数据。

```python
import numpy as np
a = np.array([1, 2, 3])                    # 从列表创建一维数组
b = np.array([[1, 2], [3, 4]])             # 从嵌套列表创建二维数组
c = np.array([1, 2, 3], dtype=np.float64)  # 指定元素类型（dtype 作为参数）
d = np.copy(a)                             # copy：元素与原来相同，但是新数组（副本）
e = np.array([1, 2, 3]).copy()             # 或使用成员方法 copy()
```

**2. 预定义形状填充**：用于快速初始化固定形状的数组（如全0占位、全1初始化）。

```python
np.zeros((2, 3))     # 全 0
np.ones((3, 2))      # 全 1
np.empty((2, 2))     # 未初始化（内容为随机内存值，速度快）
np.full((2, 2), 7)   # 填充指定数值 7
np.zeros_like(arr)   # 复制参数的形状，值全为 0（还有 ones_like / full_like / empty_like）
```

**3. 基于数值范围生成**：生成数值序列，常用于模拟时间序列、坐标网格等。

```python
np.arange(1, 10, 2)      # np.arange(start, end, step) 左闭右开 => [1 3 5 7 9]
np.linspace(0, 100, 5, dtype=np.int64)  # start, end, 个数 => [0 25 50 75 100]
np.logspace(0, 4, 2, base=2)            # 对数间隔：start, end, 个数, base=底数（默认10）
np.meshgrid(x, y)        # 坐标网格（配合 arange/linspace 生成）
```

**4. 特殊矩阵生成**：数学运算专用（如线性代数中的单位矩阵）。

```python
np.eye(3)                  # 单位矩阵：主对角线为1，其余为0
np.eye(5, dtype=np.int64)  # 可指定类型
np.identity(3)             # 单位矩阵（等价）
np.diag([1, 2, 3, 4])      # 对角矩阵：主对角线为非0，其余为0
np.zeros((3, 3)) + np.triu(np.ones((3, 3)))  # 上三角矩阵等特殊结构
```

**5. 随机数组生成**：模拟实验数据、初始化神经网络权重等场景。

```python
rng = np.random.default_rng(seed=42)  # 现代推荐写法，可复现
rng.random((2, 3))      # [0, 1) 均匀分布
rng.normal(0, 1, (2, 3))# 正态分布
rng.integers(0, 10, (3, 3))  # 随机整数

# 传统写法（旧教程/老代码常见）
np.random.rand(3, 4)             # [0,1) 均匀随机浮点数，(行,列)
np.random.uniform(3, 6, (2, 3))  # 指定区间 [3,6) 的均匀浮点数
np.random.randint(3, 60, (2, 3)) # 指定区间 [3,60) 的随机整数
np.random.randn(3, 4)            # 标准正态分布（两边小，中间大）
np.random.seed(20)               # 设置随机种子：之后每次生成的数字一致
np.random.randint(1, 10, (2, 5))
```

**6. 高级构造方法**：处理非结构化数据（如文件、字符串）或通过函数生成复杂数组。

```python
np.loadtxt("data.csv", delimiter=",")     # 从文本文件读取
np.frombuffer(b'...', dtype=np.uint8)     # 从二进制缓冲区创建
np.fromiter(range(5), dtype=int)          # 从迭代器创建
np.fromfunction(lambda i, j: i + j, (3, 3))  # 通过函数创建
```

#### 2.4 ndarray的数据类型

| 数据类型 | 说明 |
|--------|------|
| bool | 布尔类型 |
| int8、uint8 | 有符号、无符号的8位（1字节）整型 |
| int16、uint16 | 有符号、无符号的16位（2字节）整型 |
| int32、uint32 | 有符号、无符号的32位（4字节）整型 |
| int64、uint64 | 有符号、无符号的64位（8字节）整型 |
| float16 | 半精度浮点型 |
| float32 | 单精度浮点型 |
| float64 | 双精度浮点型 |
| complex64 | 用两个32位浮点数表示的复数 |
| complex128 | 用两个64位浮点数表示的复数 |

**四大类归纳**：布尔类型 `bool`、整数类型 `int` / `uint`、浮点数 `float`、复数 `complex`。

```python
# bool 类型：true or false
arr = np.array([1, 0, 1, 0, 0], dtype=bool)
print(arr)          # [ True False  True False False]
print(arr.dtype)    # bool
```

#### 2.5 索引与切片

| 索引/切片类型     | 描述/用法                                 |
| ----------- | ------------------------------------- |
| 基本索引        | 通过整数索引直接访问元素。索引从0开始。                  |
| 行/列切片       | 使用冒号`:`切片语法选择行或列的子集。                  |
| 连续切片        | 从起始索引到结束索引按步长切片。                      |
| 使用 slice 函数 | 通过 `slice(start, stop, step)` 定义切片规则。 |
| 布尔索引        | 通过布尔条件筛选满足条件的元素。支持逻辑运算符 `&`、\|。       |

**一维数组的索引与切片**

```python
arr = np.random.randint(1, 100, 20)
print(arr[0])           # 索引访问第一个元素（索引从0开始）
print(arr[:])           # 获取全部元素
print(arr[2:5])         # 切片 [left, right) 左闭右开
print(arr[slice(2, 5)]) # slice(start, end, step) 切片方法
print(arr[arr > 10])    # 布尔索引：筛选满足条件的元素
print(arr[(arr > 10) & (arr < 70)])  # 布尔索引 + 逻辑与
```

**二维数组的索引与切片**

```python
arr = np.random.randint(1, 100, (4, 8))
print(arr[0])           # 第1行
print(arr[0, :])        # 第1行（等价写法）
print(arr[1, 2:5])      # 第2行的第3~5列
print(arr[1, slice(2, 5)])
print(arr[arr > 50])    # 二维数组布尔索引：返回的是一维数组
print(arr[2][arr[2] > 50])  # 对指定行做布尔索引
```

#### 2.6 ndarray的运算

**算术运算**

```python
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(a + b)    # [3 5 7]
print(a - b)    # [-1 -1 -1]
print(a * b)    # [2 6 12] 逐元素相乘（不是矩阵乘法）
print(a ** 2)   # [1 4 9]

c = [1, 2, 3]
d = [4, 5, 6]
print(c + d)    # 列表相加是拼接 [1, 2, 3, 4, 5, 6]，与数组不同

# 数组与标量的运算：广播到每个元素
print(a + 2)    # [3 4 5]

# 二维数组之间的算术运算
a = np.array([[1, 3, 4], [2, 3, 4], [4, 5, 6]])
b = np.array([[2, 3, 4], [6, 7, 8], [0, 2, 4]])
print(a + b)
print(a - b)
print(a * b)
print(a ** 2)
```

**广播机制（Broadcasting）—— 重点**

> 同一维度下：形状**相同**即可运算；或对应维度的**行或列有一个是 1**，可以自动扩展广播。

```python
a = np.array([1, 2, 3])        # 1*3
b = np.array([[4], [5], [6]])  # 3*1
print(a + b)
# 结果等价于：
# 4 5 6     4 4 4
# 5 6 7  =  5 5 5
# 6 7 8     6 6 6

# 错误案例：1*2 与 1*3，两个维度都不为1且不相同，无法广播
a = np.array([1, 2])        # 1*2
b = np.array([[4, 5, 6]])   # 1*3
print(a + b)   # ValueError: operands could not be broadcast
```

**矩阵运算**

```python
a = np.array([[1, 3, 4], [2, 3, 4], [4, 5, 6]])
b = np.array([[2, 3, 4], [6, 7, 8], [0, 2, 4]])
print(a * b)    # 数组相乘：对应位置元素相乘
print(a @ b)    # 矩阵乘法（线性代数中的乘法运算）
```

**题目 3：矩阵运算**（来自 Numpy学习.ipynb）

> 给定矩阵 A = [[1, 2], [3, 4]] 和 B = [[5, 6], [7, 8]]：
> - 计算 A + B 和 A * B（逐元素乘法）
> - 计算 A 和 B 的矩阵乘法（点积）

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A + B)   # 逐元素加法
print(A * B)   # 逐元素乘法
print(A @ B)   # 矩阵乘法（点积）

# 结果：
# A + B ==  [[ 6  8]
#            [10 12]]
# A * B ==  [[ 5 12]
#            [21 32]]
# A @ B ==  [[19 22]
#            [43 50]]
```

## 3. Numpy常用函数

### 3.1 基本数学函数

| 函数 | 作用 |
|------|------|
| `np.sqrt(x)` | 计算平方根 |
| `np.exp(x)` | 计算指数（e^x） |
| `np.log(x)` | 计算自然对数 |
| `np.sin(x)` | 计算正弦值 |
| `np.abs(x)` | 计算绝对值 |
| `np.power(a, b)` | 幂运算，a 的 b 次方 |
| `np.round(x, n)` | 四舍五入（银行家规则） |

```python
import numpy as np

# 平方根
print(np.sqrt(9))           # 3.0
print(np.sqrt([1, 4, 9]))   # [1. 2. 3.]
arr = np.array([1, 25, 81])
print(np.sqrt(arr))

# 指数：e 的 x 次方
print(np.exp(9))

# 自然对数：以 e 为底
print(np.log(2.71))

# 三角函数
print(np.sin(-1))
print(np.cos(np.pi))

# 绝对值
arr = np.array([1, -2, 3, -4])
print(np.abs(arr))

# 幂运算：a 的 b 次幂
print(np.power(arr, 2))

# 四舍五入（银行家规则）
print(np.round([3.2, 4.5, 8.1, 9.6]))

# 向上取整 / 向下取整
arr = np.array([1.6, 25.1, 81.7])
print(np.ceil(arr))    # 向上取整
print(np.floor(arr))   # 向下取整

# 检测缺失值 NaN
print(np.isnan([1, 2, 3, np.nan]))   # [False False False  True]
```

### 3.2 统计函数

| 函数 | 作用 |
|------|------|
| `np.sum(x)` | 求和 |
| `np.mean(x)` | 求均值 |
| `np.average(x)` | 加权平均值（与 mean 的另一种求均值方式） |
| `np.median(x)` | 求中位数 |
| `np.std(x)` | 求标准差 |
| `np.var(x)` | 求方差 |
| `np.min(x)` / `np.max(x)` | 求最小值 / 最大值 |
| `np.argmin(x)` / `np.argmax(x)` | 求最小值 / 最大值的索引 |
| `np.percentile(x, q)` | 求第 q 百分位数 |
| `np.cumsum(x)` | 累积和（前 n 项之和） |
| `np.cumprod(x)` | 累积积（前 n 项之积） |

```python
# 求和
arr = np.random.randint(1, 20, 8)
print(np.sum(arr))

# 求平均值（mean 和 average，后者是加权平均值）
print(np.mean(arr))

# 求中位数：从小到大排序，然后选取中间的数字
# 偶数个数：中间两个数的平均值；奇数个数：排序后中间的数
print(np.median(arr))

# 求方差、标准差（平均值相同，方差越小越稳定）
print(np.var([1, 2, 100]))   # 方差
print(np.std([1, 2, 100]))   # 标准差

# 求最值：max 和 argmax、min 和 argmin（arg 系列返回索引）
print(f"最大值：{np.max(arr)},最大值索引：{np.argmax(arr)}")
print(f"最小值：{np.min(arr)},最小值索引：{np.argmin(arr)}")
```

**axis 参数（轴）：0 表示列，1 表示行**

```python
np.random.seed(0)
arr = np.random.randint(0, 10, [3, 4])   # 3行4列
print(arr)
print(f"每列的最大值：{np.max(arr, axis=0)}")
print(f"每行的最小值：{np.min(arr, axis=1)}")
```

**分位数（百分位数）**：`np.percentile(arr, q)` 计算第 q 百分位。

```python
np.random.seed(0)
arr = np.random.randint(1, 20, 4)
print(arr)                       # [13 16  1  4] （排序后 1 4 13 16）
print(np.percentile(arr, 25))    # 3.25
print(np.percentile(arr, 80))    # 14.2

# 计算原理（以 80% 分位为例）：
# 1. 先计算一共多少个区间：n - 1 = 3
# 2. 80% 分位位置 = 0.8 * 3 = 2.4，位于第2~3个区间内（13 ~ 16 之间）
# 3. 用 (16 - 13) * 0.4 = 1.2（0.4 是 2.4 的小数部分）
# 4. 再用 13 + 1.2 = 14.2 得到 80% 分位数
```

**累积和、累积积**

```python
arr = np.array([1, 3, 4, 5, 7])
print(np.sum(arr))      # 20
print(np.cumsum(arr))   # [ 1  4  8 13 20]  前n项的和，例如arr[1]是第0项和第1项的和
print(np.cumprod(arr))  # [ 1  3 12 60 420]  前n项的积
```

**题目 1：温度数据分析**（来自 Numpy学习.ipynb）

> 某城市一周的最高气温℃为 [28, 30, 29, 31, 32, 30, 29]。
> - 计算平均气温，最高气温和最低气温
> - 找出气温超过30℃的天数

```python
arr = np.array([28, 30, 29, 31, 32, 30, 29])
print(f"平均气温是：{np.round(np.mean(arr),1)}，最高气温是：{np.max(arr)}，最低气温是：{np.min(arr)}")
print(f"气温超过30℃的天数为：{np.size(arr[arr>30])}")
```

**题目 2：学生成绩统计**（来自 Numpy学习.ipynb）

> 某班级 5 名学生的数学成绩为 [85,90,78,92,88]。
> - 计算成绩的平均分、中位数和标准差
> - 将成绩转换为十分制（假设满分为 10）

```python
arr = np.array([58,90,78,92,88])
print(f"平均分为：{np.mean(arr)}，中位数为：{np.median(arr)}，标准差为：{np.std(arr)}")
print(arr / 10)   # 十分制
```

**题目 7：统计函数应用**（来自 Numpy学习.ipynb）

> 某公司 6 个月的销售额（万元）为 [120, 135, 110, 125, 130, 140]。
> - 计算销售额的总和、均值和方差
> - 找出销售额最高的月份和最低的月份

```python
arr = np.array([120, 135, 110, 125, 130, 140])
print(f"销售额的总和：{np.sum(arr)}，均值：{np.mean(arr)}，方差：{arr.var()}")
print(f"销售额最高的月份：{np.argmax(arr)+1}，最低的月份：{arr.argmin()+1}")
```

**综合应用：利润分析**（来自 Numpy学习.ipynb）

> 某商店 5 天的销售额（万元）和成本（万元）如下：销售额 [20, 25, 22, 30, 28]，成本 [15, 18, 16, 22, 20]。
> - 计算每天的利润（销售额 - 成本）
> - 计算利润的平均值和标准差
> - 找出利润最高的天数

```python
smoney = np.array([20, 25, 22, 30, 28])
money = np.array([15, 18, 16, 22, 20])
lirun = smoney - money
print(f"每天的利润：{lirun}，利润的平均值：{lirun.mean()}，标准差：{lirun.std()}")
print(f"利润最高的天数为：{len(lirun[lirun==np.max(lirun)])}")
```

### 3.3 比较函数

| 函数 | 作用 |
|------|------|
| `np.greater(a, b)` | 判断 a > b，返回布尔数组 |
| `np.less(a, b)` | 判断 a < b，返回布尔数组 |
| `np.equal(a, b)` | 判断 a == b，返回布尔数组 |
| `np.logical_and(a, b)` | 逻辑与运算（逐元素） |
| `np.logical_not(a)` | 逻辑非运算（逐元素） |
| `np.logical_or(a, b)` | 逻辑或运算（逐元素） |
| `np.any(x)` | 检查数组中是否至少有一个 True |
| `np.all(x)` | 检查数组中是否全部为 True |
| `np.where(condition, x, y)` | 自定义条件：满足条件取 x，否则取 y |
| `np.select(conditions, choices, default)` | 多条件选择（条件缺一不可） |

**比较是否大于、小于、等于**

```python
# 是否大于（与小）于某个值
print(np.greater([1, 2, 3, 4, 5], 2))
print(np.less([1, 2, 3, 4, 5], 3))
# 是否等于（单个值 / 两个数组按相应索引对照）
print(np.equal([1, 3, 4, 5], 3))
print(np.equal([1, 3, 4, 5], [1, 2, 3, 5]))
```

**逻辑与、或、非**

```python
# 逻辑与（逐元素，第一个元素和第一个元素逻辑运算，容易混淆）
print(np.logical_and([1, 0], [1, 1]))
# 逻辑非
print(np.logical_not([1, 0]))
# 逻辑或
print(np.logical_or([0, 0], [0, 1]))
```

**检查数组中是否至少有一个为 True / 全部为 True**

```python
print(np.any([0, 0, 0, 0, 0]))   # False
print(np.all([0, 1, 1, 0, 0]))   # False
# 其中 np.where(条件, 符合条件的值, 不符合条件的值)
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.where(arr > 3, arr, 0))    # [0 0 0 4 5 6]
```

**np.where 实现多级判断（嵌套）+ np.select**

```python
score = np.random.randint(50, 101, 20)
print(score)
print(np.where(score > 60, "及格", "不及格"))

# 嵌套 where 实现多条件：
# score<60 不及格，score<80 良好，否则 优秀
print(np.where(
    score < 60, "不及格", np.where(
        score < 80, "良好", "优秀"
    )
))
# np.select(条件, 返回的结果, default="默认值") — 条件缺一不可，否则报错
print(np.select([score<60, (score<=80)&(score>=60), score>80],
                ["不及格", "良好", "优秀"], default="未知"))
```

**题目 4：随机数据生成**（来自 Numpy学习.ipynb）

> 生成一个 (3, 4) 的随机整数数组，范围 [0, 10)。
> - 计算每列的最大值和每行的最小值
> - 将数组中的所有奇数替换为 -1

```python
np.random.seed(0)
arr = np.random.randint(0, 10, [3, 4])
print(arr)
print(f"每列的最大值：{np.max(arr, axis=0)}")   # axis参数表示轴，0表示列，1表示行
print(f"每行的最小值：{np.min(arr, axis=1)}")
print(np.where(arr % 2 == 1, -1, arr))
```

**题目 6：找出数组中大于 10 的元素**（来自 Numpy学习.ipynb）

> 生成一个 (5, 5) 的随机数组，范围 [0, 20]。
> - 找出数组中大于 10 的元素
> - 将所有大于 10 的元素替换为 0

```python
np.random.seed(0)
arr = np.random.randint(0, 20, [5, 5])
print(arr)
print(arr[arr > 10])                     # 布尔索引筛选
print(np.where(arr > 10, 0, arr))        # 替换
```

### 3.4 去重函数

| 函数 | 作用 |
|------|------|
| `np.unique(x)` | 返回去重后的唯一值 |
| `np.in1d(a, b)` | 判断 a 中元素是否存在于 b 中 |

```python
np.random.seed(0)
arr = np.random.randint(1, 100, 20)
print(arr)
print(np.unique(arr))    # 去重 + 排序（不改变原数组）

# return_counts=True：同时返回每个唯一值出现的次数
unique, counts = np.unique(arr, return_counts=True)
print(unique, "\n", counts)
```

**题目 9：唯一值与排序**（来自 Numpy学习.ipynb）

> 给定数组 [2, 1, 2, 3, 1, 4, 3]。
> - 找出数组中的唯一值并排序
> - 计算每个唯一值出现的次数

```python
arr = np.array([2, 1, 2, 3, 1, 4, 3])
unique, counts = np.unique(arr, return_counts=True)
print(unique, "\n", counts)
```

### 3.5 其他函数

| 函数 | 作用 |
|------|------|
| `np.concatenate((a, b))` | 沿指定轴拼接数组 |
| `np.split(x, indices)` | 按索引分割数组 |
| `np.reshape(x, shape)` | 修改数组形状（不改变数据） |
| `np.copy(x)` | 复制数组（返回副本而非视图） |
| `np.isnan(x)` | 判断是否为 NaN |

```python
# 数组的拼接
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.concatenate((arr1, arr2)))    # 水平拼接

# 数组的分割
np.random.seed(0)
arr = np.random.randint(1, 100, 20)
print(np.split(arr, 4))               # 平均份数，份数必须能被整除，否则报错
print(np.split(arr, [6, 12, 18]))     # 切割位置索引，切三刀分成四段

# 调整数组形状（reshape）
print(np.reshape(arr, [4, 5]))        # 1维 -> 二维
arr2d = np.reshape(arr, [4, 5])
print(arr2d.reshape(20))              # 成员方法，二维数组展平为一维
```

**题目 5：数组变形**（来自 Numpy学习.ipynb）

> 创建一个 1 到 12 的一维数组，并转换为 (3, 4) 的二维数组。
> - 计算每行的和与每列的平均值
> - 将数组展开为一维数组

```python
arr = np.arange(1, 13, 1)
print(arr)                          # [ 1  2  3  4  5  6  7  8  9 10 11 12]
new_arr = np.reshape(arr, [3, 4])
print(new_arr)
print(f"每行的和：{np.sum(new_arr, axis=1)}")
print(f"每列的平均值：{np.mean(new_arr, axis=0)}")
print(new_arr.reshape(12))          # 展平回一维
```

**题目 8：数组拼接**（来自 Numpy学习.ipynb）

> 给定 A = [1, 2, 3] 和 B = [4, 5, 6]。
> - 将 A 和 B 水平拼接为一个新数组
> - 将拼接后的数组垂直变形

```python
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.concatenate((A, B))   # 水平拼接
print(C)                     # [1 2 3 4 5 6]
print(C.reshape(2, 3))       # 变形为 2行3列
```

### 3.6 排序函数

| 函数 | 作用 |
|------|------|
| `np.sort(x)` | 返回排序后的新数组（原数组不变） |
| `x.sort()` | 原地排序（直接修改原数组） |
| `np.argsort(x)` | 返回排序后的索引 |
| `np.lexsort(keys)` | 按多键字典序排序 |

```python
np.random.seed(0)
arr = np.random.randint(1, 100, 20)
print(arr)
# print(arr.sort())    # 直接改变原数组（原地排序）
print(np.sort(arr))    # 不改变原数组，生成一个排好序的新数组
print(np.argsort(arr)) # 不改变原数组，生成该数组排好序的索引（可用于索引回原数组）
print(arr)             # 原数组不变
```

---

## 【Numpy 缺失知识点清单】

> 对照 numpy 完整知识体系，以下内容目前笔记中**尚未涉及/缺失**（**仅清单展示，未补全**，后续学完自行整理后再处理）：

### 一、数组视图与内存机制
- 视图（View）vs 副本（Copy）：切片返回的是视图（共享内存），修改会互相影响
- `ndarray.view()`、`ndarray.base`、`arr.copy()` 深拷贝的真正区别
- 内存布局：`strides`（步长）、C 顺序（行优先）与 F 顺序（列优先）、`np.ascontiguousarray`

### 二、高级索引
- 整数数组索引（Fancy Indexing）：`arr[[0, 2, 3]]`、`np.take`、`np.compress`
- `np.nonzero`、`np.argwhere`、`np.where(cond)` 单参数返回索引
- 省略号 `...` 与 `np.newaxis`（增/降维索引）
- `np.isclose` / `np.allclose`（浮点精度比较）

### 三、形状与组合操作
- `np.expand_dims` / `np.squeeze`
- `np.ravel` / `np.flatten`（及两者视图 vs 副本的区别）
- `np.hstack` / `np.vstack` / `np.stack` / `np.dstack`
- `np.tile` / `np.repeat`
- `np.resize`（与 reshape 的区别）
- `np.broadcast_to` 显式广播

### 四、线性代数进阶（np.linalg）
- `np.dot` / `np.inner` / `np.outer`（@ 之外的乘法家族）
- `np.linalg.inv` 逆矩阵、`np.linalg.det` 行列式
- `np.linalg.eig` 特征值 / 特征向量
- `np.linalg.solve` 求解线性方程组
- `np.linalg.norm` 范数、`np.linalg.svd` 奇异值分解、`np.linalg.qr`

### 五、傅里叶变换
- `np.fft` 模块：`np.fft.fft`、`np.fft.ifft`、`np.fft.fftfreq`（介绍中提到但未展开）

### 六、统计与聚合补充
- NaN 忽略版本：`np.nanmean`、`np.nansum`、`np.nanmax`、`np.nanstd` 等
- `np.clip`（裁剪数值范围）
- `np.diff`（差分）、`np.gradient`（梯度）
- `np.prod`（乘积）、`np.sum(x, axis=)` 的 axis 进阶用法

### 七、随机模块补充（np.random）
- `np.random.choice`（从数组中随机抽取，可带权重）
- `np.random.shuffle` / `np.random.permutation`（打乱数组）
- 更多分布：`np.random.exponential`、`np.random.binomial`、`np.random.poisson` 等
- `np.random.default_rng()` 的完整方法集（permutation、choice、shuffle 等，目前笔记只用到 random/normal/integers）

### 八、文件与 I/O
- 二进制存取：`np.save`、`np.load`、`np.savez`（`.npy` / `.npz` 格式）
- `np.savetxt`（文本导出）
- `np.genfromtxt`（更灵活，可处理缺失值）

### 九、特殊数组类型
- 掩码数组 `np.ma.MaskedArray`（处理缺失/无效数据）
- 结构化数组（dtype 定义字段，混合类型数据）
- `np.datetime64` / `np.timedelta64`（时间日期类型）

### 十、字符串数组
- `np.char` 模块（向量化字符串操作：`upper`、`split`、`replace` 等）

### 十一、性能与向量化
- ufunc 机制：`reduce`、`accumulate`、`outer` 等聚合方法
- `out=` 参数原地写入，避免内存副本
- `np.einsum`（爱因斯坦求和，高级张量运算）
- 向量化思想：避免 Python 循环（如列表推导）的低效做法