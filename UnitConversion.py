def calcFeet(amount):
    feet_yard = amount / 3
    feet_inch = amount * 12
    feet_cm = amount * 30.48
    feet_meter = amount / 3.28
    return feet_yard, feet_inch, feet_cm, feet_meter

def calcMeter(amount):
    meter_yard = amount * 1.09
    meter_inch = amount * 39.37
    meter_cm = amount * 100.00
    meter_feet = amount * 3.28
    return meter_yard, meter_inch, meter_cm, meter_feet

def calcYard(amount):
    yard_inch = amount * 36
    yard_cm = amount * 91.44
    yard_feet = amount * 3
    yard_meter = amount * 0.91
    return yard_inch, yard_cm, yard_feet, yard_meter

def calcInches(amount):
    inch_yard = amount * 0.02
    inch_meter = amount * 0.02
    inch_feet = amount * 0.08
    inch_cm = amount * 2.54
    return inch_yard, inch_meter, inch_feet, inch_cm

def calcCM(amount):
    cm_yard = amount * 0.01
    cm_meter = amount * 0.01
    cm_feet = amount * 0.03
    cm_inch = amount * 0.39
    return cm_yard, cm_meter, cm_feet, cm_inch

# Main
unit = input("Enter the unit you wish to convert (feet, meters, yards, inches):\t").upper()
amount = float(input("Enter the amount of " + unit + " you wish to convert:\t"))
if unit == "FEET":
    feet_yard, feet_inch, feet_cm, feet_meter = calcFeet(amount)
    print('')
    print(str(amount) + " foot is equal to %.2f" % + float(feet_inch) + " inches")
    print(str(amount) + " foot is equal to %.2f" % + float(feet_yard) + " yards")
    print(str(amount) + " foot is equal to %.2f" % + float(feet_cm) + " centimeters")
    print(str(amount) + " foot is equal to %.2f" % + float(feet_meter) + " meters")
elif unit == "METER":
    meter_yard, meter_inch, meter_cm, meter_feet = calcMeter(amount)
    calcMeter(amount)
    print('')
    print(str(amount) + " meter is equal to %.2f" % + float(meter_yard) + " yards")
    print(str(amount) + " meter is equal to %.2f" % + float(meter_inch) + " inches")
    print(str(amount) + " meter is equal to %.2f" % + float(meter_cm) + " centimeters")
    print(str(amount) + " meter is equal to %.2f" % + float(meter_feet) + " feet")
elif unit == "YARD":
    yard_inch, yard_cm, yard_feet, yard_meter = calcYard(amount)
    calcYard(amount)
    print('')
    print(str(amount) + " Yard is equal to %.2f" % + float(yard_inch) + " inches")
    print(str(amount) + " Yard is equal to %.2f" % + float(yard_meter) + " meters")
    print(str(amount) + " Yard is equal to %.2f" % + float(yard_feet) + " feet")
    print(str(amount) + " Yard is equal to %.2f" % + float(yard_cm) + " centimeters")
elif unit == "INCHES":
    inch_yard, inch_meter, inch_feet, inch_cm = calcInches(amount)
    calcInches(amount)
    print('')
    print(str(amount) + " Inch is equal to %.2f" % + float(inch_yard) + " yards")
    print(str(amount) + " Inch is equal to %.2f" % + float(inch_meter) + " meter")
    print(str(amount) + " Inch is equal to %.2f" % + float(inch_feet) + " feet")
    print(str(amount) + " Inch is equal to %.2f" % + float(inch_cm) + " centimeters")
elif unit == "CENTIMETER":
    cm_yard, cm_meter, cm_feet, cm_inch = calcCM(amount)
    calcCM(amount)
    print('')
    print(str(amount) + " Centimeter is equal to %.2f" % + float(cm_yard) + " yards")
    print(str(amount) + " Centimeter is equal to %.2f" % + float(cm_meter) + " meters")
    print(str(amount) + " Centimeter is equal to %.2f" % + float(cm_feet) + " feet")
    print(str(amount) + " Centimeter is equal to %.2f" % + float(cm_inch) + " inches")
else:
    print("You did not enter a proper unit, please select a unit from the following list:" + " Feet, Meter, Yard, Inch, Centimeter")
 
