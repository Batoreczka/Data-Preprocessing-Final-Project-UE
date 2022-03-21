# Data-Preprocessing-Final-Project-UE

## Część pierwsza:
Rzeczywiste dane finansowe zawierają informację o cenie intrumentu oraz wartościach wskaźników technicznych. 
Decyzja o zakupie (BUY lub STRONGBUY), sprzedaży (SELL lub STRONGSELL), lub czekaniu (WAIT) podejmowana jest w oparciu o poniższe wskaźniki, a także na
podstawie relacji pomiędzy wskaźnikami, a ceną. 

###### Poniżej szczegółowy opis danych:
* Close – wartość instrumentu na zamknięcie danej sesji;
* SMA14 i SMA50 – wartości prostych średnich kroczących wyznaczonych w oparciu o 14 (SMA14) i 50 (SMA50) ostatnich odczytów;
* SMA14IND i SMA50IND - wartości zmiany dla średnich kroczących obserwowane pomiędzy sąsiednimi odczytami;
* Bulls – wskaźnik określający siłę byków (siła trendu wzrostowego na rynku);
* CCI,DM, RSI – Commodity Channel Index, DeMarker oraz Relative Strength Index – oscylatory szacujące poziom wykupienia (wyprzedania na rynku);
* OSMA – Oscillator of Moving Average – oscylator średniej kroczącej;
* Stoch – oscylator stochastyczny;
* Decision – wartość decyzji podejmowanej na podstawie ustalonych wartości wskaźników (SELL, STRONGSELL, BUY, STRONGBUY, WAIT).

1. Wczytaj dane do formatu DataFrame wybierając tylko 2500 obiektów z pliku;
2. Usuń kolumny oznaczone jako SMA14IND oraz SMA50IND;
3. Dla kolumny Close policz liczbę wystąpień danych pustych. Napraw dane w taki sposób, że pusta wartość zastępowana jest wartością uśrednioną dwóch sąsiednich elementów;
4. W przypadku danych pustych w kolumnach SMA14 i SMA50 napraw wartości puste dowolną metodą;
5. Dla wszystkich pozostałych atrybutów wypełnij wartości puste zerami;
6. Wyznacz korelację pomiędzy SMA14 i SMA50;
7. Wyznacz korelację pomiędzy Close oraz SMA14 a także pomiędzy Close oraz SMA50. Usuń kolumnę, dla której wartość korelacji była większa;
8. Podaj liczbę elementów ujemnych dla atrybutu CCI;
9. Podaj informację o wartości maksymalnej i minialnej dla każdego atrybutu;
10. Przeprowadź normalizację dwóch wybranych atrybutów;
11. Przeprowadź dyskretyzację dwóch wybranych atrybutów (podział odpowiednio na 2 i 4 kategorie);
12. Na wykresie kołowym przedstaw rozkład wartości decyzji (atrybut Decision);
13. Na wykresie liniowym przedstaw przebieg zmienności atrybutu Close;
14. Dane po preprocessingu zapisz do pliku w formacie JSON.

## Część druga:
Należy wygenerować sztuczny zestaw danych o takiej samej wielkości, jak zestaw bazowy. Jednocześnie należy kierować się następującymi założeniami:
1. w pierwszym wierszu dla danych znajdują się elementy losowe z zakresu ⟨mini , maxi ⟩, gdzie mini jest wartością minimalną i-tego atrybutu, a wartość maxi jest wartością maksymalną i-tego atrybutu;
2. losowe wartości w poszczególnych kolumnach nie mogą wyjść poza wskazany zakres ⟨mini , maxi ⟩, dla i = 1, 2, ..., k gdzie k jest liczbą atrybutów z wyłączeniem atrybutu decyzyjnego;
3. zmiana wartości dla poszczególnych atrybutów w kolejnych wierszach musi być w zakresie ⟨prevval − prevval · 1%; prevval + prevval · 1%⟩;
4. w przypadku, gdy wynikiem będzie wartość poza zakresem max (lub min) należy jako nową wartość przyjąć właśnie wartość max (lub min);
5. wartości atrybutu decyzyjnego ustalane są na podstawie rozkładu jednostajnego zbioru zawierającego te same wartości atrybutów, co zbiór oryginalny;
6. po wygenerowaniu tablicy należy policzyć korelację pomiędzy każdą z kolumn z pierwszego zestawu oraz odpowiadającym kolumnom z drugiego zestawu (tj. korelacja pomiędzy pierwszymi kolumnami, korelacja pomiędzy drugimi kolumnami i tak dalej).
