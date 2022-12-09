# Multiple inheritance is one child🧒 class inheriting from multiple 
# classes say father🧔‍♂️ and mother 👩
#

class Mom:
    def affections(self):
        print("Mother cares immensely for you")
        
class Father:
    def money(self):
        print("Father is providing money")
        
class Son(Father, Mom):
    pass

rohit = Son()
rohit.affections()
rohit.money()