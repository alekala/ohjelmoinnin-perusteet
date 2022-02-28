# -*- coding: utf-8 -*-
# 003 Tunnistustehtävä

def move(x, y):
    print(f"Siirrytty kohtaan {x}, {y}.")

def home():
    move(0, 0)
    print("Siirrytty kotiin.")

def init():
    home()

if __name__ == "__main__":
    init()

# Mitä ohjelma tekee?
# Mitä vaiheita ohjelma käy läpi?
