"""
排序
"""

def 冒泡排序(arr, *, comp=lambda x, y: x <= y):
    # 从数组中取出全部的值
    items = arr[:]
    # 循环 1 到 数组长度 次
    for i in range(1, len(items)):
        # 定义调换的变量
        swapped = False
        # 遍历剩余的元素
        for y in range(i - 1, len(items) - i):
            if comp(items[y], items[y + 1]):
                # 调换元素
                items[y], items[y + 1] = items[y + 1], items[y]
                swapped = True
        if swapped:
            swapped = False
            for y in range(len(items) - i - 1, i - 1, -1):
                if comp(items[y - 1], items[y]):
                    items[y], items[y - 1] = items[y - 1], items[y]
                    swapped = True
        if not swapped:
            break
    return items





def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(冒泡排序(items))


if __name__ == '__main__':
    main()
