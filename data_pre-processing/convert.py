from PIL import Image


def convert_to_black_and_white(image_path, output_path):
    # 打开图片文件
    with Image.open(image_path) as img:
        # 将图片转换为灰度（黑白）
        bw_img = img.convert('L')

        # 保存转换后的黑白图片
        bw_img.save(output_path)
        print(f"Black and white image saved as {output_path}")


# 使用函数将彩色图片转换为黑白图片
image_path = 'img.png'  # 替换为你的彩色图片路径
output_path = 'white_black.png'  # 替换为你想要保存的黑白图片路径
convert_to_black_and_white(image_path, output_path)
