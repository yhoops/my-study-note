"""
案例：演示自定义迭代器.

迭代器介绍：
    概述：
        自定义的类，只要写了__iter__()和__next__()方法，那么这个类就是一个迭代器。
    目的：
        隐藏底层逻辑，让用户使用更方便.
        惰性加载，使用的时候才会获取.
"""

# 需求：模拟range(1,6)，自定义迭代器实现同等逻辑.
# 场景1：回顾range用法
for i in range(1, 6):
    print(i)
print("-" * 23)


# 场景2：自定义迭代器.
# 1. 自定义迭代器类
class MyIterator:
    # 通过__init__()方法，初始化属性，指定：范围.
    def __init__(self, start, end):
        self.current_value = start  # 当前值默认为开始值
        self.end = end

    # 3. 重写iter()方法，返回迭代器对象本身.
    def __iter__(self):
        return self

    # 4. 重写next()魔法方法，返回当前值，并更新当前值.
    def __next__(self):
        # 4.1 判断当前值范围是否合法.
        if self.current_value >= self.end:
            raise StopIteration  # 抛出异常，迭代结束
        # 4.2 走这里，说明当前值合法，返回当前值并更新
        # value = self.current_value
        # self.current_value += 1
        # return value

        # 效果同上，代码更简
        self.current_value += 1
        return self.current_value - 1


# 5. 创建迭代器对象，并遍历.
for i in MyIterator(1, 6):
    print(i)
print("-" * 23)

# 5.1 next()函数
my_iter = MyIterator(10, 13)
# next()方法是获取指针元素后一位
print(next(my_iter))  # 10
print(next(my_iter))  # 11
print(next(my_iter))  # 12
print(next(my_iter))  # 抛出异常
