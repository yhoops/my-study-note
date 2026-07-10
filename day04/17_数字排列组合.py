"""
需求：
    问1，2，3，4能组合成的四位数有几种情况，控制5个一行输出。
要求：
    1. 同时包含1，2，3，4这四个数字.
    2. 要求1和3不能挨着
    3. 数字4不能开头
    4. 5行以内搞定(包括5行)
"""

from itertools import permutations

result = []
for p in permutations("1234"):
    s = "".join(p)
    if "13" not in s and s[0] != "4":
        result.append(s)

print(f"len(result) -> {len(result)}")

for i in range(0, len(result), 5):
    print(result[i : i + 5])


count = 0
for i in range(1234, 4322):
    s = str(i)
    if (
        "1" in s
        and "2" in s
        and "3" in s
        and "4" in s
        and "13" not in s
        and s[0] != "4"
    ):
        count += 1
        print(s, end="\n" if count % 5 == 0 else "\t")

print("\n" + "-" * 50)

# 第二题：已知列表：my_list=["aa","bb","cc","bb","bb","bb","dd"]，删除所有的"bb"元素，尽可能多的用不同的解决办法
# 思路1：
my_list = ["aa", "bb", "cc", "bb", "bb", "bb", "dd"]
new_list = [s for s in my_list if s != "bb"]
print(new_list)

# 思路2：
my_list = ["aa", "bb", "cc", "bb", "bb", "bb", "dd"]
for s in my_list[
    :
]:  # 复制了一份副本，遍历的是副本，但是修改的是原列表（切片的本质是浅拷贝）
    if s == "bb":
        my_list.remove(s)
print(my_list)
