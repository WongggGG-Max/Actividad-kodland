meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "XD": "Algo gracioso o chistoso",
    "BRO": "Como para decirle a alguien hermano, amigo"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(word, "significa:", meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no existe BRO")
