import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# フォントをメイリオにする
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)

df_population_data = pd .read_csv("data.csv", encoding="shift-jis")
df_population_data_mean = df_population_data.groupby(by="都道府県名").mean()[["人口（総数）", "人口（男）", "人口（女）"]].round(1)
df_population_data_mean_sort =df_population_data_mean.sort_values(by="人口（総数）", ascending=False)


# 図の幅と高さをインチで指定する。※figsize パラメータのデフォルト値は [6.4、4.8]らしい。
plt.rcParams["figure.figsize"] = (9, 6)

# グラフを描く
df_population_data_mean_sort.plot()

plt.xlabel("x-lable：都道府県名", color="blue")
plt.ylabel("y-lable：人口")

# 軸の最大値・最小値の設定
plt.ylim(0, 10000000)
plt.yticks(np.arange(0, 10000001, step=1000000))

# 指数表記から普通の表記に変換
plt.ticklabel_format(style='plain', axis='y')

# y軸に補助目盛線を設定
plt.grid(which="major", axis="both", color="gray", alpha=0.5, linestyle="--", linewidth=1)

plt.show()