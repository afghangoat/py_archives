#replace()
#karakterek lecserélése
print("""
Talpra magyar, hí a haza
Itt az idő, most vagy soha
Rabok legyünk vagy szabadok
Ez a kérdés válasszatok""".replace("e","a"))
#upper()
#lower()

print("Az ember nem ember.".upper()) #nagy betűt csinál mindenből
print("Az ember nem ember.".lower()) #kis betűt csinál mindenből
#title()
print("Az ember nem ember.".title()) #nagy betűvé teszi a szavak elejét
#capitalize()
print("Az ember nem ember.".capitalize()) #csak az 1. betűt nagy betűvé teszi
#__len__
print("Az ember nem ember.".__len__()) #megszámolja, hány betűből áll a string
#split()
print("Az ember nem ember.".split(" ")) #felbontja a stringet 1 paraméterrel
#count()
print("Az ember nem ember.".count("e")) #megszámolja, hányszor van a paraméter a string-be
#find()
print("Az ember nem ember.".find("nem")) #megnézi, megvan-e a paraméter a stringbe
#startswith()
#endswith()
print("Az ember nem ember.".startswith("A")) #megnézi, hogy a paraméterrel kezdődik-e a string
print("Az ember nem ember.".endswith(".")) #megnézei, hogy a paraméterrel végződik-e a string
#HF:
print("Welcome to USA.Usa is awesome, isn't it. Lets go to usa.".upper().count("USA"))
word = print("You will face many defeats in life, but never let yourself be defeated.")
word.__str__()
