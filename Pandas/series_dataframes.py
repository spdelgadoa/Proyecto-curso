import pandas as pd

#Ways to define Series

#1 With the index
psg_players = pd.Series(['Navas','Mbappe','Neimar','Messi'],
          index=[1,7,10,30])
print(psg_players)

#2 with no index, it set by default from 0
psg_players = pd.Series(['Navas','Mbappe','Neimar','Messi'])
print('\n Default index \n',psg_players)

#From a dict
dict = {1:'Navas', 7:'Mbapee', 10:'Neimar', 30:'Messi'}
pd.Series(dict)

print('\n Dict \n', pd.Series(dict))

#Use the index to identify an element

#Error: psg_players[0] --> there is no element with 0 index

#Correct
print(dict[7])

dict_2 = {'Jugador':['Navas','Mbappe','Neimar','Messi'],
          'Altura':[183.0, 170.0, 170.0,165],
          'Goles':[2, 200, 200, 200]}
df_PLayers = pd.DataFrame(dict_2,index=[1,7,10,30])
print(df_PLayers)

print(df_PLayers.columns)
print(df_PLayers.index)

#RETO 

granada_players = {'Jugador':['Luis Suárez','Jorge Molina', 'Antonio Puertas', 'Germán Sánchez', 'Luis Milla', 'Luís Manuel Arantes Maximiano'],

'Posición':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],

'Número':[9, 23, 10, 6, 5, 1],

'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],

'Goles':[7, 7, 5, 2, 2, 0]}

altura = pd.DataFrame(granada_players, index = [1,2,3,4,5,6])
print(altura)

print(pd.Series(granada_players))
print(altura.columns)
print(altura.index)
print(altura[0:2])

