class Rectangle:

    def __init__(self,width,height ) -> None:
        self.width = width
        self.height = height

    #setting the set_width method
    def set_width(self,width=None):
       if width !=None:
           self.width = width
           return width
       else:
            return self.width
        
    #setting the set_height method
    def set_height(self,height=None):
        if height != None:
            self.height =height
            return height
        else:
           return self.height
        
    #setting the get_area method
    def get_area(self):
        return self.width * self.height
    
    #setting the get_perimeter method
    def get_perimeter(self):
    
            return (2 * self.width + 2 * self.height)

    #setting up the get_diagonal method
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    
    #setting up the get_picture method
    def get_picture(self):
        length = "*" 
        breath = self.height
        
        while breath !=0:
            if self.height > 50 or self.width >50:
                print("Too big for picture.")
                break
            else:
                c = length * self.width
                breath -=1
                print(c)

    #setting the get_amount_inside method
    def get_amount_inside(self,shape):
        pass

    def __str__(self) -> str:
        result = f"Rectangel(width={self.width},height={self.height})"
        return result

#setting the squre class
class Square(Rectangle):
    #defining the contstructor
    def __init__(self,length, width=0, height=0) -> None:
        super().__init__(width, height)
        self.length = length
        self.side = 0
    
    #get_area method from Rectangle
    def get_area(self):
        return self.length **2
    
    #setting the set_side method
    def set_side(self,side):
        self.side += side
    
    #setting the idagonal
    def get_diagonal(self):
        diagonal = ((self.length ** 2 + self.length ** 2) ** 0.5)
        return diagonal
    
    def __str__(self) -> str:
        result = f"Square(side={self.length})"
        return result
    
    #getting the picture
    def get_picture(self):
        length = "*" 
        side = self.side
        breath = side
        
        while breath !=0:
            if self.height > 50 or self.width >50:
                print("Too big for picture.")
                break
            else:
                c = length * side
                breath -=1
                print(c)
    

c = Rectangle(10,5)
print(c.get_area())
c.set_height(3)
print(c.get_perimeter())
print(c)
c.get_picture()

s = Square(9)
print(s.get_area())
print(s.get_diagonal())
print(s)
s.set_side(4)
s.get_picture()