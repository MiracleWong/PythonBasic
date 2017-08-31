# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt

x_bar = [10, 20, 30, 40, 50] #柱形图横坐标
y_bar = [0.5, 0.6, 0.7, 0.4, 0.6] #柱形图纵坐标
bars = plt.bar(x_bar, y_bar, color='blue', label=x_bar, width=2)
for i,rect in enumerate(bars):
    x_text = rect.get_x()
    y_text = rect.get_height() + 0.01
    plt.text(x_text, y_text, '%.1f' % y_bar[i]) #标注文字

    # 增加箭头标注
    plt.annotate('Max', xy=(32, 0.6), xytext=(38, 0.6), arrowprops=dict(facecolor='black', width=1, headwidth=7))
plt.show()