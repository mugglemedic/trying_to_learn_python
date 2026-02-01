#!/usr/bin/python3
# Physics Functions - Temperature conversion and force/energy calculations
# Demonstrates: functions, default parameters, lambda functions, unpacking

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Temperature Conversions
def f_to_c(f_temp):
    """Convert Fahrenheit to Celsius"""
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


def c_to_f(c_temp):
    """Convert Celsius to Fahrenheit"""
    f_temp = c_temp * 9 / 5 + 32
    return f_temp


# Physics Calculations
def get_force(mass, acceleration):
    """Calculate force using F = ma"""
    force = mass * acceleration
    return force


def get_energy(mass, c=3*10**8):
    """Calculate energy using E = mc²"""
    energy = mass * c**2
    return energy


def get_work(m, a, d):
    """Calculate work done: W = F × d"""
    work = get_force(m, a) * d
    return work


# Calculate train force
train_force = get_force(train_mass, train_acceleration)

# Calculate bomb energy
bomb_energy = get_energy(bomb_mass)

# Calculate train work (regular method)
train_work = train_mass * train_acceleration * train_distance

# Calculate train work (using lambda with unpacking)
train_deets = [train_mass, train_acceleration, train_distance]
train_work_lambda = (lambda x, y, z: x*y*z)(*train_deets)


# Display results
if __name__ == '__main__':
    print(f'Temperature conversions:')
    print(f'0°C in Fahrenheit: {c_to_f(0)}°F')
    print(f'100°F in Celsius: {f_to_c(100):.1f}°C')
    print()
    
    print(f'Physics calculations:')
    print(f'The GE train supplies {train_force:,} Newtons of force.')
    print(f'A 1kg bomb supplies {bomb_energy:,} Joules.')
    print(f'The GE train does {train_work:,} Joules of work over {train_distance} meters.')
    print(f'Lambda calculation result: {train_work_lambda:,} Joules')
