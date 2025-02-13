from PIL import Image, ImageOps


def IMG_correct(img):
    img = Image.open(img)
    # 图片扩展
    img = ImageOps.expand(img, (200, 200, 200, 200))

    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    # Img.save("test1.jpg")

    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    threshold = 200

    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)

    # 图片二值化
    photo = Img.point(table, '1')
    # photo.save("test2.jpg")

    return photo


if __name__ == '__main__':
    img = IMG_correct('ocr_box.png')
    img.show()
