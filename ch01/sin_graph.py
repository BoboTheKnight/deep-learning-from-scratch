# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.show()
