class Person:
    pass
    #attributes
    
    #construcktur method
    
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("init metodu çalıştı.")
    #methods
    
    
#object(instance)

p1=Person("ali",1990)

print(p1)

p2=Person("yarrak",1980)

print(p2)

print(type(p1))


print(f"name={p1.name}")

print(f"name={p2.name}")


#classlara method ekleme



class new:
    adress="no information"
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("construcktor oluşturuldu")
    #instance methods
    def intro(self):
        print("hello there. I'm "+self.name)
        
    def agecal(self):
        return 2025-self.year
        
    


pn=new(name="eren",year=2002)
    
pn.adress="denizciler"


print(f"name={pn.name}, year={pn.year}, adress={pn.adress} ")

print(f"{pn.intro()}.I'm {pn.agecal()} years old.")


class Circle:
    pi=3.14
    def __init__(self,yaricap=1):
       self.yaricap=yaricap
    
    def alanhesap(self):
        return 2*self.pi*((self.yaricap)**2)
    def cevre(self):
        cevre=2*self.pi*(self.yaricap)
        return cevre
C1=Circle()
c2=Circle(yaricap=5)

print(C1.alanhesap())
print(c2.cevre())



#inheritance



class personn():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("person created.")
class student(personn):
    def __init__(self,fname,lname):
        personn.__init__(self,fname,lname)
    print("student created.")
    

p1=personn("ali","yılmaz")
s1=student("yarrak","gülgeç")
print(s1.firstname,s1.lastname)




class Circle2:
        pi=3.14
        def __init__(self,yaricap=1):
            self.yaricap=yaricap
        
    
        def alanhesap(self,yaricap=1):
            return 2*self.pi*(self.yaricap**2)
        def cevre(self,yaricap):
            return 2*self.pi*self.yaricap
c3=Circle2(5)
        
print(f"circle 3 alan {c3.alanhesap()} circle 3 cevre {c3.cevre(5)}")
        






