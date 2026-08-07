
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
np.fromfunction(lambda i, j: i + j, (3, 3))  # 通过函数生成
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


## 3. Numpy常用函数

### 3.1 **基本数学函数**

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

### 3.2 **统计函数**

| 函数 | 作用 |
|------|------|
| `np.sum(x)` | 求和 |
| `np.mean(x)` | 求均值 |
| `np.median(x)` | 求中位数 |
| `np.std(x)` | 求标准差 |
| `np.var(x)` | 求方差 |
| `np.min(x)` / `np.max(x)` | 求最小值 / 最大值 |
| `np.percentile(x, q)` | 求第 q 百分位数 |

### 3.3 **比较函数**

| 函数 | 作用 |
|------|------|
| `np.greater(a, b)` | 判断 a > b，返回布尔数组 |
| `np.less(a, b)` | 判断 a < b，返回布尔数组 |
| `np.equal(a, b)` | 判断 a == b，返回布尔数组 |
| `np.logical_and(a, b)` | 逻辑与运算 |
| `np.where(condition, x, y)` | 满足条件取 x，否则取 y |

### 3.4 **去重函数**

| 函数 | 作用 |
|------|------|
| `np.unique(x)` | 返回去重后的唯一值 |
| `np.in1d(a, b)` | 判断 a 中元素是否存在于 b 中 |

### 3.5 **其他函数**

| 函数 | 作用 |
|------|------|
| `np.concatenate((a, b))` | 沿指定轴拼接数组 |
| `np.split(x, indices)` | 按索引分割数组 |
| `np.reshape(x, shape)` | 修改数组形状（不改变数据） |
| `np.copy(x)` | 复制数组（返回副本而非视图） |
| `np.isnan(x)` | 判断是否为 NaN |

### 3.6 **排序函数**

| 函数 | 作用 |
|------|------|
| `np.sort(x)` | 返回排序后的新数组（原数组不变） |
| `x.sort()` | 原地排序（直接修改原数组） |
| `np.argsort(x)` | 返回排序后的索引 |
| `np.lexsort(keys)` | 按多键字典序排序 |



