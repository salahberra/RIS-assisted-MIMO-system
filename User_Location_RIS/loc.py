import numpy as np 
import matplotlib.pyplot as plt

#the code presents the location of the base station and RIS (Reconfigurable intelligent surfaces ) vers the users.

class pos():
    def __init__(self, x=200, y=30, r=10, R=20): # the dimensions of the area that can be covered via the base station and RIS.
        self.x=x # height of the base station BS
        self.y=y # width of the base station BS
        self.r=r # optimal raduis
        self.R=R # maximal raduis

    def position(self, K=5):
        if not isinstance(K, int):
                raise TypeError('Parameter K must an integer')
        if K < 0:
                raise ValueError('Parameter K must be non-negative')
        Pt = np.zeros((K,2))
        for k in range(K):
            amplitude=np.random.uniform(self.R) #distrubation of random amplutide 
            theta=np.random.uniform(2*np.pi) # distrubation of the phase
            p=np.array([[np.cos(theta), np.sin(theta)]]) # the coordonations
            Pt[k,:] = np.array([[self.x, self.y]]) + amplitude*p # raduis of each users with random values  
        return Pt

    def plot(self, pos, figure=1):
        plt.figure(figure)
        circle_theta = np.linspace(0, 2*np.pi, 100)
        plt.plot(self.r*np.cos(circle_theta) + self.x, self.r*np.sin(circle_theta) + self.y, 'g--')
        plt.plot(self.R*np.cos(circle_theta) + self.x, self.R*np.sin(circle_theta) + self.y, 'r--')
        plt.scatter(pos[:,0], pos[:,1], s=50, c='r')
        plt.xlim(self.x-self.R, self.x+self.R); plt.ylim(self.y-self.R, self.y+self.R);
        plt.xlabel("position of user in lax X")
        plt.ylabel("position of user in lax Y")
        plt.title('The position of Users in the RIS')
        plt.grid(b=True, which='major')
        plt.grid(b=True, which='minor',alpha=0.4)
        plt.show()
