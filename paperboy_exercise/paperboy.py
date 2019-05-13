class Paperboy:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0
    
    def __str__(self):
        return f"Name: {self.name} Experience: {self.experience} deliveries Earned: ${self.earnings}"

    def quota(self):
        return int(self.experience / 2) + 50


    def deliver(self, start_address, end_address):
        papers_delivered = abs(end_address - start_address)
        quota_papers = self.quota()
        extra_papers = (papers_delivered - quota_papers)
       
        self.experience += papers_delivered
        
        if papers_delivered == quota_papers:
            self.earnings += papers_delivered * 0.25
        elif papers_delivered > quota_papers:
            self.earnings += (papers_delivered * 0.25) + (extra_papers * 0.25)
        elif papers_delivered < quota_papers:
            self.earnings -= 2
        return self.earnings
        
    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned ${:.2f} so far!".format(self.name, self.experience, self.earnings)

tommy = Paperboy("Tommy")


tommy.deliver(86,202)
print(tommy.report())

tommy.deliver(143,18)
print(tommy.report())

tommy.deliver(21, 59)
print(tommy.report())

tommy.deliver(1,9000)
print(tommy.report())
