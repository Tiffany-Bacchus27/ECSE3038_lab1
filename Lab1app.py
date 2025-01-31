# Question 1 (5mks) 

def parallel(resistors):
    if not resistors:
        print("No resistors provided.")
        return
    
    reciprocals = [1 / r for r in resistors]
    total_sum = sum(reciprocals)
    
    if total_sum == 0:
        print("Infinite resistance")
    else:
        effective_resistance = 1 / total_sum
        print("Effective resistance: " + str(round(effective_resistance, 3)) + " ohms")

# resistors = [330,1000,2200]
resistors = [20, 30, 60]
parallel(resistors)



# Question 2 (5mks)

def potential_divider(resistors, total_voltage):

    total_resistance = sum(resistors)
    for i in  range(len(resistors)):
        voltage_drop = (resistors[i] / total_resistance * total_voltage)
        print("Voltage drop across resistor", i + 1, ":", voltage_drop, "V")


resistors= [10, 5, 3]
total_voltage =  9
potential_divider(resistors, total_voltage)



# Question 3 (5mks)

def temperature_check(unit, temp):
    limits = {
        'C': {'hypothermic': 35.5, 'hyperthermic': 38.5},
        'F': {'hypothermic': 95.9, 'hyperthermic': 101.3}
    }

    if unit in limits: 
        if temp < limits[unit]['hypothermic']:
            print("The patient is hypothermic.")
        elif temp > limits[unit]['hyperthermic']:
            print("The patient is hyperthermic.")
        else:
            print("The patient has a normal body temperature.")


temperature_check('C', 36.5)
temperature_check('F', 104.0)      