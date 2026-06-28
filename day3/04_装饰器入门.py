# 装饰器的作用是不改变原有函数的基础上，给原有函数增加额外功能.
# 装饰器本质上就是一个封包函数.

"""
装饰器构成条件    (特殊的闭包函数)
    1. 有嵌套
    2. 有引用
    3. 有返回
    4. 有额外功能
"""

"""
案例：装饰器入门

装饰器的用法：
    格式1：传统写法.
        装饰后的函数名 = 装饰器名(被装饰函数名)
        装饰后的函数名()    
    
    格式2：语法糖写法.
        在要被装饰的原函数上，直接写上 @装饰器名，之后直接调用原函数即可.
"""

# 需求：在发表评论前，都是需要先登录的.

# 1. 定义外部函数，形参列表接收要被装饰的函数名(对象)
def check_login(func):      # func：要被装饰的函数名(对象)
    # 1.1. 定义内部函数
    def fn_inner():         # 有嵌套.
        # 1.2 额外功能.
        print("校验登录中...，请稍后...，登录成功！")
        # 1.3 访问原函数：即外部函数的引用.
        func() #            # 有引用
    # 1.4 返回内部函数
    return fn_inner         # 有返回


# 2.定义函数，表示发表评论
def comment():
    print("发表评论")

@check_login
def payment():
    print("充值中...")

# 3.测试.
# 3.1 传统方式.
comment = check_login(comment)  # comment = fn_inner
comment()

print('-' * 30)

# 3.2 语法糖方式.
payment() # payment = fn_inner

class Student:
    @staticmethod   # 静态方法装饰器
    def show(self):
        print("我是静态方法")