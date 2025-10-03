lugat = {
    "agar": "if",
    "aks": "else",
    "chiqar": "print",
    "takrorla": "for",
    "ichida": "in",
    "qator": "range"
}
def tarjima(ozbekcha_kod):
    lugat = {
        "agar": "if",
        "aks": "else",
        "chiqar": "print",
        "takrorla": "for",
        "ichida": "in",
        "qator": "range"
    }
    # Har bir so‘zni lug‘atdan qidirib almashtiramiz
    sozlar = ozbekcha_kod.split()
    tarjima_qilingan = []
    for soz in sozlar:
        if soz in lugat:
            tarjima_qilingan.append(lugat[soz])
        else:
            tarjima_qilingan.append(soz)
    return " ".join(tarjima_qilingan)


# Sinash
ozbekcha = 'agar son > 0: chiqar("Musbat") aks: chiqar("Manfiy")'
print("O‘zbekcha kod:", ozbekcha)
print("Python kodi:", tarjima(ozbekcha))

O‘zbekcha kod: agar son > 0: chiqar("Musbat") aks: chiqar("Manfiy")
Python kodi: if son > 0: print("Musbat") else: print("Manfiy")
