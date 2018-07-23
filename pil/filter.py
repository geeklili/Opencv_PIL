# -*- coding: cp936 -*-
from PIL import Image, ImageDraw, ImageEnhance
from PIL import ImageFilter
import random, sys

img = Image.open("./data/123.jpg")
# 对比度增强
enh_con = ImageEnhance.Contrast(img)
contrast = 1.5
img_contrasted = enh_con.enhance(contrast)
img_contrasted.show()
# # 图像处理
# # 转换为RGB图像
img = img.convert("RGB")

# 经过PIL自带filter处理
img_b = img.filter(ImageFilter.BLUR)
img_c = img.filter(ImageFilter.CONTOUR)
img_ee = img.filter(ImageFilter.EDGE_ENHANCE)
img_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img_em = img.filter(ImageFilter.EMBOSS)
img_fe = img.filter(ImageFilter.FIND_EDGES)
img_sm = img.filter(ImageFilter.SMOOTH)
img_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
img_sh = img.filter(ImageFilter.SHARPEN)
img_d = img.filter(ImageFilter.DETAIL)

# 组合使用filter
group_imgfilted = img.filter(ImageFilter.CONTOUR)
group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)

# 图像保存
img_b.save("./data/f_b.jpg")
img_c.save("./data/f_c.jpg")
img_ee.save("./data/f_ee.jpg")
img_ee_m.save("./data/f_eem.jpg")
img_em.save("./data/f_em.jpg")
img_fe.save("./data/f_fe.jpg")
img_sm.save("./data/f_sm.jpg")
img_sm_m.save("./data/f_smm.jpg")
img_sh.save("./data/f_sh.jpg")
img_d.save("./data/f_d.jpg")
group_imgfilted.save("./data/f_group.jpg")

# 图像显示
img_b.show()
img_c.show()
img_ee.show()
img_ee_m.show()
img_em.show()
img_fe.show()
img_sm.show()
img_sm_m.show()
img_sh.show()
img_d.show()
group_imgfilted.show()

