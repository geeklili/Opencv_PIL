from PIL import Image, ImageDraw

import face_recognition

# 首先我们导入需要的依赖包，第一个导入的包为图像处理库，第二个为人脸识别的API
image = face_recognition.load_image_file("./data/123.jpg")

face_landmarks = face_recognition.face_landmarks(image)[0]
print(face_landmarks)

# 我们先将image.jpg加载成一个numpy数组，然后让其被API人脸识别库识别。其中image.jpg为需要PS恶搞的图片，当然可以是你的闺蜜或者基友啦！

pil_image = Image.fromarray(image)
for i in dir(pil_image):
    print(i)

d = ImageDraw.Draw(pil_image, 'RGBA')
print(pil_image.size)
pil_image.resize((360, 640))
print(pil_image.show())

# 遍历所有的先前定义的numpy数组，查看里面所有的脸，并让图片处理库（PIL）对其进行恶搞绘画。

d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))

d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))

d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)

d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

# 我们首先识别库会识别眼镜，并对人脸的眉毛进行一场噩梦级别的绘画，里面的参数可以自调。

d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))

d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))

d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)

d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

# 光滑人脸的嘴唇，参数可自调。

d.polygon(face_landmarks['left_eye'], fill=(0, 0, 0, 0))

d.polygon(face_landmarks['right_eye'], fill=(0, 0, 0, 0))

# 闪耀Ta的12K氪金狗眼，发散出母牛发情般的光芒……（此处省略10000字）

d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)

d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

# 图上迷人的眼线，项目对男人慎用……

pil_image.show()
pil_image.save('./data/234.jpg')

# 最后显示恶搞图像
