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
        self.shape = shape
        if self.shape == shape:
            num_of_shape = self.get_area()/(self.width * self.width)
            return num_of_shape
        else:
            num_of_shape = self.get_area()/(self.width * self.height)
            return num_of_shape

    def __str__(self) -> str:
        result = f"Rectangel(width={self.width},height={self.height})"
        return result

#setting the squre class
class Square(Rectangle):
    #defining the contstructor
    def __init__(self,length, width=0, height=0) -> None:
        super().__init__(width, height)
        self.length = length
        
    
    #get_area method from Rectangle
    def get_area(self):
        return self.length **2
    
    #setting the set_side method
    def set_side(self,side=None):
        if side != None:
            self.length = side
            return side
        else:
           return self.length
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
        side = self.length
        breath = side
    
        
        while breath !=0:
            if self.height > 50 or self.width >50:
                print("Too big for picture.")
                break
            else:
                c = length * side
                breath -=1
                print(c)
                
if __name__ == "__main__":            
    

    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    rect.get_picture()

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))


