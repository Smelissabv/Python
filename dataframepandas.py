import pandas as pd
data = {'Nombre':['Ana', 'Luis', 'Carlos'], 'Edad': [23, 24, 25,]}
df = pd.DataFrame(data)
# print(df) 
# print(df['Nombre'])
# print(df['Edad'])


# filtro =df[df['Edad'] > 24]
# print(filtro)
# print(df.describe())

print(df.head())
