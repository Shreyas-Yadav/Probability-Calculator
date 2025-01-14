import random
"""
This module simulates a probability experiment involving drawing balls from a hat.
Classes:
    Hat: Represents a hat containing balls of different colors.
Functions:
    experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
        Conducts a probability experiment to determine the likelihood of drawing a specific combination of balls from the hat.
Usage Example:
    hat = Hat(blue=3, red=2, green=6)
    expected_balls = {'blue': 2, 'green': 1}
    num_experiments = 1000
    probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
    print(probability)
"""
class Hat:
    def __init__(self,**args):
        self.contents = []
        for k,v in args.items():
            while v > 0:
                self.contents.append(k)
                v-=1
        
    

    def draw(self,number_of_balls=0):
        # removing all balls from contents
        if number_of_balls >= len(self.contents):
            copyList = self.contents.copy()
            self.contents.clear()
            return copyList
        
        # removing requested balls randomly
        removed_balls = []
        while number_of_balls > 0:
            index=random.randint(0,len(self.contents)-1)
            removed_balls.append(self.contents[index])
            del self.contents[index]
            number_of_balls-=1
        
        # print(removed_balls,self.contents)
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list = []
    for k,v in expected_balls.items():
        while v > 0:
            expected_list.append(k)
            v-=1
    

    expected_dict = {}
    for item in expected_list:
        expected_dict[item] = expected_dict.get(item, 0) + 1
    
    hit_count = 0
    expriments = num_experiments
    while expriments > 0:
        drawn_balls = hat.draw(num_balls_drawn)
        drawn_dict = {}
        for item in drawn_balls:
            drawn_dict[item] = drawn_dict.get(item, 0) + 1
        
        if all(drawn_dict.get(k,0) >= expected_dict.get(k) for k,v in expected_dict.items()):
            hit_count+=1
        
        hat.contents.extend(drawn_balls)
        expriments -= 1
    return hit_count/num_experiments
    


hat = Hat(blue=3,red=2,green=6)
expected_balls = {'blue':2,'green':1}
num_balls_drawn = 4
num_experiments=1000
print(f'Probability:', experiment(hat,expected_balls,num_balls_drawn,num_experiments))