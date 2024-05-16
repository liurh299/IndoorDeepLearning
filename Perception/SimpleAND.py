"""
Created on Sep 21, 2016
AND函数 与门的Python实现
"""


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x1 + w2 * x2
    if tmp > theta:
        return 1
    elif tmp <= theta:
        return 0


# 测试AND
out00 = AND(0, 0)
out01 = AND(0, 1)
out10 = AND(1, 0)
out11 = AND(1, 1)

print(out00)
print(out01)
print(out10)
print(out11)