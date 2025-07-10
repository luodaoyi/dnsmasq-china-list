#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
域名格式转换脚本
将 accelerated-domains.china.conf 从 dnsmasq 格式转换为纯域名列表格式
"""

import re
import os

def convert_dnsmasq_to_domain_list(input_file, output_file):
    """
    将 dnsmasq 配置文件转换为纯域名列表
    
    Args:
        input_file (str): 输入文件路径 (accelerated-domains.china.conf)
        output_file (str): 输出文件路径 (accelerated-domains.china.txt)
    """
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件 {input_file} 不存在")
        return False
    
    # 正则表达式匹配 server=/域名/DNS服务器 格式
    pattern = r'^server=/([^/]+)/.*$'
    
    domains = []
    processed_count = 0
    skipped_count = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # 跳过空行和注释行
                if not line or line.startswith('#'):
                    continue
                
                # 使用正则表达式提取域名
                match = re.match(pattern, line)
                if match:
                    domain = match.group(1)
                    domains.append(domain)
                    processed_count += 1
                else:
                    print(f"警告：第 {line_num} 行格式不匹配: {line}")
                    skipped_count += 1
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for domain in domains:
                f.write(domain + '\n')
        
        print(f"转换完成！")
        print(f"- 输入文件: {input_file}")
        print(f"- 输出文件: {output_file}")
        print(f"- 成功处理: {processed_count} 个域名")
        print(f"- 跳过行数: {skipped_count} 行")
        print(f"- 输出文件大小: {os.path.getsize(output_file)} 字节")
        
        return True
        
    except Exception as e:
        print(f"错误：处理文件时发生异常: {e}")
        return False

def main():
    """主函数"""
    input_file = "accelerated-domains.china.conf"
    output_file = "accelerated-domains.china.txt"
    
    print("开始转换域名格式...")
    print(f"从 {input_file} 转换到 {output_file}")
    print("-" * 50)
    
    success = convert_dnsmasq_to_domain_list(input_file, output_file)
    
    if success:
        print("-" * 50)
        print("转换成功完成！")
        
        # 显示输出文件的前几行作为示例
        print("\n输出文件前10行预览:")
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i >= 10:
                        break
                    print(f"  {line.strip()}")
        except Exception as e:
            print(f"无法预览输出文件: {e}")
    else:
        print("转换失败！")

if __name__ == "__main__":
    main()
