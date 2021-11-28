import pandas as pd
df = pd.read_csv('data.csv')

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

df.to_csv('updated.csv', index = False)
df.to_excel('updated.xlsx', index = False)
df.to_csv('updated.txt', index = False, sep = '\t')

print(df.head(5))



'''
   #                   Name Type 1  ... Speed  Generation  Legendary
0  1              Bulbasaur  Grass  ...    45           1      False
1  2                Ivysaur  Grass  ...    60           1      False
2  3               Venusaur  Grass  ...    80           1      False
3  3  VenusaurMega Venusaur  Grass  ...    80           1      False
4  4             Charmander   Fire  ...    65           1      False

[5 rows x 13 columns]
'''
# Generation  Legendary