"""
快速排序法
"""


class FastSort:
    def fsort(self, x, start, end):
        # 每次交换就将比对的方向交换一下,从左边为基准
        leftCheck = True
        i, j = start, end
        while i < j:
            if leftCheck:
                if x[i] > x[j]:
                    m = x[i]
                    x[i], x[j] = x[j], m
                    i += 1
                    leftCheck = False
                else:
                    j -= 1
            else:
                if x[i] < x[j]:
                    i += 1
                else:
                    m = x[i]
                    x[i], x[j] = x[j], m
                    leftCheck = True
                    j -= 1
        # 递归两边
        if i > 0:
            self.fsort(x, 0, i - 1)
        if i < end:
            self.fsort(x, i + 1, end)


def main():
    x = [12, 3, 4, 11, 23, 44, 2, 6, 4]
    FastSort().fsort(x, 0, len(x) - 1)
    print(x)


if __name__ == "__main__":
    main()
