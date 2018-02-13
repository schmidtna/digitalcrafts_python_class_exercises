class Person:
    def __init__(self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.friends_greeted = []
        # self.friends_greeted = set()

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        # self.friends_greeted.add(other_person.name)
        if other_person.name not in self.friends_greeted:
            self.friends_greeted.append(other_person.name)

    def contact_info(self):
        print("{}'s contact info is: Phone - {}, email - {}".format(self.name, self.phone, self.email))

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return "Person: {}, {}, {}".format(self.name, self.email, self.phone)

    def unique_greet_count(self):
        print(len(self.friends_greeted))
        


    

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", [], 0)
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [], 0)

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.contact_info()
jordan.add_friend(sonny)
jordan.num_friends()
print(sonny)
sonny.unique_greet_count()

# print(len(jordan.friends))

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("{}, {}, {}".format(self.make, self. model, self.year))

car = Vehicle("Nissan", "Leaf", 2015)

car.print_info()
    
    