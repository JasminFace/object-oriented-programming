class Paperboy:
    def __init__(self, name, experience, earnings):
    self.name = name
    self.papers_delivered = experience
    self.money_earned = earnings
    
    def __str__(self):
        return f"Name: {self.name} Experience: {self.papers_delivered} Earned: {self.money_earned}"

