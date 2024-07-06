# sudo add-apt-repository ppa:alex-p/tesseract-ocr5
# sudo apt update
# sudo apt install tesseract-ocr  tesseract-ocr-ara
# https://github.com/tesseract-ocr/tesseract

from pdf2image import convert_from_path
import pytesseract

pdf_path = 'test.pdf'
images = convert_from_path(pdf_path)

language = 'ara'

for i, image in enumerate(images):
    temp_image_path = f'temp_image_{i + 1}.png'
    image.save(temp_image_path, 'PNG')
    text = pytesseract.image_to_string(temp_image_path, lang=language)
    text_file_path = f'output_page_{i + 1}.txt'
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print(f"Page {i + 1} Arabic text written to {text_file_path}")
