from objective_function import f_2, nabra_f_2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import sqrt

# グラフの設定
x = np.arange(-1.5, 1.5, 0.1)
y = np.arange(-1.5, 1.5, 0.1)
z = np.zeros( (x.size, y.size) )
for i in range(x.size):
  for j in range(y.size):
    z[i][j] = f_2([x[i],y[j]])
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, z)
plt.ylim(-1.5,1.5)
plt.xlim(-1.5,1.5)
plt.xlabel('x')
plt.ylabel('y')
search_x = []
search_y = []

# （収束判定用に）勾配の大きさを求める
def get_norm_descent(des):
  return sqrt(pow(des[0],2)+pow(des[1],2))

def search(f, nabra_f):
  e = 0e-10

  # 初期点
  xy = np.array([-1.0, -2.0])

  # 勾配とその大きさを求める
  descent = nabra_f(xy)
  norm_descent = get_norm_descent(descent)

  while norm_descent > e:
    # 点の移動幅の調節
    it = 0.1

    # 点の移動
    xy = xy + descent * it

    descent = nabra_f(xy)
    norm_descent = get_norm_descent(descent)

    # グラフ用
    search_x.append(xy[0])
    search_y.append(xy[1])
  return xy


# 最大値をとる点を求める
print(search(f_2, nabra_f_2))

# グラフの表示
ax.scatter(search_x,search_y,[10 for x in range(len(search_x))],color='r')
plt.show()