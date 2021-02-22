"""
    常用算法：
    穷举法
    贪婪法
    分治法
    回溯法
    动态规划
"""
"""穷举法"""
#公鸡五元一只，母鸡三元一只，小鸡一元三只，用一百元买100只鸡 问公鸡/母鸡/小鸡各多少只

def 穷举法():
    for x in range(20):
        for y in range(33):
            z = 100-x-y
            if (5*x+3*y+z):
                print(x,y,z)



