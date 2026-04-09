# 导入os模块，用来获取当前文件的路径
import os

# 1. 获取当前Python文件所在的文件夹路径
current_dir = os.path.dirname(__file__)
# 2. 拼接出test.txt的完整路径（自动适配系统，Windows/Mac都能用）
file_path = os.path.join(current_dir, "test.txt")

# 3. 用拼接好的路径打开文件，加utf-8解决中文乱码
with open(file_path, encoding="utf-8") as f:
    content = f.read()
    print(content)