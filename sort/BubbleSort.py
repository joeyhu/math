"""
冒泡排序法
"""


class BubbleSort:
    def sort(self, x):
        l = len(x)
        for i in range(l):
            for j in range(i + 1, l):
                if x[i] > x[j]:
                    m = x[i]
                    x[i], x[j] = x[j], m


def main():
    x = [12, 3, 4, 11, 23, 44, 2, 6, 4]
    BubbleSort().sort(x)
    print(x)


if __name__ == "__main__":
    main()
