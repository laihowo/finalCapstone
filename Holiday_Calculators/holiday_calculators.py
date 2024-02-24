'''This program is for calculating the total holiday cost, 
which includes the hotel cost, plane cost, and car-rental cost.'''

def hotel_cost(num_nights):
    '''Calculate hotel cost based on number of nights'''
    return num_nights * 140

def plane_cost(city_flight):
    '''Calculate plane cost based on destination'''

    if city_flight in flight_price:
        return flight_price[city_flight]

    print('Destination is not available and we assume',
        'you do not buy the boarding pass via our program.')
    return 0

def car_rental(rental_days):
    '''Calculate car rental cost based on number of rental days'''
    return rental_days * 30

def holiday_cost(hotel_cost, plane_cost, car_rental):
    '''Calculate total holiday cost'''
    return hotel_cost + plane_cost + car_rental

# Print the flight cost for each city
flight_price = {'New York': 2000, 'Auckland': 790, 'Venice': 154, 'Glasgow': 65}
for city in flight_price:
    print(f'The flight to {city} costs ${flight_price[city]}.')
print()

# Initialize the variables
city_flight = ''
num_nights = 0
rental_days = 0
print('Enter "-1" at any time to quit.')

# Loop to handle user input
while True:
    try:
        # Prompt and validate the input of destination
        city_flight = input('Enter the city will be flying to: ').title()
        if city_flight == '-1':
            exit()

        # Prompt and validate the input of number of nights
        num_nights = int(input('Enter the number of nights will be staying at a hotel: '))
        if num_nights == -1:
            exit()

        # Prompt and validate the input of number of rental days
        rental_days = int(input('Enter the number of days for which will be hiring a car: '))
        if rental_days == -1:
            exit()

        if num_nights < 0 or rental_days < 0:
            raise ValueError
        print()
        break
    except ValueError:
        print('Please enter a non-negative integer.')

# Calculate the expenses of hotel, flight and car-rental
hotel_expense = hotel_cost(num_nights)
plane_expense = plane_cost(city_flight)
car_expense = car_rental(rental_days)

# Print the expenses and total cost of the holiday
print(f'The cost of the hotel is ${hotel_expense}.')
print(f'The cost of the plane is ${plane_expense}.')
print(f'The cost of the car rental is ${car_expense}.')
print('The total cost of the holiday is',
    f'${holiday_cost(hotel_expense, plane_expense, car_expense)}.')
