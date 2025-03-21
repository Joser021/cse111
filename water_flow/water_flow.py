# i add variables for Earth’s acceleration of gravity, the density of water, and the dynamic viscosity of water
# i add a function that converts kPa to psi and prints the result in psi

def water_column_height(tower_height, tank_height):
    """
    it calculates the height of a column of water.

    parameters
    tower_height: the height of the water.
    tank_height: is the height of the walls of the tank that is on top of the tower.
    return: height of the water column
    """

    water_column = tower_height + ((3 * tank_height) / 4)
    return water_column

def pressure_gain_from_water_height(water_density, earth_acceleration, height):
    """
    it calculates the pressure caused by Eath's gravity pullng on the water stored in an elevated tank.

    parameter
    height: is the height of the water column in meters
    return: the pressure in kilopascals
    """

    result = (water_density * earth_acceleration * height) / 1000
    pressure_gain = round(result, 3)
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, water_density, friction_factor, fluid_velocity):
    """
    it calculates the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.

    parameter
    friction_factor: is the pipe’s friction factor
    pipe_length: is the length of the pipe in meters
    fluid_velocity: is the velocity of the water flowing through the pipe in meters / second
    pipe_diameter: is the diameter of the pipe in meters
    return: the lost pressure in kilopascals
    """

    result = (-friction_factor * pipe_length * water_density * fluid_velocity ** 2) / (2000 * pipe_diameter)
    pressure_loss = round(result, 3)
    return pressure_loss

def pressure_loss_from_fittings(water_density, fluid_velocity, quantity_fittings):
    """
    it calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline.

    parameters
    fluid_velocity: is the velocity of the water flowing through the pipe in meters / second
    quantity_fittings: is the quantity of fittings
    return: the lost pressure in kilopascals
    """

    result = (-0.04 * water_density * (fluid_velocity ** 2) * quantity_fittings ) / 2000
    pressure_loss = round(result, 3)
    return pressure_loss

def reynolds_number(water_density, hydraulic_diameter, fluid_velocity, water_viscosity):
    """
    it calculates and returns the Reynolds number for a pipe with water flowing through it.

    parameters
    hydraulic_diameter: is the hydraulic diameter of a pipe in meters.
    fluid_velocity: is the velocity of the water flowing through the pipe in meters / second.
    return: the Reynolds number
    """

    result = (water_density * hydraulic_diameter * fluid_velocity) / water_viscosity
    reynolds_number_result = round(result, 3)
    return reynolds_number_result

def pressure_loss_from_pipe_reduction(water_density, larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    it calculates the water pressure lost because of water moving from
    a pipe witha large diameter into a pipe with a smaller diameter.


    parameters
    reynolds_number: the Reynolds number that corresponds to the pipe with the larger diameter
    large_diameter: the diameter of the larger pipe in meters
    smaller_diameter: is the diameter of the smaller pipe in meters
    
    ρ is the density of water (998.2 kilogram / meter3)
    fluid_velocity: is the velocity of the water flowing through the larger diameter pipe in meters / second

    return: the lost pressure kilopascals

    k = (0.1 + (50 / R)) ((D / d)^4 -1)

    P = -kpv² / 2000
    """

    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)

    result = (-k * water_density * (fluid_velocity ** 2)) / 2000
    pressure_loss = round(result, 3)
    return pressure_loss

def kpa_psi_converter(pressure_kpa):
    """
    it converts the pressure at house(result) to psi
    """

    pressure_psi = pressure_kpa * 0.145038
    return pressure_psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_density = WATER_DENSITY
    earth_acceleration = EARTH_ACCELERATION_OF_GRAVITY
    water_viscosity = WATER_DYNAMIC_VISCOSITY
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_density, earth_acceleration, water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(water_density, diameter, velocity, water_viscosity)
    loss = pressure_loss_from_pipe(diameter, length1, water_density, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(water_density, velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(water_density, diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, water_density, friction, velocity)
    pressure += loss
    pressure_psi = kpa_psi_converter(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} pounds per square inch")
    
if __name__ == "__main__":
    main()