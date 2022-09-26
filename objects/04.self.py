# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 


class student:
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills
    def say_name(self):
        print("mi nombre es",self.name,"mi cargo es ",self.position,"mis habilidades son",self.skills)

Alice = student("Alice","fullstack Developer",["Python","Git","HTML","CSS","javascript"])
Bob_el_chef = student("Bob el chef","kitchen helper",["Pastry chet international and cake shop","international foof","sea food"])

Alice.say_name()

Bob_el_chef.say_name()