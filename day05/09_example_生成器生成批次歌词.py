"""
案例：基于传入的数值(每批次的歌词条数)，创建生成器，生成批次歌词.


1. 生成器的概念？
    根据一定规则生成数据的一种机制，每次调用生成器只生成一个值，可以节省大量内存.
    next(generater) next 函数获取生成器的下一个值
    for 循环遍历生成器中的每一个值

2. 生成器的创建有两种方式？
    生成器推导式
    yield 关键字

"""

# 导入 math 模块：用于 math.ceil() 向上取整，计算歌词按 batch_size 分批后的总批次数
# （总条数不能被整除时，最后不足一批的剩余歌词也要单独算作一个批次，所以向上取整）
import math


# 需求：基于文件中周杰伦的歌词，创建生成器，根据传入的歌词条数，生成批次歌词.
# 1. 定义函数，接收 每批次的歌词条数，返回生成器.
def dataset_loader(batch_size):
    """
    自定义的歌词批量生成器
    :param batch_size: 每批次的歌词条数
    :return: 生成，每个元素都是一批次的数据，例如：(8条,8条，8条，8条，8条，8条，8条，8条)
    """

    # 1.1 读取文件数据
    with open("day05\data\jay_lyrics.txt", "r", encoding="utf-8") as f:
        # 1.2 一次读取所有行.
        lines = [line.strip() for line in f.readlines()]

        # 1.3 计算批次.
        total_batch = math.ceil(len(lines) / batch_size)

        # 1.4 for循环方式，获取到每批次的数据，放到生成器中，并返回.
        for idx in range(total_batch):
            # 第1批格式，批次索引(idx = 0)，歌词为：第1条到第8条，索引为0~7
            yield lines[idx * batch_size : idx * batch_size + batch_size]


# 2. 测试
if __name__ == "__main__":
    dl = dataset_loader(3)
    print(next(dl))
    print(next(dl))

    for batch_data in dl:
        print(batch_data)
