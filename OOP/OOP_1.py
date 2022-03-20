import csv

class Verification:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) <= 4:
            raise ValueError("lenght password is very small!")

    def save(self):
        with open('users.csv', mode='a', newline="") as writer:
            file_writer = csv.writer(writer)
            temp = [self.login, self.password]
            file_writer.writerow(temp)

