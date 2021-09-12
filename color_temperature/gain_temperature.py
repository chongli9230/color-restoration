import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
pi = np.pi

# 模拟生成一组实验数据
x = np.arange(0, 100, 0.2)      #R 通道 数据
y = np.exp(-x / 51.3)    # 色温值 
noise = np.random.uniform(0, 0.1, len(x))
y += noise
fig, ax = plt.subplots()
ax.plot(x, y, 'b--')


# 拟合指数曲线
def target_func(x, a0, a1, a2):
    return a0 * np.exp(-x / a1) + a2


a0 = max(y) - min(y)
a1 = x[round(len(x) / 2)]
a2 = min(y)
p0 = [a0, a1, a2]
print(p0)
para, cov = optimize.curve_fit(target_func, x, y, p0=p0)
print(para)
y_fit = [target_func(a, *para) for a in x]
ax.plot(x, y_fit, 'g')

plt.show()


