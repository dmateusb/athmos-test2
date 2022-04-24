class User:

    def __init__(self, n, l, a, e):
        self.__names = n
        self.__last_names = l
        self.__age = a
        self.__email = e

    def __repr__(self):
        message = """[ names: {}, last_names: {}, age: {}, email: {} ]""".format(
            self.__names, self.__last_names, self.__age, self.__email)
        return message