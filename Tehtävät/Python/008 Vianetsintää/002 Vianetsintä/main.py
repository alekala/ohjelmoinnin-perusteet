# -*- coding: utf-8 -*-
# 002 Vianetsintää

errorState = True

def throwError(error_message):
    print(error_message)
    sys.exit(2)

if __name__ == "__main__":
    if errorState:
        throwError("Vika löydetty!")

# Ohjelmasta puuttuu kirjasto, korjaa puute.
