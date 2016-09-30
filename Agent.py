import numpy as np
import uuid

class Gambler(object):
    """This class will represent the agents in my model, who I term gamblers.
    They love to gamble. They don't mind risk in the least. In fact, they love
    highly volatile gambling events. Many of them will soon be broke."""
    
    def __init__(self, funds=1000):
        self.name = uuid.uuid4()
        self.funds = funds 
        self.shares = 0
        self.wagers = 0
        self.getBelief()

    def getBelief(self):
        """Establishes an internal range of belief around some unknown event."""
        self.mu = np.random.normal(0.5,0.25)
        self.sigma = np.random.normal(0.2, 0.1)
        
    def getAverage(self):
        """Returns average cost basis across all bets"""
        if self.shares > 0:
            self.average = self.wagers/self.shares
            return self.average
        else: return "You're a bum! (you have no skin in the game)"
    
    def biasedFlip(self, price):
        """Decision rule for buying, selling, or holding"""
        p = (self.mu + self.sigma - price) / (2.0 * self.sigma)
        return np.random.random() <= p
    
    def decideTrade(self, price):
        """Implementation of decision rule"""
        if price < (self.mu - self.sigma):
            while price < self.getAverage() and self.funds >= price:
                self.buy(price)
        if price > (self.mu + self.sigma):
            while self.shares > 0:
                self.sell(price)
        if (self.mu - self.sigma) < price < (self.mu + self.sigma):
            if self.biasedFlip(price):
                while price < self.getAverage() and self.funds >= price:
                    self.buy(price)
            else: return "I don't know what to do!!! \n", str(self)
            
    def buy(self, price, N=1):
        if self.funds >= N * price:
            self.funds -= N * price
            self.shares += N
        else: return "You're a bum! (price exceeds funds)"
    
    def sell(self, price, N=1):
        if self.shares > 0:
            self.shares -= N
            self.wagers -= N * price
            self.funds += N * price
        else: return "You're a bum! (shares = 0)"
        
    def __str__(self):
        string = ("Agent ID: {0} \n"
        "Funds: {1} \n"
        "Shares: {2} \n"
        "Belief HIGH: {3} \n"
        "Belief LOW: {4}").format(self.name, self.funds, self.shares, 
                                  (self.mu + self.sigma), (self.mu - self.sigma)) 
        return string