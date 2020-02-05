class User(object):
     

    # Initializer / Instance Attributes
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    # instance method
        def allData(self):
            return "{} {} {} {}".format(self.firstname, self.lastname, self.email )
    #Static Data
philo = User("Ismael", "Sarunay", "abuasyah2018@gmail.com")

print("{} {} \n {}".format(philo.firstname, philo.lastname, philo.email))




def userRegistration(person):
   
    print( "" + person + ".")
  

def main():
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    email = input("Enter email addres: ")
    userRegistration(firstname)
    userRegistration(lastname)
    userRegistration(email)
     
main()


