class IOString():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ")
        
    def print_String(self):
        print("The Result is:", self.str1.upper())

str_obj = IOString()
str_obj.get_string()
str_obj.print_String()

        