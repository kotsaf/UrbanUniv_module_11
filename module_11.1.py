import requests
from PIL import Image

'''REQUESTS'''
URL = 'https://urban-university.ru/'
URL2 = 'https://smartiqa.ru'

request = requests.request(url=URL, method='get')       # запрос на сайт
print(request)
#вывод - 403 (доступ запрещен)

response = requests.request(url=URL2, method='get')     # заголовки сайта
print(response.headers)



'''PILLOW'''
image = 'image.jpg'
with Image.open(image) as img: # чтение
    img.load()                 # чтение в память
    #img.show()                 # отображение
    print(img.format)          # JPEG - формат
    print(img.size)            # (736, 552) - размер
    print(img.mode)            # RGB - цветовой режим

    img = img.crop((300, 150, 700, 500))    # обрезка
    img_resized = img.resize((img.width // 4, img.height // 4))    # тоже обрезка но другим способом

    img = img.convert("L")          # преобразование из RGB (цветное) в L (серое)

    img.save('image1.png')      # сохранение изображения в другом формате



image = 'image1.png'
with Image.open(image) as img:  # чтение
    img.load()  # чтение в память
    print(img.format)  # PNG - формат
    print(img.size)    # (400, 350) - размер
    print(img.mode)    # L - цветовой режим
