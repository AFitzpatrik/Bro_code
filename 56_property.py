# @property = Decorator used to define a method as a property (it can be accessed like and attribute)
# #           Benefit: Add additional logic when read, write or delete attributes
# #           Gives you getter, setter and deleter method




class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height #_.height = protected attribute, its private
        #jsou private, neměli by se použít 'natrvrdo' ale uvnitř methody

    @property
    def width(self):
        return f" {self._width:.1f}cm"

    @property
    def height(self):
        return f" {self._height:.1f}cm"



rectangle = Rectangle(3, 4)
print(rectangle.width)
print(rectangle.height)