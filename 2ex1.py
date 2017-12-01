class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        
    def say_hello(self):
        print(self.msg)
        
if __name__ == "__main___":
    print("Hi")

#instance of class
inst = PythonProjects("First message")
    
#call via instance
inst.say_hello()