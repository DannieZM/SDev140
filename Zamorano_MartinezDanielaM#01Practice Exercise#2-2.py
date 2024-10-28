def calculate_cube(edge_length):
    """calculate the surface area"""
    
    ''' returns surface area '''
    return 6 * (edge_length**2)

'''User enters the length of cube'''
edge_length = int(input("Enter the length of the cube: "))

surface_area = calculate_cube(edge_length)


#output the surface area
print(f"The surface area of the cube is: {surface_area}")
