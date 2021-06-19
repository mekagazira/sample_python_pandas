import pandas as pd

df_population_data = pd .read_csv("data.csv", encoding="shift-jis")

# データ型を確認
print(type(df_population_data))

# 最初から10rows表示
print(df_population_data.head(10))

# 最後から10rows表示
print(df_population_data.tail(10))

# ランダムに10rows表示
print(df_population_data.sample(10))

# データフレームの情報を取得する。
print(df_population_data.info())

# 要約統計量を取得する。
print(df_population_data.describe().round(1))

# 都道府県毎の平均（人口順）
df_population_data_mean = df_population_data.groupby(by="都道府県名").mean()[["人口（総数）", "人口（男）", "人口（女）"]].round(1)
print(df_population_data_mean.sort_values(by="人口（総数）", ascending=False))

# 特定のグループにどのようなデータが入った調べる
print(df_population_data.groupby(by="都道府県名").get_group("東京都"))

# 各グループのサイズを取得
print(df_population_data.groupby(by="都道府県名").size())
