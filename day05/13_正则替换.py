"""
案例：演示正则替换.


回顾：正则的使用步骤
    1. 导包
        import re
    2. 正则匹配.
        result = re.match('正则表达式', '要校验的字符串')
        result = re.search('正则表达式', '要校验的字符串')
        result = re.compile('正则表达式').sub('替换后的内容', '要被替换的字符串')
    3. 获取匹配结果.
        result.group()
"""

# 导包
import re

# 1. 定义字符串
s = "开心你就大声笑，哈哈，嘿嘿，呵呵，嘻嘻，桀桀桀"

# 2. 把上述的 哈,嘿,嘻,桀 替换成 *
#                   正则规则    新字符串   要被替换的字符串
result = re.compile("哈|嘿|嘻|桀").sub("*", s)
# 3. 打印结果
print(result)

print("-" * 30)

# 新版API写法
# 参1：正则规则 参2：新字符串 参3：要被替换的字符串
result = re.sub("哈|嘿|嘻|桀", "♥", s)
print(result)
