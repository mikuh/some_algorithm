"""
划分土地算法
将一块地 划分成尽量大的等大小方块
运用了递归和分治策略
例如：
输入 1680, 640
输出 80, 80
"""


def devide(width, height):
    if width == height:
        return (width, height)
    elif width > height:
        return devide(width - height, height)
    else:
        return devide(width, height - width)



if __name__ == '__main__':
    result = devide(1680, 640)
    print(result)
