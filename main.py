import random

class Agent():
    def __init__(self, health=-1):
        if health == -1:
            self.health = random.randint(10,20)
        else:
            self.health = health
        self.starting_health = self.health
    def die(self):
        if self.health <= 0:
            return True
        return False
    def timestep(self, delta=1):
        self.health -= delta
        if self.die():
            return True
        return False
    def have_child(self):
        return Agent(health=self.starting_health)

avg_difference = 0
for w in range(100):
    agents = []
    before_average_starting_health = 0
    for i in range(10):
        agents.append(Agent())
        before_average_starting_health += agents[i].starting_health
    before_average_starting_health /= 10

    childern_born = 0
    deaths = 0

    for i in range(100):
        num_agents = len(agents)
        to_decrease = 0
        for j in range(num_agents):
            j -= to_decrease
            if agents[j].timestep():
                deaths += 1
                to_decrease += 1
                del agents[j]
            elif random.random()<0.1:
                childern_born += 1
                agents.append(agents[j].have_child())

    after_average_starting_health = 0
    for agent in agents:
        after_average_starting_health += agent.starting_health
    after_average_starting_health /= len(agents)
    w += after_average_starting_health-before_average_starting_health
w/=100
print(w)

# print("\n")
# print("Num agents:", len(agents))
# print("Total deaths:", deaths)
# print("Total births:", childern_born)
# print("Before average:", before_average_starting_health)
# print("After average:", after_average_starting_health)