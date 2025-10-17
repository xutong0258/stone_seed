# 安装必要的库（如果尚未安装）
# !pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2
import os
import numpy as np

template_image = "template.png"  # 鼠标指针的模板图像

def remove_mouse_pointer_opencv(img, template_path):
    # 读取图像和模板（鼠标指针图像）
    # img = cv2.imread(image_path)
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

    return img

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
    return img


def detect_video(input_video_path, output_video_path=None):
    """
    使用YOLOv8n模型对视频进行目标检测

    参数:
        input_video_path: 输入视频的路径
        output_video_path: 输出视频的保存路径，若为None则不保存
    """
    # 检查输入视频文件是否存在
    if not os.path.exists(input_video_path):
        print(f"错误: 输入视频文件 '{input_video_path}' 不存在")
        return

    # 打开视频文件
    cap = cv2.VideoCapture(input_video_path)

    # 获取视频属性
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"视频信息: 宽度={frame_width}, 高度={frame_height}, FPS={fps}, 总帧数={total_frames}")

    # 初始化视频编写器（如果需要保存输出）
    out = None
    if output_video_path:
        # 获取输出目录并确保其存在
        output_dir = os.path.dirname(output_video_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 定义编解码器并创建VideoWriter对象
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 可以根据需要更改编解码器
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # 处理视频帧
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # 视频处理完毕

        frame_count += 1
        if frame_count % 10 == 0:  # 每10帧打印一次进度
            print(f"处理中: {frame_count}/{total_frames} 帧 ({frame_count / total_frames * 100:.1f}%)")

        annotated_frame = remove_mouse_pointer_opencv(frame, template_image)

        # 显示检测结果
        cv2.imshow('视频检测PS', annotated_frame)

        # 保存检测结果（如果需要）
        if out:
            out.write(annotated_frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("用户中断处理")
            break

    # 释放资源
    cap.release()
    if out:
        out.release()
    cv2.destroyAllWindows()
    print(f"处理完成，共处理 {frame_count} 帧")


if __name__ == "__main__":
    # 示例用法
    input_video = "11.mp4"  # 替换为你的输入视频路径
    output_video = "12.mp4"  # 替换为你的输出视频路径，或设为None不保存

    # 执行检测
    detect_video(
        input_video_path=input_video,
        output_video_path=output_video
    )
