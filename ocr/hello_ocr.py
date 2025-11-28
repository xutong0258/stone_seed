import pytesseract
from PIL import Image

def extract_text_from_image(image_path, lang='eng'):
    """
    从图片中提取文字
    :param image_path: 图片路径（绝对路径或相对路径）
    :param lang: 语言（eng=英文，chi_sim=简体中文，chi_tra=繁体中文，可组合如 'eng+chi_sim'）
    :return: 提取的文字字符串
    """
    # 打开图片
    image = Image.open(image_path)
    
    # 若 Tesseract 未添加到环境变量，需手动指定引擎路径（Windows 示例）
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # 调用 Tesseract 提取文字
    text = pytesseract.image_to_string(image, lang=lang)
    
    # 清理空白字符（可选）
    text = text.strip().replace('\n', ' ').replace('\r', '')
    
    return text

# 示例：识别中文图片
if __name__ == "__main__":
    image_path = "./11.png"  # 你的图片路径
    extracted_text = extract_text_from_image(image_path, lang='eng')
    print("提取的文字：")
    print(extracted_text)
