#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理GESP Scratch题目，按级别分类PDF文件
"""

import os
import re
import shutil

def extract_level_from_filename(filename):
    """从文件名中提取级别信息"""
    # 匹配数字级别
    match = re.search(r'(图形化编程|Scratch)[^\d]*?(\d+)级', filename)
    if match:
        return int(match.group(2))
    # 匹配一级、二级等中文级别
    match = re.search(r'(图形化编程|Scratch)[^一-九]*?(一|二|三|四)级', filename)
    if match:
        level_map = {'一': 1, '二': 2, '三': 3, '四': 4}
        return level_map.get(match.group(2), 0)
    return 0

def main():
    """主函数"""
    pdf_dir = "./gesp_pdfs"
    
    # 保存结果
    output_dir = "./scratch_questions"
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历所有PDF文件
    for filename in os.listdir(pdf_dir):
        if "图形化编程" in filename and filename.endswith(".pdf"):
            level = extract_level_from_filename(filename)
            if level > 0:
                # 为每个级别创建一个目录
                level_dir = os.path.join(output_dir, f"level_{level}")
                os.makedirs(level_dir, exist_ok=True)
                
                # 复制PDF文件到对应级别目录
                src_path = os.path.join(pdf_dir, filename)
                dst_path = os.path.join(level_dir, filename)
                
                print(f"复制文件: {filename} -> level_{level}/{filename}")
                shutil.copy2(src_path, dst_path)
    
    print("处理完成！PDF文件按级别分类保存到 scratch_questions 目录中。")

if __name__ == "__main__":
    main()