class Bank:

    def __init__(self, password, username='Anonymous'):
        self.username = username
        self.password = password
        print(f'Welcome Mr.{self.username}')


user1 = Bank('12345', 'balaji')
user2 = Bank('123')
