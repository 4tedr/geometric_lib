# Project documentations

Project includes different math functions

**Modules:**
- 'rectangle.py' - functions for working with rectangle
- 'circle.py' - functions for working with circles
- 'square.py' - functions for working with square

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Functions Description

### Module: rectangle.py

#### Function area(a, b)
Calculates the area of a rectangle with given width and height

**Parameters:**

- a (int): rectangle width
- b (int): rectangle height

**Returns:**

- int: rectangle area

**Example call:**

result = area(5, 4)
print(result)  # Output: 20

#### Function perimeter(a, b)
Calculates the perimeter of rectangle with given width and height

**Parameters:**

- a (int): rectangle width
- b (int): rectangle height

**Returns:**

- int: rectangle perimeter

**Example call:**

result = perimeter(5, 4)
print(result)  # Output: 18

### Module: circle.py

#### Function area(r)
Calculates the area of a circle with given radius.

**Parameters:**
- r (float): circle radius

**Returns:**
- float: circle area

**Example call:**

result = area(5)
print(result)  # Output: 78.53981633974483

#### Function perimeter(r)
Calculates the circumference length with given radius.

**Parameters:**

- r (float): circle radius

**Returns:**

- float: circumference length

**Example call:**

result = perimeter(5)
print(result)  # Output: 31.41592653589793

### Module square.py:

#### Function area(a)
Calculates the area of a square with given side length.

**Parameters:**
- a (int): square side length

**Returns:**
- int: square area

**Example call:**

result = area(4)
print(result)  # Output: 16

#### Function perimeter(a)
Calculates the perimeter of a square with given side length.

**Parameters:**

- a (int): square side length

**Returns:**
- int: square perimeter

**Example call:**

result = perimeter(4)
print(result)  # Output: 16

## Project Change History

- `d078c8d` - L-03: Docs added
- `8ba9aeb` - L-03: Circle and square added

