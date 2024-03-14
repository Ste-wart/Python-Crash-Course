class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
        name = self.last_name.title() + ' ' + self.first_name.title()
        self.name = name

    def describe_user(self):
        """ prints a summary of the user’s information"""

        print(' Name:', self.name)
        print(' Age:', self.age, '\n Gender:', self.sex)

    def greet_user(self):
        print('-' * 30)
        if self.sex.lower() == 'male':
            print(f'Hello Mr. {self.name}, nice to meet you')
        elif self.sex.lower() == 'female':
            print(f'Hello Miss. {self.name}, nice to meet you')
        else:
            print(f'Hello {self.name}, nice to meet you')

    def increment_login_attempts(self):
        """ increments the value of login_attempts by 1"""
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        """ resets the value of login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, sex, privilege):
        super().__init__(first_name, last_name, age, sex)
        self.privilege = privilege
        User.describe_user(self)

    def show_privileges(self):
        print('As the Admin your privileges are:')
        for i in self.privilege:
            print('--', i)


me = User('Magnus', 'Stewart', 22, 'male')
me.describe_user()
me.greet_user()
me.increment_login_attempts()
me.increment_login_attempts()

df = ["can add post", "can delete post", "can ban user", ]
me = Admin('Magnus', 'Stewart', 22, 'male', df)
me.show_privileges()
