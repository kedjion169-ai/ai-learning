import os

# 1. 直接写死文件夹路径（复制你的路径过来，解决找不到文件的问题）
# 注意：Windows路径里的反斜杠 \ 要改成正斜杠 / 或者加 r 前缀
folder_path = r"C:\Users\19428\Desktop\ME\ai-learning\tools\rename-test" 

# 2. 设置规则
prefix = "我的文件_"
start_num = 1
exclude_list = ["batch-rename.py", "README.md"] # 排除脚本自己

# 3. 遍历文件
print("开始扫描文件夹...")
for filename in os.listdir(folder_path):
    print(f"发现文件：{filename}") # 打印所有发现的文件
    
    # 跳过排除项
    if filename in exclude_list:
        continue
    
    # 拼接完整路径
    file_path = os.path.join(folder_path, filename)
    
    # 只处理文件
    if os.path.isfile(file_path):
        # 分离名字和后缀
        file_name, file_ext = os.path.splitext(filename)
        
        # 生成新名字
        new_name = f"{prefix}{start_num:03d}{file_ext}"
        new_path = os.path.join(folder_path, new_name)
        
        # 执行重命名
        os.rename(file_path, new_path)
        print(f"✅ 已重命名：{filename} -> {new_name}")
        start_num += 1

print("\n🎉 批量重命名完成！总处理数：", start_num - 1)