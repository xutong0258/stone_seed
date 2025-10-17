import cv2
import numpy as np


def remove_mouse_pointer_by_pixel(img):
    height, width, _ = img.shape
    center_x, center_y = width // 2, height // 2
    half_size = 10

    # OpenCV 使用 BGR 格式，红色为 [0, 0, 255]
    # img[center_y - half_size:center_y + half_size,
    #     center_x - half_size:center_x + half_size] = [0, 0, 255]

    mouse_y = height - 213
    img[mouse_y - half_size:mouse_y + half_size,
    width - half_size:width + half_size] = [18, 19, 15]

    # 保存结果
    cv2.imwrite('result_no_mouse.jpg', img)

    return

if __name__ == '__main__':
    # 读取图片
    img = cv2.imread('1.jpg')
    remove_mouse_pointer_by_pixel(img)