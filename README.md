# OOP reprezentace HTML
## Úvod & Shrnutí
- Každý konkrétní tag je samostatnou třídou
- Každý tag může být přidán jako potomek nějakého párového tagu, vzniká tím stromová struktura
- Výsledkem vypsání je pak jednoduše formátované HTML i s atributy jednotlivých tagů
- Pro vložení textu slouží speciální tag TextTag
## Dědičnost
- všechny tagy dědí ze třídy Tag, která by se dala považovat za abstraktní
- ta zajišťuje vlastnosti, které mají všechny tagy společné
- z ní dědí třídy `LeafTag` a `PairTag`, které jsou také abstraktní
  - tyto třídy především definují, jakým způsobem se mají vytisknout jejich potomci
- každý konkrétní tag poté dědí buďto ze třídy
  - `PairTag`, pokud má mít možnost možnost obsahovat další html tagy
  - `LeafTag`, pokud nemá mít možnost obsahovat html tagy
## Atributy
- atributy, které jsou povinné jsou přímo jako parametr v konstruktoru
- pokud vyžadují zvláštní kontrolu, jsou implementovány jako private sloty tříd (podtržítka a přístup přes property)
- pokud jsou nepovinné, tak jsou implementovány jako sloty objektu s nastaveným typem na hodnotu `None`
- pomocí property `attributes` je možno určit, jaké atributy mají být vytisknuty spolu s tagem
### Warningy
- při nedodání povinných atributů při vytváření tagu systém do konzole vypíše barevný warning
  - ten nepřeruší běh programu, ale upozorní uživatele na chybějící hodnotu atributu
## Úprava jména tagu
- pomocí property `name` je možné specifikovat, jaké jméno má mít tag při tisku, není to však nutné, výchozí hodnotou je totiž název třídy
## Speciální TextTag
- je analogií k TextNodu z klasického DOMu, tedy představuje pouze text, aby bylo možné určit jeho pozici v HTML
- v tomto speciálním případě jsou záměrně porušena někerá z teoretických pravidel dědičnosti
