"""
案例：演示编解码

细节：
    1. 编码 = 把我们看懂的 转成 我们看不懂的.
        '字符串'.encode('编码方式')
    2. 解码 = 把我们看不懂的 转成 我们看懂的.
        '字符串'.decode('编码方式')
    3. 只要乱码了，原因只有一个，编解码不同.
    4. 英文字母，数字，特殊符号无论什么码表都只占1个字节，中文在gbk中占2个字节，utf-8中占3个字节
    5. 二进制数据特殊写法，即：b'字母 数字 特殊符号'，中文不行
"""


# 需求1：编码
s1 = '黑马123abCD!@#'
print(s1.encode()) # b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(s1.encode('utf-8')) # b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(s1.encode('gbk')) # b'\xba\xda\xc2\xed123abCD!@#'

print('-' * 50)

# 需求2：解码
bytes = b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(type(bytes)) # <class 'bytes'>

s2 = bytes.decode('utf-8')
print(s2) # 黑马123abCD!@#

print('-' * 50)

# 需求3：编码和解码不同
s3 = bytes.decode('gbk')
print(s3) # 榛戦┈123abCD!@#