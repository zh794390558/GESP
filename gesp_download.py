#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GESP真题PDF下载脚本
功能：从GESP真题解析页面下载所有真题PDF文件
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 目标URL列表
BASE_URL = "https://gesp.ccf.org.cn"
TARGET_URLS = [
    "https://gesp.ccf.org.cn/101/1010/index_1.html",
    "https://gesp.ccf.org.cn/101/1010/index_2.html"
]

# 保存目录
SAVE_DIR = "gesp_pdfs"


def create_save_directory():
    """创建保存目录"""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"创建保存目录: {SAVE_DIR}")


def get_page_content(url: str) -> str:
    """获取网页内容"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.RequestException as e:
        print(f"获取页面 {url} 失败: {e}")
        return ""


def extract_exam_links(page_content: str, base_url: str) -> list:
    """提取考试链接"""
    exam_links = []
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # 查找所有链接，筛选出考试真题链接
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        text = a_tag.get_text(strip=True)
        
        # 筛选包含考试信息的链接
        if text and ('年' in text) and ('月' in text):
            full_url = urljoin(base_url, href)
            exam_links.append((full_url, text))
    
    return exam_links


def extract_pdf_links(page_content: str, base_url: str) -> list:
    """提取PDF链接"""
    pdf_links = []
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # 查找所有PDF链接
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        text = a_tag.get_text(strip=True)
        
        # 筛选PDF链接
        if href.endswith('.pdf'):
            full_url = urljoin(base_url, href)
            pdf_links.append((full_url, text))
    
    return pdf_links


def download_pdf(url: str, filename: str) -> bool:
    """下载PDF文件"""
    try:
        response = requests.get(url, timeout=60, stream=True)
        response.raise_for_status()
        
        # 清理文件名中的特殊字符
        filename = ''.join(c for c in filename if c.isalnum() or c in ' ._-')
        filepath = os.path.join(SAVE_DIR, f"{filename}.pdf")
        
        # 检查文件是否已存在
        if os.path.exists(filepath):
            print(f"文件已存在: {filepath}")
            return True
        
        # 下载文件
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"下载成功: {filepath}")
        return True
    except Exception as e:
        print(f"下载失败 {url}: {e}")
        return False


def main():
    """主函数"""
    create_save_directory()
    
    total_pdfs = 0
    
    # 遍历目标URL
    for target_url in TARGET_URLS:
        print(f"\n处理页面: {target_url}")
        
        # 获取页面内容
        page_content = get_page_content(target_url)
        if not page_content:
            continue
        
        # 提取考试链接
        exam_links = extract_exam_links(page_content, BASE_URL)
        print(f"找到 {len(exam_links)} 个考试链接")
        
        # 遍历考试链接
        for exam_url, exam_name in exam_links:
            print(f"\n处理考试: {exam_name}")
            
            # 获取考试页面内容
            exam_page_content = get_page_content(exam_url)
            if not exam_page_content:
                continue
            
            # 提取PDF链接
            pdf_links = extract_pdf_links(exam_page_content, BASE_URL)
            print(f"找到 {len(pdf_links)} 个PDF链接")
            
            # 下载PDF文件
            for pdf_url, pdf_name in pdf_links:
                # 构建完整的文件名，避免重复的日期信息
                # 移除exam_name中可能的重复日期部分
                clean_exam_name = exam_name.split('真题')[0] + '真题'
                # 移除可能的时间戳
                clean_exam_name = ''.join([c for c in clean_exam_name if not (c.isdigit() and len(c) == 8)])
                full_filename = f"{clean_exam_name} {pdf_name}"
                download_pdf(pdf_url, full_filename)
                total_pdfs += 1
    
    print(f"\n下载完成！总共处理了 {total_pdfs} 个PDF文件")


if __name__ == "__main__":
    main()