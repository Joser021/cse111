"""
store_efficiency = volume / surface_area

# volume = π radius² height

surface_area = 2π radius (radius + height)

# use math module

main()

storage_efficiency()

volume()

surface_area()
"""

from math import pi
data_sizes = [
    ["#1 Picnic", 6.83, 10.16, 0.28],
    ["#1 Tall", 7.78, 11.91, 0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5", 10.32, 11.91, 0.61],
    ["#3 Cylinder", 10.79, 17.78, 0.86],
    ["#5", 13.02, 14.29, 0.83],
    ["#6Z", 5.40, 8.89, 0.22],
    ["#8Z short", 6.83, 7.62, 0.26],
    ["#10", 15.72, 17.78, 1.53],
    ["#211", 6.83, 12.38, 0.34],
    ["#300", 7.62, 11.27, 0.38],
    ["#303", 8.10, 11.11, 0.42]
]



# the main part of the code, reading the file and displaying the result
def main():
    for line in data_sizes:
        # parts of the list
        names = line[0]
        radius = line[1]
        heights = line[2]
        costs = line[3]

        # calling functions and setting parameters
        volume = compute_volume(radius, heights)
        surface_area = compute_surface_area(radius, heights)
        store_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, costs)

        print(f"{names:12} {store_efficiency:.2f}   ${cost_efficiency:.2f}")


# functions to finde the volume, surface_area, storage efficiency and cost efficiency
def compute_volume(radius, height):
    """
    it calculates the volume of a cylinder, in this case the volume of a can
    """
    volume = pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    """
    it calculates the surface area of a cylinder, in this case the surface area of a can
    """
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """
    it calculates the store efficiency of a cylinder, in this case the store efficiency of a cylinder
    """
    store_efficiency = volume / surface_area
    return store_efficiency

def compute_cost_efficiency(volume, costs):
    cost_efficiency = volume / costs
    return cost_efficiency

# it runs the code
main()