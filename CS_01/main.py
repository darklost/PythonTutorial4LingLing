# -*- coding: utf-8 -*-
"""
Created on 2024-01-05 13:24:00
@author: D.K.
"""
import argparse
from pdf2docx import Converter

def main(pdf_file,docx_file):
    # Convert pdf to docx
    # 将pdf转换为docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    
if __name__ == "__main__":
    # Parse command line arguments
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    # Add arguments input pdf file path and output docx file path
    # 添加参数输入pdf文件路径和输出docx文件路径
    parser.add_argument("--pdf_file",type=str)
    parser.add_argument('--docx_file',type=str)
    # Parse arguments
    # 解析参数
    args = parser.parse_args()
    # Call main function
    # 调用主函数
    main(args.pdf_file,args.docx_file)