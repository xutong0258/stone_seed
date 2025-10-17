import os
import cv2
import numpy as np


def remove_mouse_pointer_opencv(image_path, template_path, output_path):
    # 读取图像和模板（鼠标指针图像）
    img = cv2.imread(image_path)
    template = cv2.imread(template_path)
    h, w, _ = template.shape

    # 模板匹配
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # 匹配阈值
    loc = np.where(res >= threshold)

    # r g b 15 19 18
    # 覆盖鼠标指针区域（用黑色填充）# B, G, R
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (18, 19, 15), -1)

        # 保存处理后的图像
    cv2.imwrite(output_path, img)

file_list = os.listdir('11')
template_image = "template.png"  # 鼠标指针的模板图像

for file in file_list:
    # 调用函数（需要准备鼠标指针的模板图像template.png ）
    output_image = f'12\\{file}'
    file = os.path.join(r'D:\00_stone_project\11', file)
    print(file)
    remove_mouse_pointer_opencv(file, template_image, output_image)
