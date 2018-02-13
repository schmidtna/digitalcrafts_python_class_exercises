class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))

    def contact_info(self):
        print("{}'s contact info is: Phone - {}, email - {}".format(self.name, self.phone, self.email))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)
sonny.contact_info()
    