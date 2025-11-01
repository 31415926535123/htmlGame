#!/usr/bin/env python3
"""
图标生成器 - 根据输入图片自动生成多种尺寸的图标
支持常见图标尺寸：16x16, 32x32, 48x48, 64x64, 128x128, 256x256, 512x512
"""

import os
import sys
from PIL import Image, ImageOps
import argparse


def generate_icons(input_path, output_dir="icons", sizes=None):
    """
    生成多种尺寸的图标
    
    Args:
        input_path: 输入图片路径
        output_dir: 输出目录
        sizes: 要生成的尺寸列表，默认为常见图标尺寸
    """
    if sizes is None:
        sizes = [16, 32, 48, 64, 128, 256, 512]
    
    try:
        # 打开原始图片
        with Image.open(input_path) as img:
            # 转换为RGBA模式以支持透明度
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # 创建输出目录
            os.makedirs(output_dir, exist_ok=True)
            
            print(f"正在处理图片: {input_path}")
            print(f"原始尺寸: {img.size}")
            print(f"输出目录: {output_dir}")
            print("-" * 40)
            
            # 生成各种尺寸的图标
            for size in sizes:
                # 使用高质量缩放算法
                resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
                
                # 生成文件名
                base_name = os.path.splitext(os.path.basename(input_path))[0]
                output_filename = f"{base_name}_{size}x{size}.png"
                output_path = os.path.join(output_dir, output_filename)
                
                # 保存图片
                resized_img.save(output_path, "PNG", optimize=True)
                print(f"✓ 生成 {output_filename}")
            
            # 生成ICO文件（Windows图标）
            ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            ico_path = os.path.join(output_dir, f"{base_name}.ico")
            img.save(ico_path, format="ICO", sizes=ico_sizes)
            print(f"✓ 生成 {base_name}.ico")
            
            print("-" * 40)
            print(f"完成！共生成 {len(sizes) + 1} 个文件")
            
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"错误：{e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="根据输入图片生成多种尺寸的图标")
    parser.add_argument("input", help="输入图片路径")
    parser.add_argument("-o", "--output", default="icons", help="输出目录 (默认: icons)")
    parser.add_argument("-s", "--sizes", nargs="+", type=int, 
                       help="指定要生成的尺寸列表 (例如: 16 32 48 64)")
    
    args = parser.parse_args()
    
    # 验证输入文件
    if not os.path.exists(args.input):
        print(f"错误：文件 '{args.input}' 不存在")
        sys.exit(1)
    
    # 生成图标
    generate_icons(args.input, args.output, args.sizes)


if __name__ == "__main__":
    main()