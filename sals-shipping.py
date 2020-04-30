## Codecademy Data Science Course Python Exercise : Sal's Shipping ##

## Q1 ##
def cost_of_ground_shipping(weight):
  flat_charge = 20
  if weight <= 2:
    return weight * 1.5 + flat_charge
  elif weight > 2 and weight <= 6:
    return weight * 3.0 + flat_charge
  elif weight > 6 and weight <= 10:
    return weight * 4.0 + flat_charge
  elif weight > 10:
    return weight * 4.75 + flat_charge
## Q2 ##
print(cost_of_ground_shipping(8.4))
## Q3 ##
cost_of_premium_ground_shipping = 125.0
## Q4 ##
def cost_of_drone_shipping(weight):
  flat_charge = 0
  if weight <= 2:
    return weight * 4.5 + flat_charge
  elif weight > 2 and weight <= 6:
    return weight * 9.0 + flat_charge
  elif weight > 6 and weight <= 10:
    return weight * 12.0 + flat_charge
  elif weight > 10:
    return weight * 14.25 + flat_charge
## Q5 ##
print(cost_of_drone_shipping(1.5))
## Q6 ##
def cheapest(weight):
  cost_of_premium_ground_shipping = 125.0
  if cost_of_ground_shipping(weight) < cost_of_premium_ground_shipping and cost_of_ground_shipping(weight) < cost_of_drone_shipping(weight):
    return " Ground shipping is the cheapest with " + str(cost_of_ground_shipping(weight))
  elif cost_of_premium_ground_shipping < cost_of_ground_shipping(weight) and cost_of_premium_ground_shipping < cost_of_drone_shipping(weight):
    return " Premium ground shipping is the cheapest with " + str( cost_of_premium_ground_shipping)
  elif cost_of_drone_shipping(weight) < cost_of_ground_shipping(weight) and cost_of_drone_shipping(weight) < cost_of_premium_ground_shipping :
    return " Drone shipping is the cheapest with " + str(cost_of_drone_shipping(weight))

## Q7 ##
print(cheapest(4.8))
print(cheapest(41.5))
