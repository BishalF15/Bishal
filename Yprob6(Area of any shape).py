
base = float(input("Enter base value : "))
height = float(input("Enter height value : "))
width = float(input("Enter width value : "))
radius = float(input("Enter radius value : "))

Triangle_Area = 0.5 * base * height
Reactangle_Area = height * width
Square_Area = height * height
Parallelogram_Area = base * height
Circle_Area = 3.14159 * radius * radius
Circumference = 2 * 3.14159 * radius

print("\n\n")

print("Area of a Triangle is : ",Triangle_Area)
print("Area of a Reactangle is : ",Reactangle_Area)
print("Area of a Square is : ",Square_Area)
print("Area of a Parallelogram is : ",Parallelogram_Area)
print("Area of a Circle is : ",Circle_Area)
print("Circumference of a circle : ",Circumference)