import pandas as pd

data = pd.read_csv('/Users/sandradelgadoalmendrales/Library/Mobile Documents/com~apple~CloudDocs/Platzi /Numpy y Pandas/Proyecto curso/Pandas/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv',sep=',', header=0)

print(data)

data2 = pd.read_json('/Users/sandradelgadoalmendrales/Library/Mobile Documents/com~apple~CloudDocs/Platzi /Numpy y Pandas/Proyecto curso/Pandas/HPCharactersDataRaw.json', typ='Series')

print(data2)

#RETO

data3 = pd.read_csv('/Users/sandradelgadoalmendrales/Library/Mobile Documents/com~apple~CloudDocs/Platzi /Numpy y Pandas/Proyecto curso/Pandas/RealEstateUnitedStates.csv')
print(data3)