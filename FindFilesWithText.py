import os
import re


def find_files_with_text(directory, text_to_find):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 或者你可以根据需要修改文件类型
            if file.endswith('.json'):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    contents = f.read()
                    if re.search(text_to_find, contents):
                        print(os.path.join(root, file))


# 使用函数
find_files_with_text("../../document/百峰网后台备份", "2023年台山市部分事业单位公开招聘工作人员")
