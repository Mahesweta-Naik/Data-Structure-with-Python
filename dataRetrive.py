#retrive all the data(name, age, gender) present in a queue by  males and females
'''class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def get_people_by_gender(self, gender):
        people = []
        for person in self.items:
            if person.gender == gender:
                people.append(person)
        return people

q = Queue()
q.enqueue(Person('Alice', 25, 'female'))
q.enqueue(Person('Bob', 30, 'male'))
q.enqueue(Person('Charlie', 20, 'male'))
q.enqueue(Person('David', 27, 'male'))
q.enqueue(Person('Eve', 22, 'female'))

people = q.get_people_by_gender('female')
if people:
    for person in people:
        print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
else:
    print("No people of the given gender found in the queue.")'''
