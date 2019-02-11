'''
几何中夹角余弦可用来衡量两个向量方向的差异，机器学习中借用这一概念来衡量样本向量之间的差异。

1.二维空间向量的夹角余弦相似度
'''
import numpy as np


def cosn(a, b):
    """
    n维夹角余弦
    """
    sum1 = sum2 = sum3 = 0
    for i in range(len(a)):
        sum1 += a[i] * b[i]
        sum2 += a[i] ** 2
        sum3 += b[i] ** 2
    cos = sum1 / (np.sqrt(sum2) * np.sqrt(sum3))
    return cos


print('a,b 多维夹角余弦距离：', cosn((1, 1, 1, 1), (2, 2, 2, 2)))


def cosn2(a, b):
    """
    n维夹角余弦, 不使用循环
    """
    A, B = np.array(a), np.array(b)
    sum1 = sum(A * B)
    sum2 = np.sqrt(np.sum(A ** 2))
    sum3 = np.sqrt(np.sum(B ** 2))
    cos = sum1 / (sum2 * sum3)
    return cos


print('a,b 多维夹角余弦距离：', cosn2((1, 1, 1, 1), (2, 2, 2, 2)))

print('a,b 二维夹角余弦距离：', cosn((0, 2), (2, 0)))

print(np.pi / 3)
print(np.sin(np.pi / 3))
print(355 / 113)
