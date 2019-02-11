'''
取欧几里得摸
'''


class EuclideanNorm:
    def euclideanNorm(self, x):
        l = len(x)
        if l == 0:
            return None
        if l == 1:
            return x[0]
        s = 0
        for i in range(l):
            s += x[i] ** 2
        return s ** 0.5

    '''
    n维空间坐标系下的两点距离
    '''

    def euclideanNorm1(self, x, y):
        l = len(x)
        if l == 0:
            return None
        if l == 1:
            return x[0]
        s = 0
        for i in range(l):
            s += (x[i] - y[i]) ** 2
        return s ** 0.5

    '''
    在长方体区域进行聚类的时候，普通的距离计算公式无法满足需求，按照普通距离计算后进行聚类出的大多数是圆形区域，这时候需要采用标准化欧氏距离计算公式。
    标准欧氏距离的定义: 标准化欧氏距离是针对简单欧氏距离的缺点而作的一种改进方案。
    标准欧氏距离的思路：既然数据各维分量的分布不一样，好吧！那我先将各个分量都“标准化”到均值、方差相等吧。
    '''

    def standardizedEuclideandistance(self, a, b):
        sumnum = 0
        for i in range(len(a)):
            # 计算si 分量标准差
            avg = (a[i] - b[i]) / 2
            si = ((a[i] - avg) ** 2 + (b[i] - avg) ** 2) ** 0.5
            sumnum += ((a[i] - b[i]) / si) ** 2
        distance = (sumnum) ** 0.5
        return distance


def main():
    e = EuclideanNorm()
    re = e.euclideanNorm([3, 4])  # 三角形斜边
    print('Euclidean norm: ', re)
    re = e.euclideanNorm1([3, 4, 2], [5, 8, 7])
    print('Euclidean norm1: ', re)
    re = e.standardizedEuclideandistance([3, 4, 2], [5, 8, 7])
    print('Euclidean norm1: ', re)


if __name__ == '__main__':
    main()
