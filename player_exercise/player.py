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

player1 = Player()
print(player1)
player1.level_up()
print(player1)