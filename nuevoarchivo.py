import pandas as pd

df = pd.read_csv("poblacion.csv")
print(df)

# print(df.head())

# print(df.describe())

# print(df.tail())

# print(df.sample(20))

# filtro = df[df['Date'] > 2010]
# print(filtro['COL'])

# df.at[0, "COL"] = 50000
# print(df["COL"])

df = df.drop("ABW", axis=1)
print(df)

df.to_csv("salida.csv", index=False)

