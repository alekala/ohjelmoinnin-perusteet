# -*- coding: utf-8 -*-
# 001 Kommentointi

# 
def read_file(file):
    # 
    with open(file, "r") as f:
        # 
        content = f.read()
    # 
    return content

# 
def print_words(content):
    # 
    words = content.split()
    # 
    for word in words:
        # 
        print(word)

# 
if __name__ == "__main__":
    # 
    content = read_file("message.txt")
    # 
    print_words(content)

# Täydennä tyhjät kommenttipaikat selityksellä, mitä alapuolella olevalla rivillä tehdään.
# Tee kommentista mahdollisimman selkeä ja läpikotainen, että kuka tahansa voi ymmärtää mitä ohjelmassa tehdään.
