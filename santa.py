"""This is santa."""
from faker import Faker


fake = Faker()


class Santa(object):
    """Santa generator."""

    def __init__(self):
        """Initialize a new santa."""
        self.name = 'Gerard'
        self.naughty_list = {}
        self.wish_list = {}
        self.greeting = 'HO HO HO!'
        self.cookies = False
        self.rap_sheet = None

    def _naughty_list_maker(self):
        """Make a naughty list."""
        for person in range(100):
            self.naughty_list.setdefault(fake.name, fake.address)

    def _wish_list_maker(self):
        """Make a wish list."""
        for person in self.naughty_list:
            self.wish_list.setdefault(person.name, fake.text(10))
        for x in range(100):
            self.wish_list.setdefault(person.name, fake.text(10))


if __name__ == '__main__':
    make = input('Would you like a make a santa? Y/N')
    if make == 'Y':
        name = input('What would you like to name your santa?')
        if isinstance(name, str):
            name = Santa()
            name.name = name
            check = input('Would you like to see the wish list?')
            print('Here it is!')
            print(name.wish_list)
            add = input('What would you like to wish for?')
            user = input('What\'s your name?')
            name.naughty_list.setdefault(user, fake.address)
            name.wish_list.setdefault(user, add)
            print('I\'ll see what I can do.')
            print('Let us check the list...')
            print('It looks liks you are on the naughty list.')
            print(name.naughty_list)
            print('Maybe if you leave santa cookies you will be removed?')
            cookies = input('How many cookies would you like give him?')
            name.cookies = cookies
            del name.naughty_list[user]
            print('Let us check again...')
            print(name.naughty_list)
            print('What about that wish list?')
            print(name.wish_list)
        else:
            print('Sorry, you did not enter a name. You are on the naughty list.')
    else:
        print('Ok. You are on the naughty list.')
