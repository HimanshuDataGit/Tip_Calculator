print("Welcome to the tip calculator.")
Bill = float(input('What was the total bill?: $'))
Percentage = float(input('What percentage tip would you like to give?: %'))
no_of_people = int(input('How many people you are splitting the bill with? '))
print('You should pay: $'+str(round((Bill*Percentage/100),2)))
print('Each person should pay: $'+str(round(((Bill*Percentage/100)/no_of_people),2)))

