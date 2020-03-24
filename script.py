def ground_shipping(weight):
  if weight <= 2:
    return weight*1.50 + 20
  elif weight > 2 and weight <= 6:
    return weight*3.00 + 20
  elif weight > 6 and weight <= 10:
    return weight*4.00 + 20
  else:
    return weight*4.75 + 20

print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    return weight*4.50
  elif weight > 2 and weight <= 6:
    return weight*9.00
  elif weight > 6 and weight <= 10:
    return weight*12.00
  else:
    return weight*14.25

print(drone_shipping(1.5))

def cheapest_method(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    print("The cheapest shipping method for " + str(weight) + " is ground shipping.")
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    print("The cheapest shipping method for " + str(weight) + " is drone shipping.")
  else:
    print("The cheapest shipping method for " + str(weight) + " is premium ground shipping.")

cheapest_method(4.8)
cheapest_method(41.5)
