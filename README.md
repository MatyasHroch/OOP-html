# OOP reprezentace HTML
## Dědičnost
- všechny tagy dědí ze třídy Tag, která by se dala považovat za abstraktní
- ta zajišťuje vlastnosti, které mají všechny tagy stejné
- z ní dědí třídy `LeafTag` a `PairTag`, které jsou také abstraktní
  - tyto třídy především definují, jakým způsobem se mají vytisknout všichni jejich potomci
- každý konkrétní tag poté dědí buďto ze třídy
  - `PairTag`, pokud má mít možnost možnost obsahovat další html tagy
  - `LeafTag`, pokud není párový a nemá tedy možnost obsahovat tagy
## Atributy
- atributy, které jsou povinné jsou přímo jako parametr v konstruktoru
- pokud vyžadují zvláštní kontrolu, jsou implementovány jako private sloty tříd (podtržítka a přístup přes property)
- pokud jsou nepovinné, tak jsou implementovány jako sloty objektu s nastaveným typem a hodnotou `None`
- pomocí property `attributes` je možno určit, jaké atributy mají být vytisknuty spolu s tagem
## Úprava jména tagu
- pomocí property `name` je možné specifikovat, jaké jméno má mít tag při tisku, není to však nutné, výchozí hodnotou je totiž název třídy
## Warningy
- při nedodání povinných atributů při vytváření tagu systém do konzole vypíše barevný warning
  - ten nepřeruší běh programu, ale upozorní uživatele na chybějící data
## Speciální TextTag
- je analogií k TextNodu, tedy představuje pouze text, aby bylo možné určit jeho pozici v HTML
- porušuje někerá z teoretických pravidel dědičnosti, ale v tomto případě to dává smysl
