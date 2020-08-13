w = 800
h = 800
n_people = 20
p_infection = 0.09
p_recovery = 0.001

class Person():
    def __init__(self, id, x, y, vx, vy):
        self.id = id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.status = "normal"
    
    def move(self):
        if self.x < 0 or self.x > w:
            self.vx *= -1
        if self.y < 0 or self.y > h:
            self.vy *= -1
            
        self.x += self.vx
        self.y += self.vy
    
    def display(self):
        if self.status == "infected":
            fill(255, 0, 0)
        elif self.status == "recovered":
            fill(0, 255, 0)
        else:
            fill(255, 255, 255)
        
        ellipse(self.x, self.y, 10, 10)
    
    def collide(self):
        for i in range(self.id+1, len(people)):
            person = people[i]
            distance = sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
            
            if distance < 20 and random(0, 1) < p_infection:
                if self.status == "infected" and person.status == "normal":
                    person.status = "infected"
                elif self.status == "normal" and person.status == "infected":
                    self.status = "infected"
    
    def change_status(self):
        if self.status == "infected" and random(0, 1) < p_recovery:
            self.status = "recovered"

people = []        
for i in range(n_people):
    person = Person(i, random(w), random(h), random(0, 5), random(0, 5))
    people.append(person)

people[0].status = "infected"        
    
def setup():
    global w, h
    size(w, h)
    background(32)
    
def draw():
    background(32)
    
    for person in people:
        person.move()
        person.collide()
        person.change_status()
        person.display()
