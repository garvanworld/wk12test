x = 10
print(f'var is {x}.')

class UserAccount:

    def __init__(self, firstname):
        #constructor, store firstname
        self.firstname = firstname

    def __str__(self):
        return f'In userAccount, firstname: {self.firstname}.'

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

peter = UserAccount("Pete firstn")
print(f"created new UserAcct for {peter.get_firstname()}")
print(peter)