"""
()      代表 分组，从左往右数，第几个左小括号(，就表示第几组
\num    代表 引用第几组的内容.

扩展：
    (?P<分组名>)    设置分组
    (?P=分组名)     使用分组
"""

# 导包
import re

# 需求：在列表fruits = ['apple', 'banana', 'orange', 'pear'], 匹配 apple, pear
# 1. 定义水果列表
fruits = ["apple", "banana", "orange", "pear"]

# 2. 遍历，获取到每种水果
for fruit in fruits:
    # 3. 判断当前水果是否是喜欢吃的水果.
    # 参1：正则表达式.  参2：要校验的字符串.
    if re.match("apple|pear", fruit):
        # 4. 走这里，说明是喜欢吃的
        print(f"{fruit}是喜欢吃的水果")
    else:
        # 5. 走这里，说明不是喜欢吃的
        print(f"{fruit}不是喜欢吃的水果")
