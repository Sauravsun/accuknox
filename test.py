class Rectangle:
    def __init__(self, length:int, width:int):#It takes two parameters.
        self.length = int(length) #length argument to an integer and assigns it to the length attribute of the Rectangle object.
        self.width =int(width)#width argument to an integer and assigns it to the width attribute of the Rectangle object.

    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}]) # iterator over a list containing two dictionaries

if __name__ == "__main__":
    rect = Rectangle(5, 3)

    for item in rect: #for loop iterates over the rect objec
        print(item)