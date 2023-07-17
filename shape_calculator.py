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
        picture = []
        
        while breath !=0:
            if self.height > 50 or self.width >50:
                return "Too big for picture."
            else:
                c = length * self.width
                picture.append(c)
                breath -=1
        return "\n".join(picture)+"\n"

    #setting the get_amount_inside method
    def get_amount_inside(self,shape):
        return self.get_area()// shape.get_area()

    def __str__(self) -> str:
        result = f"Rectangle(width={self.width}, height={self.height})"
        return result

#setting the squre class
class Square(Rectangle):
    #defining the contstructor
    def __init__(self,length) -> None:
        super().__init__(width=length, height=length)
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
        result = f"Square(side={self.width})"
        return result
    
    #getting the picture
    def get_picture(self):
        length = "*" 
        side = self.length
        breath = side
        picture = []
        
        while breath !=0:
            if self.height > 50 or self.width >50:
                return "Too big for picture."
                
            else:
                c = length * side
                picture.append(c)
                breath -=1
        return "\n".join(picture)+"\n"
                
if __name__ == "__main__":            
    

    # rect = Rectangle(10, 5)
    # print(rect.get_area())
    # rect.set_height(3)
    # print(rect.get_perimeter())
    # print(rect)
    # print(rect.get_picture())

    rect = Rectangle(3, 6)
    sq = Square(5)

    # print("RECTANGLE ",rect.get_perimeter())# expected = 18
    # print("SQUARE", sq.get_perimeter())# expected = 20

    rect.set_width(7)
    rect.set_height(8)
    sq.set_side(2)
    print(rect)# "Rectangle(width=7, height=8)"
    print(sq)#"Square(side=2)"
    sq.set_width(4)
    print(sq)#"Square(side=4)"
      


