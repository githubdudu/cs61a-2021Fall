class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        self.lives = lives
        super().__init__(name, owner)

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        if not self.is_alive:
            print('This cat has no more lives to lose.')
        else:
            self.life -= 1
        if self.life <= 0 and self.is_alive:
            self.is_alive = False

    @classmethod
    def adopt_random_cat(cls, owner):
        """
        Returns a new instance of a Cat with the given owner,
        a randomly chosen name and a random number of lives.
        >>> randcat = Cat.adopt_random_cat("Ifeoma")
        >>> isinstance(randcat, Cat)
        True
        >>> randcat.owner
        'Ifeoma'
        >>> randcat.name
        'Aby'
        """
        namelist = ['Aby', 'Bete', 'Chor', 'Dizzy']
        rand_name = random.choice(namelist)
        rand_lives = random.randint(1, 9)
        return cls(rand_name, owner, rand_lives)

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()

import random as random
