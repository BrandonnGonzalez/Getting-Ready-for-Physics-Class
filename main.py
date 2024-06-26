train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# converts farenheit temperature to celsius.
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

# converts celsius temperature to farenheit.
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)
  return f_temp

c0_in_fahrenheit = c_to_f(0)

# Gets the force of an object by multiplying the mass of it times the acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)


print("The GE train supplies", str(train_force) + " " + "Newtons of force")

# Finds the energy within something, by multiplying its mass by the speed of light constant "c" squared.
def get_energy(mass, c = 3*10**8):
  return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies ", str(bomb_energy) + " ", "Joules.")

# Gets the overall workload of an object by calling the previous get_force() function, and including our inputs that need to be calculated.
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does ", str(train_work) + " ",  "Joules of work over ", str(train_distance) + " ", "meters")
