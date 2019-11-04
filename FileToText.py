import tesserocr as tc
from PIL import Image

'''
通过添加字体库支持新的语言和字体
C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\/tessdata/'
'''

class OcrTools:
    def __init__(self):
        demo  = ''

print(tc.tesseract_version())  # print tesseract-ocr version
print(tc.get_languages())  # prints tessdata path and list of available languages

filename = 'data/news.png'

en_filename = 'data/testp.png'

image = Image.open(filename)

#print(tc.image_to_text(image))  # print ocr text from image
# or
#标准中文图片
print('---------------------标准中文图片---------------------')
print(tc.file_to_text(filename,lang='chi_sim'))
#标准英文图片
print('---------------------标准英文图片---------------------')
print(tc.file_to_text(en_filename))