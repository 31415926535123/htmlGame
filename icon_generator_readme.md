# 图标生成器使用说明

## 安装依赖
```bash
pip install -r requirements.txt
```

## 基本用法

### 1. 使用默认设置生成图标
```bash
python icon_generator.py input.png
```
默认会生成以下尺寸的PNG图标和一个ICO文件：
- 16x16, 32x32, 48x48, 64x64, 128x128, 256x256, 512x512

### 2. 指定输出目录
```bash
python icon_generator.py input.png -o my_icons
```

### 3. 自定义尺寸
```bash
python icon_generator.py input.png -s 16 24 32 48 64 128 256
```

### 4. 完整参数示例
```bash
python icon_generator.py input.png -o output_folder -s 16 32 48 64 128 256 512
```

## 支持的输入格式
- PNG, JPEG, BMP, GIF, TIFF等PIL支持的格式

## 输出文件
- PNG格式：`原文件名_尺寸x尺寸.png`
- ICO格式：`原文件名.ico`（包含多种尺寸）

## 特性
- 高质量缩放（LANCZOS算法）
- 自动处理透明度
- 保持宽高比
- 生成Windows兼容的ICO文件

## 示例
假设你有一个 `logo.png` 文件：
```bash
python icon_generator.py logo.png
```
输出：
```
icons/logo_16x16.png
icons/logo_32x32.png
icons/logo_48x48.png
icons/logo_64x64.png
icons/logo_128x128.png
icons/logo_256x256.png
icons/logo_512x512.png
icons/logo.ico
```