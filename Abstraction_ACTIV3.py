
class India():

    def capital(self):
        print ("Delhi is Indias capital")

    def language(self):
        print("Hindi is the most widley spoken language in India")

    def type(self):
        print("India is a devloped country")

class USA():

    def capital(self):
        print ("Washington D.C is USA's capital")

    def language(self):
        print("English is the most widley spoken language in USA")

    def type(self):
        print("USA is a devloped country")

# Obj creation:

ind = India()
usa = USA()

# Common interface

for country in (ind, usa):
    country.capital()
    country.language()
    country.type()






