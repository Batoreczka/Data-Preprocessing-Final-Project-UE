# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:43:03 2022

@author: bator
"""

import pandas
import os
import random

print(os.getcwd())

data = pandas.read_json('projekt_1_bator.json') # plik bazowy
print(data) #sprawdzam, czy się wczytało

n_elems = 2500 #liczba wierszy

max_values = data.max(axis=0) # maksymalne wartosci
min_values = data.min(axis=0) # minimalne wartosci

column_names = list(min_values.index)
column_names.remove("Decision") #usuwam kolumne atrybutu decyzyjnego
#print(column_names)


# w pierwszym wierszu dla danych znajdują się elementy losowe z zakresu ⟨mini , maxi ⟩, gdzie mini jest wartością minimalną i-tego
# atrybutu, a wartość maxi jest wartością maksymalną i-tego atrybutu;

random_data_dict = {cn : [random.uniform(min_values[cn], max_values[cn])] for cn in column_names}

# losowe wartości w poszczególnych kolumnach nie mogą wyjść poza wskazany zakres ⟨mini , maxi ⟩, dla i = 1, 2, ..., k gdzie k jest liczbą
# atrybutów z wyłączeniem atrybutu decyzyjnego;
# zmiana wartości dla poszczególnych atrybutów w kolejnych wierszach musi być w zakresie ⟨prevval − prevval · 1%; prevval + prevval · 1%⟩;
# w przypadku, gdy wynikiem będzie wartość poza zakresem max (lub min) należy jako nową wartość przyjąć właśnie wartość max (lub min);


for cn in random_data_dict:
  for i in range(n_elems - 1):
    new_val = random.uniform(random_data_dict[cn][-1] * 0.99, random_data_dict[cn][-1] * 1.01)
    if new_val > max_values[cn]:
      new_val = max_values[cn]
    elif new_val < min_values[cn]:
      new_val = min_values[cn]

    random_data_dict[cn].append(new_val)
    
# wartości atrybutu decyzyjnego ustalane są na podstawie rozkładu jednostajnego zbioru zawierającego te same wartości atrybutów, co zbiór oryginalny;

random_data_dict["Decision"] = [random.choice(["STRONGBUY", "BUY", "WAIT", "SELL", "STRONGSELL"]) 
                          for i in range(n_elems)]


random_data = pandas.DataFrame(random_data_dict)
print(random_data)
print("Korelacje:\n",  random_data.corrwith(data))
