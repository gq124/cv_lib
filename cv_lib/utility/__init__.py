# -*- coding: utf-8 -*-
from utility.file_path_utility import combine_file_path

__author__ = 'l'
__date__ = '2018/5/17'
"""
工具类
"""

import cv2 as cv


def clip_img(img, start, end):
    """
    裁剪图片
    :param img:ndarray格式的图片
    :param start: 起始位置:左上角点
    :param end: 结束位置：右下角点
    :return:
    """
    new_img = img[start[0]:end[0], start[1]:end[1], :]
    return new_img


def show_img(new_img):
    """
    显示图片
    :param new_img:
    :return:
    """
    cv.imshow("Image", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def load_img_to_gray(img):
    """
    转变成灰度图片
    :param img:
    :return:
    """
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


if __name__ == '__main__':
    # path = combine_file_path('data/img/1.png')
    # im = load_img_to_numpy(path)
    # new_im = clip_img(im, (200, 200), (424, 424))
    # # show_img(new_im)
    # gray_im = load_img_to_gray(im)
    # show_img(gray_im)
    pass
