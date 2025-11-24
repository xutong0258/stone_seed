from pathlib import Path
from utils.logger_util import *

# 当前工作目录
p = Path('.')
logger.info(f"Path : {p}")

# 绝对路径
p = Path('/home/user/documents')

# Windows 示例（自动处理斜杠）
p = Path('C:/Users/User/Documents')

# 使用路径拼接
p = Path.home() / 'documents' / 'file.txt'  # Path 重载了 / 运算符
logger.info(f"Path : {p}")

p = Path('/home/user/file.txt')

logger.info(p.name)       # 'file.txt'
logger.info(p.stem)       # 'file'（不含扩展名）
logger.info(p.suffix)     # '.txt'
logger.info(p.parent)     # '/home/user'
logger.info(p.parts)      # ('/', 'home', 'user', 'file.txt')
logger.info(p.absolute()) # 返回绝对路径

p = Path('example.txt')

is_exist = p.exists()     # 是否存在
logger.info(f"is_exist: {is_exist}")

p.is_file()    # 是否是文件
p.is_dir()     # 是否是目录
p.is_symlink() # 是否是符号链接

p = Path('new_folder')
p.mkdir(exist_ok=True)         # 创建目录（若存在也不报错）
p.mkdir(parents=True, exist_ok=True)  # 递归创建父目录

file = Path('temp.txt')
file.unlink()  # 删除文件

folder = Path('empty_folder')
folder.rmdir()  # 删除空目录
