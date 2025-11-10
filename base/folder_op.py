import shutil
import os
from base.fileOP import *
from base.logger import *

BASEDIR = os.path.dirname(__file__)

def delete_folder(folder_path):
    try:
        # 检查文件夹是否存在
        if not os.path.exists(folder_path):
            logger.info(f"错误: 文件夹 '{folder_path}' 不存在")
            return
            
        # 检查是否是文件夹
        if not os.path.isdir(folder_path):
            logger.info(f"错误: '{folder_path}' 不是一个文件夹")
            return
            
        # 删除文件夹及其内容
        shutil.rmtree(folder_path)
        logger.info(f"文件夹 '{folder_path}' 已成功删除")
        
    except PermissionError:
        logger.info(f"错误: 没有权限删除 '{folder_path}'")
    except Exception as e:
        logger.info(f"删除文件夹时发生错误: {str(e)}")

def create_folder(folder_path):
    try:
        # 检查文件夹是否已存在
        if not os.path.exists(folder_path):
            # 创建文件夹，parents=True表示如果父目录不存在也会一起创建
            os.makedirs(folder_path, exist_ok=True)
            logger.info(f"文件夹创建成功: {folder_path}")
            return True
        else:
            logger.info(f"文件夹已存在: {folder_path}")
            return True
    except PermissionError:
        logger.info(f"权限错误: 无法在 {folder_path} 创建文件夹，请检查权限")
    except OSError as e:
        logger.info(f"创建文件夹时发生错误: {e}")
    return False

def copy_single_file(src_path, dest_path, overwrite=True):
    try:
        # 检查源文件是否存在
        if not os.path.isfile(src_path):
            logger.info(f"错误: 源文件不存在 - {src_path}")
            return False

        # 处理目标路径，如果是目录则保留原文件名
        if os.path.isdir(dest_path):
            file_name = os.path.basename(src_path)
            dest_path = os.path.join(dest_path, file_name)

        # # 检查目标文件是否存在
        # if os.path.exists(dest_path) and not overwrite:
        #     logger.info(f"错误: 目标文件已存在，未进行覆盖 - {dest_path}")
        #     return False

        # 复制文件
        shutil.copy2(src_path, dest_path)  # copy2会保留文件元数据
        logger.info(f"文件复制成功: {src_path} -> {dest_path}")
        return True

    except PermissionError:
        logger.info(f"错误: 权限不足，无法复制文件 - {src_path}")
    except Exception as e:
        logger.info(f"复制文件时发生错误: {str(e)}")
    return False

def copy_multiple_files(src_files, dest_dir, overwrite=False):
    success_count = 0
    fail_count = 0

    # 确保目标目录存在
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
            logger.info(f"创建目标目录: {dest_dir}")
        except Exception as e:
            logger.info(f"无法创建目标目录: {str(e)}")
            return (0, len(src_files))

    # 逐个复制文件
    for file_path in src_files:
        if copy_single_file(file_path, dest_dir, overwrite):
            success_count += 1
        else:
            fail_count += 1

    logger.info(f"批量复制完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    return (success_count, fail_count)

# 使用示例
if __name__ == "__main__":
    # 要删除的文件夹路径
    folder_path = r'D:\0_LOG_VIP\Result_10_28'
    post_report_process(folder_path)
