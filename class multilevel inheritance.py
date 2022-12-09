#Multilevel inheritance between gradfather👴, father🧔‍♂️and the son👶

class Grandpa:
    
    def __init__(self):
        self.family_occupation = "Farming 🧑‍🌾"
                
    def grandpa_occupation(self):
        self.occupation = "Headmaster 👨‍🏫"
        return self.occupation

class Father(Grandpa):
    def father_occupation(self):
        self.occupation = "Gov employee"
        return self.occupation
    
class Son(Father):
    def son_occupation(self):
        print("I am earning to grow")
        
rohit = Son()
print(rohit.grandpa_occupation())
print(rohit.father_occupation())
rohit.son_occupation()
print(rohit.family_occupation)

    