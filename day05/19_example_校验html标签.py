"""
()      代表 分组，从左往右数，第几个左小括号(，就表示第几组，可以获取指定分组的信息
\num    代表 引用第几组的内容.

扩展：
    (?P<分组名>正则表达式)    设置分组
    (?P=分组名)               使用分组
"""

import re

# 需求1：校验html的单级标签
# 1. 定义变量，记录：html标签.
html_s = "<html>我是html页面</html>"  # 规则：字母数：1 ~ 4

# 2. 匹配校验.
# 写法1：重新copy一份.
result = re.match("^<[a-zA-z]{1,4}>.*</[a-zA-z]{1,4}>$", html_s)
# 写法2：引入分组的概念.
result = re.match(
    r"^<([a-zA-z]{1,4})>.*</\1>$", html_s
)  # \1 表示引用第1组    前面要加r 避免python转义和正则引擎的冲突


# 3. 打印结果
print(result.group() if result else "匹配失败")


# 需求2：校验html的单级标签
# 1. 定义变量，记录：html标签.
html_s = "<html><h1>我是html页面</h1></html>"  # 规则：字母数：1 ~ 4，标题标签1 ~ 6

# 2. 匹配校验.
# 思路1：/ 后面重新copy 一份前面的内容
result = re.match(r"<[a-zA-Z]{1,4}><h[1,6]>.*</h[1,6]></[a-zA-Z]{1,4}>", html_s)
# 思路2：引入分组的概念.
result = re.match(r"<([a-zA-Z]{1,4})><(h[1,6])>.*</\2></\1>", html_s)
# 写法3：给分组起名.
result = re.match(r"<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1,6])>.*</(?P=B)></(?P=A)>", html_s)


# 3. 打印结果
print(result.group() if result else "匹配失败")
