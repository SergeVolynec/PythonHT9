import pandas as pd

df = pd.read_csv('california_housing_train.csv')
print(df.loc[(df.population >= 0) & (df.population <= 500)].median_house_value.mean())
print(df.loc[(df.population < df.population.quantile(.15))].households.max())

