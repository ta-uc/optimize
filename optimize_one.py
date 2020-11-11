from objective_function import f_1, d_f_1, d_2_f_1
import matplotlib.pyplot as plt
import numpy as np

# グラフの設定
xa = []
xb = []
ya = []
yb = []
x = [i/100 for i in range(-200,200)]
y = [f_1(i/100) for i in range(-200,200)]
z = [d_f_1(i/100) for i in range(-200,200)]
plt.ylim(-10,10)
plt.plot(x, y)

def search(f, d_f):
  # 収束判定用
  e = 0.001

  # 移動幅の初期値
  h = 0.5
  
  # 初期点
  x = 0.5

  while abs(d_f(x)) > e:

    # 点の移動方向の決定
    if d_f(x) > 0:
      h = abs(h)
    elif d_f(x) < 0:
      h = -1 * abs(h)
    
    X = x
    X_d = x + h

    # X と X_h の間に最大値をとる点が来るまで移動する
    if f(X) < f(X_d):
      while f(X) < f(X_d):
        # グラフ用
        xa.append(X)
        ya.append(f(X))

        h = 2*h
        X = X_d
        X_d = X + h
      x = X
      h = h / 2

    else:
      # X と X_h　間に最大値があるので間隔を狭めていく
      while f(X) > f(X_d):
        # グラフ用
        xa.append(X)
        ya.append(f(X))

        h = h / 2
        X_d = X_d - h
      x = X_d
      h = 2 * h

  return x

def newton(f, d_f, d_2_f):
  # 初期点
  x = -1.2

  # 収束判定用
  delta = 0.001

  while True:
    x_d = x
    # グラフ用
    xb.append(x)
    yb.append(f(x))

    # 点の移動
    x = x_d - d_f(x_d) / d_2_f(x_d)

    if abs(x - x_d) < delta:
      break
  return x

# 勾配法で探す
print(search(f_1, d_f_1))
# ニュートン法で探す
print(newton(f_1, d_f_1, d_2_f_1))

# グラフの表示
plt.plot(xa, ya)
plt.plot(xb, yb)
plt.scatter([xa[-1]], [ya[-1]],color="r")
plt.scatter([xb[-1]], [yb[-1]],color="b")
plt.show()