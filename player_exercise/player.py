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
    
    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            return self.level_up()
        else: None

player1 = Player()
print(player1)
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
print(player1)