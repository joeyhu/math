'''
计数排序法，对序列比较集中，重复值较多时对的排序非常有效，：
1.知道或统计出待排序数组的元素的最大值和最小值
2.创建一个最大值和最小值差+1的数组，从小到大的统计每个值出现的次数
3.迭代每个值，及重复的次数放到一个新数组中，就完成了排序

'''
import numpy as np


class CountingSort:
    def sort(self, x, min, max):
        l = len(x)
        b = [0 for i in range(max - min + 1)]
        for i in range(l):
            j = x[i] - min
            b[j] += 1
        c = [0 for i in range(l)]
        ji = 0
        for k in range(len(b)):
            for bIndex in range(b[k]):
                c[ji] = min + k
                ji += 1
        return c


def main():
    min, max = 0, 100
    x = np.random.randint(min, max, 20)
    print(x)
    re = CountingSort().sort(x, min, max)
    print('After sort: ', re)


if __name__ == '__main__':
    main()
