class Player:
    """ A class that represents a player """
    def __init__(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return f"Lives: {self.lives}  Health: {self.health_points}  Gold Coins: {self.gold_coins}"

    def level_up(self):
        self.lives += 1
        if self.lives == 1:
            print(f"You gained a life! You have {self.lives} life!")
        else:
            print(f"You gained a life! You have {self.lives} lives!")
    
    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            return self.level_up()
        
        if self.gold_coins == 1:
            print(f"You found a coin! You have {self.gold_coins} coin!") 
        else:
            print(f"You found a coin! You have {self.gold_coins} coins!")  

    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10
            if self.lives < 0:
                return self.restart()
        print(f"Oh no! You're hit! You received {damage} damage.")

    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5
        print("GAME OVER. Try again!")
        


player1 = Player()

print(player1)