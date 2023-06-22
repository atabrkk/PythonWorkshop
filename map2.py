# cities_cel içersindeki şehirlerin sıcaklık derecelerini celcius'tan fahrenheit'a çevirme. 

cities_cel = [
    ("İstanbul", 27),
    ("Ankara", 24),
    ("İzmir", 31),
    ("Antalya", 34)
]

cel_to_fah = lambda city: (city[0], (city[1] * (9/5) + 32))

cities_fah = list(map(cel_to_fah, cities_cel))

print(cities_fah)