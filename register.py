class Register:
  

    # Initializer / Instance Attributes
    def __init__(self, firstname, lastname, fullname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = fullname
        self.email = email
       


# instance method
    def allData(self, firstname, lastname, fullname, email):
        return "{} {} {} {}".format(self.firstname, lastname, fullname, email )
       

#Static Data
philo = Register("Ismael", "Sarunay", "Ismael Sarunay", "abuasyah2018@gmail.com")


# Display All Users
print(" First_name:{} \n Last_name:{} \n Full_name:{} \n Email:{}".format(
    philo.firstname, philo.lastname, philo.fullname, philo.email))
print("=============================")

# Update Users  
philo = Register("Ismael", "Reactjs", "Ismael Reactjs", "smilepogz@gmail.com")
print( philo.firstname, philo.lastname, philo.fullname, philo.email)
print("=============================")

# Add Users  
philo = Register(" React",  "\n Javascript", "\n React Javascript", "\n reactjs@gmail.com")
print( philo.firstname, philo.lastname, philo.fullname, philo.email)
print("=============================")


class Greek:
  firstname = "Ismael"
  lastname = "Sarunay"
  fullname = "Ismael Sarunay"
  email = "abuasyah2018@gmail.com"


names = Greek()  

print('Students before del--') 
print('First_name = ',names.firstname) 
print('Second_name = ',names.lastname) 
print('Full_name = ',names.fullname) 
print('Email = ',names.email) 

  
# implementing the operator 
del Greek.email 
  
print('After deleting fith student--') 
print('First_name = ',names.firstname) 
print('Second_name = ',names.lastname) 
print('Full_name = ',names.fullname) 
