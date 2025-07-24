def greet(msg):
    print(msg)
    input("Press Enter to continue...")

class Helloworld:
    def __init__(self):
        self.message = "Hello, World!"

    def hello(self):
        greet("hello!")
    
    def welcome(self):
        greet("welcome!")

    def german(self):
        greet("guten Tag!")