"""
()      代表 分组，从左往右数，第几个左小括号(，就表示第几组，可以获取指定分组的信息
\num    代表 引用第几组的内容.

扩展：
    (?P<分组名>)    设置分组
    (?P=分组名)     使用分组
"""

# 导包
import re

# 1. 定义邮箱
email = "abc123@163.com"

# 2. 校验邮箱是否合法.
result = re.match("^[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com$", email)

# 3. 打印结果
print(f"合法邮箱为：{result.group()}" if result else "邮箱不合法")
print(
    f"合法邮箱为：{result.group(0)}" if result else "邮箱不合法"
)  # 获取第0组的信息，效果同上
print(f"合法邮箱为：{result.group(1)}" if result else "邮箱不合法")  # 获取第1组的信息
