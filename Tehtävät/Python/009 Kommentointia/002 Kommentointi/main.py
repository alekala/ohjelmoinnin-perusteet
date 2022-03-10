# -*- coding: utf-8 -*-
# 002 Kommentointi

# 
animals = ["Cat", "Dog", "Parrot", "Squirrel", "Sheep"]

# 
query = input("Anna hakusana:\n")

# 
found = False

# 
for animal in animals:
    # 
    if animal.lower() == query.lower():
        # 
        print("Haku löytyi!")
        # 
        found = True
        # 
        break

# 
if not found:
    # 
    print("Hakusana ei vastannut mitään...")

# Täydennä tyhjät kommenttipaikat selityksellä, mitä alapuolella olevalla rivillä tehdään.
# Tee kommentista mahdollisimman selkeä ja läpikotainen, että kuka tahansa voi ymmärtää mitä ohjelmassa tehdään.
