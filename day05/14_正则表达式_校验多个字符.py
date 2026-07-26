"""
*       代表前边的内容 出现至少0次, 至多无数次
?       代表前边的内容 出现至少0次, 至多1次
+       代表前边的内容 出现至少1次, 至多无数次
{n}     代表前边的内容 恰好出现n次, 多一次,少一次都不行
{n,}    代表前边的内容 至少出现n次, 至多无数次
{n,m}   代表前边的内容 至少出现n次, 至多出现m次, 包左包右.
w - word    s - space   d - digital
"""

# 导包
import re

# 验证
result = re.match(".*heima.*", "hello heima world")  # 匹配成功
result = re.match(".+heima.*", "heima world")  # 匹配失败
# ? 0次或1次
result = re.match(".?heima.*", "heima world")  # 匹配成功
result = re.match(".?heima.*", "1heima world")  # 匹配成功
result = re.match(".?heima.*", "11heima world")  # 匹配失败
# {n} 恰好出现n次
result = re.match(r"\d{2}heima.*", "11heima world")  # 匹配成功

result = re.match(r"\d{3,}hm\w{2, 5}", "123hmabc")  # 失败，注意空格
result = re.match(r"\d{3,}hm\w{2,5}", "123hmabc")  # 匹配成功


# 查看结果
print(result.group() if result else "匹配失败")
