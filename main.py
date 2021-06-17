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

