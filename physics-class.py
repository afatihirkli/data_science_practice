# Codecademy Data Science Python Exercise : Getting Ready for Physics Class #
train_mass = 22680
train_acceleration = 10
train_distance = 100

impact_mass = 1
## Q1 ##
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp
## Q2 ##  
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
## Q3 ##
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) +32
  return f_temp
## Q4 ##
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
## Q5 ##
def get_force(mass, acceleration):
  return mass * acceleration
## Q6 ##
train_force = get_force(train_mass, train_acceleration)
print(train_force)
## Q7 ##
print("The GE train supplies ", train_force, " Newtons of force.")
## Q8 ##
def get_energy(mass, c = 3*10**8):
  return mass * c
## Q9 ##
impact_energy = get_energy (impact_mass)
## Q10 ##
print("A 1kg impact supplies ", impact_energy, " Joules.")
## Q11 ##
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
## Q12 ##
train_work = get_work(train_mass, train_acceleration, train_distance)
## Q13 ##
print("The GE train does ", train_work, " Joules of work over ", train_distance, " meters.")
