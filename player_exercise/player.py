class Player:
    """ A class that represents a player """
    def __init__(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return f"Lives: {self.lives}  Health: {self.health_points}  Gold Coins: {self.gold_coins}"

player1 = Player()
print(player1)