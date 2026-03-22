class EmptyException(RuntimeError):
    def __init__(self, argument):
        self.arguments = argument
        
var =""

try :
    raise EmptyException("This variable is an empty string")
except EmptyException as e :
    print(e.arguments)