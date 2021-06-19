import pandas as pd

df_left = pd.DataFrame({
    'city': ['osaka', 'tokyo', 'kyoto'],
    'food': ['apple', 'orange', 'banana'],
})

df_right = pd.DataFrame({
    'city': ['osaka', 'tokyo', 'kyoto', 'kumamoto'],
    'price': [100, 200, 250, 300],
})

# 結合
print(pd.merge(df_left, df_right))

# 外部結合
print(pd.merge(df_left, df_right, how="outer"))

# データフレームの結合
print(pd.concat([df_left, df_right]))

# データフレームの結合
print(pd.concat([df_left, df_right], axis=1))

