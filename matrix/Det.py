'''
计算矩阵的行列式
'''
import random


class Det:
    def det(self, a):
        l = len(a)
        if l == 0:
            return None
        if l == 1:
            return a[0][0]
        s = 0
        for x in range(l):
            k = []
            for y in range(l):
                if x != y:
                    k.append(a[y][1:])
            print(k)
            s += (-1) ** (x % 2) * a[x][0] * self.det(k)

        return (s)


def main():
    n = 2  # 方阵维数
    x = []
    for i in range(n):
        x.append(random.sample(range(10), n))
    print(x)
    re = Det().det(x)
    print('det: ', re)


if __name__ == '__main__':
    main()
