# 案例1：函数名 → 对象
def get_sum(a,b):
    return a + b

print(get_sum) # <function get_sum at 0x000001E9B8C1F430>
print(get_sum(10,20)) # 调用函数，获取返回值 30

# 案例2: 演示闭包写法.
# 需求: 定义求和的闭包, 外部函数有参数num1, 内部函数有参数num2, 调用, 求解两数之和, 观察结果.

# 1. 定义外部函数
def fun_outer(num1):    
    # 2. 定义内部函数
    def fun_inner(num2): # 有嵌套
        # 3. 求和
        sum = num1 + num2 # 有引用
        print(f'求和结果：{sum}')
    # 4. 返回内部函数名
    return fun_inner    # 5. 调用外部函数, 获取内部函数名，不能加括号，有返回

# 6. 调用外部函数, 获取内部函数名
fn_inner = fun_outer(10)
fn_inner(20) # 30

print('-' * 23)

fun_outer(100)(200)