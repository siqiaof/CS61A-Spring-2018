#1
class Baller:
    all_players = []
    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False
        
class BallHog(Baller):
    def pass_ball(self, other_player):
        return False
#2
class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other_player):
        if self.has_ball:
            print('Yay!')
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            print("I don't have the ball")
            return False
        Baller.pass_ball(self, other_player)

#3
def has_seven(k):
    if k % 7 == 0:
        return True
    else:
        judge = False
        while k > 10:
            if k % 10 == 7:
                judge = True
            k = k // 10
        if k == 7:
            judge = True
        return judge

class PingPongTracker:
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True
    def next(self): 
        if self.add:
            self.current += 1
        else:
            self.current -= 1
        if has_seven(self.index):
            self.add = not self.add
        self.index += 1
        return self.current

#4
class Bird:
    def __init__(self, call):
        self.call = call
        self.can_fly = True
    def fly(self):
        if self.can_fly:
            return "Don't stop me now!"
        else:
            return "Ground control to Major Tom..."
    def speak(self):
        print(self.call)
        
class Chicken(Bird):
    def speak(self, other):
        Bird.speak(self)
        other.speak()
        
class Penguin(Bird):
    can_fly = False
    def speak(self):
        call = "Ice to meet you"
        print(call)
        
andre = Chicken("cluck")
gunter = Penguin("noot")

