"""
^   表示开头
$   表示结尾
"""

# 需求1：校验字符串必须以数字开头，无论match(), 还是search()均是.   后面是啥无所谓.

# 导包
import re

# 正则匹配
result1 = re.match("\d+.*", "abc123xyz")
result2 = re.search("^\d+.*", "abc123xyz")  # 表示必须以数字开头

# 需求2：校验字符串必须以数字开头，以任意的3个字母结尾
result1 = re.match("^\d+.*[a-zA-Z]{3}$", "123xyz")
result2 = re.search("^\d+.*[a-zA-Z]{3}$", "123123xyz")

# 需求3：校验手机号.    规则：1.长度必须是11位.   2.必须是纯数字    3.第1位数字必须是1.     4.第2位数字可以是3-9
phone = re.match("^1[3-9]\d{9}$", "13012345678")


# 打印匹配结果
print(result1.group() if result1 else "匹配失败")
print(result2.group() if result2 else "匹配失败")
print(phone.group() if phone else "匹配失败")
