class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hi,I'm {self.name} and I'm {self.age} years old."
    def __repr__(self):
        return f"person(name={self.name!r},age={self.age!r})"
p1=person("Alice",25)
p2=person("Bob",30)
print(p1)
print(p1.greet())
print(p2.name,p2.age)
        