'''
识别手写数字
'''
import numpy
import skimage.data
import sys


# conv_函数是卷积具体的实现代码
def conv_(img, conv_filter):
    filter_size = conv_filter.shape[1]
    result = numpy.zeros((img.shape))
    # Looping through the image to apply the convolution operation.
    for r in numpy.uint16(numpy.arange(filter_size / 2.0,
                                       img.shape[0] - filter_size / 2.0 + 1)):
        for c in numpy.uint16(numpy.arange(filter_size / 2.0,
                                           img.shape[1] - filter_size / 2.0 + 1)):
            """
            Getting the current region to get multiplied with the filter.
            How to loop through the image and get the region based on 
            the image and filer sizes is the most tricky part of convolution.
            """
            curr_region = img[r - numpy.uint16(numpy.floor(filter_size / 2.0)):r + numpy.uint16(
                numpy.ceil(filter_size / 2.0)),
                          c - numpy.uint16(numpy.floor(filter_size / 2.0)):c + numpy.uint16(
                              numpy.ceil(filter_size / 2.0))]
            # Element-wise multipliplication between the current region and the filter.
            curr_result = curr_region * conv_filter  # 在图像区域矩阵和滤波器之间对位相乘
            # 并将结果求和以得到单值输出
            conv_sum = numpy.sum(curr_result)  # Summing the result of multiplication.
            result[r, c] = conv_sum  # Saving the summation in the convolution layer feature map.

    # Clipping the outliers of the result matrix.
    final_result = result[numpy.uint16(filter_size / 2.0):result.shape[0] - numpy.uint16(filter_size / 2.0),
                   numpy.uint16(filter_size / 2.0):result.shape[1] - numpy.uint16(filter_size / 2.0)]
    return final_result


def conv(img, conv_filter):
    # 首先确保每个滤波器的深度等于图像通道的数目，代码如下。if语句首先检查图像与滤波器是否有一个深度通道，若存在，则检查其通道数是否相等，如果匹配不成功，则报错
    if len(img.shape) > 2 or len(conv_filter.shape) > 3:  # Check if number of image channels matches the filter depth.
        if img.shape[-1] != conv_filter.shape[-1]:
            print("Error: Number of channels in both image and filter must match.")
            sys.exit()
    # 滤波器的大小应该是奇数，且每个滤波器的大小是相等的。这是根据下面两个if条件语块来检查的。如果条件不满足，则程序报错并退出
    if conv_filter.shape[1] != conv_filter.shape[2]:  # Check if filter dimensions are equal.
        print('Error: Filter must be a square matrix. I.e. number of rows and columns must match.')
        sys.exit()

    if conv_filter.shape[1] % 2 == 0:  # Check if filter diemnsions are odd.
        print('Error: Filter must have an odd size. I.e. number of rows and columns must be odd.')
        sys.exit()

    # 通过初始化一个数组来作为滤波器的值，通过下面代码来指定滤波器的值：
    feature_maps = numpy.zeros((img.shape[0] - conv_filter.shape[1] + 1,
                                img.shape[1] - conv_filter.shape[1] + 1,
                                conv_filter.shape[0]))

    # Convolving the image by the filter(s).
    # 开始通过滤波器进行卷积，由于没有设置步幅（stride）或填充（padding），默认为步幅设置为1，无填充。那么卷积操作后得到的特征图大小为（img_rows-filter_rows+1, image_columns-filter_columns+1, num_filters），即输入图像的尺寸减去滤波器的尺寸后再加1。注意到，每个滤波器都会输出一个特征图
    for filter_num in range(conv_filter.shape[0]):
        print("Filter ", filter_num + 1)
        # 循环遍历滤波器组中的每个滤波器后，通过下面代码更新滤波器的状态：
        curr_filter = conv_filter[filter_num, :]  # getting a filter from the bank.
        """ 
        Checking if there are mutliple channels for the single filter.
        If so, then each channel will convolve the image.
        The result of all convolutions are summed to return a single feature map.
        
        如果输入图像不止一个通道，则滤波器必须具有同样的通道数目。只有这样，卷积过程才能正常进行。最后将每个滤波器的输出求和作为输出特征图。下面的代码检测输入图像的通道数，如果图像只有一个通道，那么一次卷积即可完成整个过程
        """
        if len(curr_filter.shape) > 2:
            conv_map = conv_(img[:, :, 0], curr_filter[:, :, 0])  # Array holding the sum of all feature maps.
            for ch_num in range(1, curr_filter.shape[
                -1]):  # Convolving each channel with the image and summing the results.
                conv_map = conv_map + conv_(img[:, :, ch_num],
                                            curr_filter[:, :, ch_num])
        else:  # 单通道就不需要循环进行卷积 There is just a single channel in the filter.
            conv_map = conv_(img, curr_filter)
        feature_maps[:, :, filter_num] = conv_map  # Holding feature map with the current filter.
    return feature_maps  # Returning all feature maps.


'''
池化层，用于
'''


def pooling(feature_map, size=2, stride=2):
    # Preparing the output of the pooling operation.
    pool_out = numpy.zeros((numpy.uint16((feature_map.shape[0] - size + 1) / stride + 1),
                            numpy.uint16((feature_map.shape[1] - size + 1) / stride + 1),
                            feature_map.shape[-1]))
    for map_num in range(feature_map.shape[-1]):
        r2 = 0
        for r in numpy.arange(0, feature_map.shape[0] - size + 1, stride):
            c2 = 0
            for c in numpy.arange(0, feature_map.shape[1] - size + 1, stride):
                pool_out[r2, c2, map_num] = numpy.max([feature_map[r:r + size, c:c + size, map_num]])
                c2 = c2 + 1
            r2 = r2 + 1
    return pool_out


'''
ReLU激活层,用于将线性输出结果，重新激活
'''


def relu(feature_map):
    # Preparing the output of the ReLU activation function.
    relu_out = numpy.zeros(feature_map.shape)
    for map_num in range(feature_map.shape[-1]):
        for r in numpy.arange(0, feature_map.shape[0]):
            for c in numpy.arange(0, feature_map.shape[1]):
                relu_out[r, c, map_num] = numpy.max([feature_map[r, c, map_num], 0])
    return relu_out


# Reading the image
img = skimage.data.chelsea()
# Converting the image into gray.
img = skimage.color.rgb2gray(img)
# 创建一个2维的滤波器，2个3x3的滤波器
l1_filter = numpy.zeros((2, 3, 3))
# 滤波器组的大小由自己指定，但没有给定滤波器中具体的数值，一般采用随机初始化。下列一组值可以用来检查垂直和水平边缘：
l1_filter[0, :, :] = numpy.array([[[-1, 0, 1],
                                   [-1, 0, 1],
                                   [-1, 0, 1]]])
l1_filter[1, :, :] = numpy.array([[[1, 1, 1],
                                   [0, 0, 0],
                                   [-1, -1, -1]]])

# 用滤波器对图像进行卷积，具体逻辑使用：conv方法
l1_feature_map = conv(img, l1_filter)
