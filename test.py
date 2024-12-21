import os

WATCH_DIR = os.getcwd()  # 获取当前目录
filepath = os.path.join(WATCH_DIR, "readme.txt")

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        print(file.read())
else:
    print("File not found:", filepath)
