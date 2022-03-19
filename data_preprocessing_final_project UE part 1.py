# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:48:52 2022

@author: bator
"""

import pandas
import numpy
import os
### 1.Wczytaj dane do formatu DataFrame wybierając tylko 2500 obiektów z pliku
print(os.getcwd())
data = pandas.read_csv('EURUSD_H4.csv', nrows=2500)
#print(data) ### sprawdzam, czy dobrze wyszło

### 2.Usuń kolumny oznaczone jako SMA14IND oraz SMA50IND
data.drop('SMA14IND', inplace=True, axis=1)
data.drop('SMA50IND', inplace=True, axis=1)

 ### 3.Dla kolumny Close policz liczbę wystąpień danych pustych. Napraw dane w taki sposób, że pusta wartość zastępowana jest wartością uśrednioną dwóch sąsiednich elementów
count_null_close = data['Close'].isnull().sum()
data['Close'] = data['Close'].interpolate()
###print(data['Close'])

### 4. W przypadku danych pustych w kolumnach SMA14 i SMA50 –napraw wartości puste dowolną metodą
count_null_close = data['SMA14'].isnull().sum()
data['SMA14'] = data['SMA14'].fillna(0) ### nadpisuje zerami
###print(data['SMA14'])
count_null_close = data['SMA50'].isnull().sum()
data['SMA50'] = data['SMA50'].interpolate() ###uśredniam
##print(data['SMA50'])

### 5. Dla wszystkich pozostałych atrybutów wypełnij wartości puste zerami
###count_null_frame = data.isnull().sum() ### sprawdzanie pustych
###print(count_null_frame)
data['Bulls'] = data['SMA14'].fillna(0) ### nadpisuje zerami

### 6. Wyznacz korelację pomiędzy SMA14 i SMA50
korelacjaSMA1450 = data['SMA14'].corr(data['SMA50'])
#print (korelacjaSMA1450)

### 7.  Wyznacz korelację pomiędzy Close oraz SMA14 a także pomiędzy Close oraz SMA50. Usuń kolumnę, dla której wartość korelacji była większa;
korelacja14_close = data['SMA14'].corr(data['Close'])
#print (korelacja14_close)

korelacja50_close = data['SMA50'].corr(data['Close'])
#print (korelacja50_close)

if (korelacja14_close>korelacja50_close):
    data.drop('SMA14', inplace=True, axis=1)
else:
    data.drop('SMA50', inplace=True, axis=1)
#print(data)

### 8. Podaj liczbę elementów ujemnych dla atrybutu CCI
negative_CCI = sum(data['CCI'].lt(0))
print(negative_CCI)

### 9 Podaj informację o wartości maksymalnej i minialnej dla każdego atrybutu
max_values = data.max(axis=0)
min_values = data.min(axis=0)
print('Wartosci maksymalne atrybutow')
print(max_values)
print('Wartosci minimalne atrybutow')
print(min_values)
##########

### 1. Przeprowadź normalizację dwóch wybranych atrybutów
atributes = ['RSI','Stoch']

for atribute in atributes:
    max_RSI = data['RSI'].max()
    min_RSI = data['RSI'].min()
    data['RSI'] = (data['RSI'] - min_RSI)/(max_RSI-min_RSI)

    max_Stoch = data['Stoch'].max()
    min_Stoch = data['Stoch'].min()
    data['Stoch'] = (data['Stoch'] - min_Stoch)/(max_Stoch-min_Stoch)
print(data)

## 2 Przeprowadź dyskretyzację dwóch wybranych atrybutów (podział odpowiednio na 2 i 4 kategorie)
labels_1 = ['Q1','Q2','Q3','Q4']
series_1 = pandas.Series(numpy.array(data['Bulls']))
discrete_1 = pandas.cut(series_1,4,labels_1)

labels_2 = ['Up','Down']
series_2 = pandas.Series(numpy.array(data['DM']))
discrete_2 = pandas.cut(series_2,2,labels_2)

##3 Na wykresie kołowym przedstaw rozkład wartości decyzji (atrybut Decision);
data['Decision'].value_counts().plot.pie()

##4 Na wykresie liniowym przedstaw przebieg zmienności atrybutu Close;
data['Close'].plot()

##5 Dane po preprocessingu zapisz do pliku w formacie JSON.
data.to_json("projekt_1_bator.json")

