# SpencerP2.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 08/30/2024
# Purpose: Provide a user some information about a state of their choice and display their results.
# Python Version: 3.12.5
import time

# Print a greeting message to the user
print('Congratulations! \nYou have found the State Savvy program!')
print('This program will provide you with information about a state of your choice.')


# Create a list for all 50 states
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# Have the user enter a state for query
find_state = input("\nLet's get started! \nPlease enter a state name: ")

# If user provides a state that is not in the list, display a message and exit the program
if find_state not in states:
    print('State not found')
    exit()

# Find the index of the state
state_index = states.index(find_state)

# Interim message to the user to make code more interactive
print('\nFinding information about', find_state, '\nThis should only take a moment...')
time.sleep(3.5)

# Create a list of state capitals
state_capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St. Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

# Create a list of districts for each state
state_districts = [7, 1, 9, 4, 52, 8, 5, 1, 28, 14, 2, 2, 17, 9, 4, 4, 6, 6, 2, 8, 9, 13, 8, 4, 8, 1, 3, 4, 2, 12, 3, 26, 14, 1, 15, 5, 6, 17, 2, 7, 1, 9, 38, 4, 1, 11, 10, 2, 8, 1]
# Create a variable to determine if the state has one or more districts then display the correct word
district = 'district' if state_districts[state_index] == 1 else 'districts'

# Create a parallel list for the chronological order of states joining the union
order_joined_union = [22, 49, 48, 25, 31, 38, 5, 1, 27, 4, 50, 43, 21, 19, 29, 34, 15, 18, 23, 7, 6, 26, 32, 20, 24, 41, 37, 36, 9, 3, 47, 11, 12, 39, 17, 46, 33, 2, 13, 8, 40, 16, 28, 45, 14, 10, 42, 35, 30, 44]

# sort the order of states joining the union to be in the correct chronological order
# and create the variables to access the correct index
join_index_for_order = order_joined_union[state_index]
sort_order = sorted(order_joined_union)

# Use the returned index to create the ordinal number for when the state joined the union
sorted_order = sort_order.index(join_index_for_order) + 1


# Create endings for ordinal dates
ending = (
        ['st', 'nd', 'rd']       # 1-3
        + 17 * ['th'] +          # 4-20
        ['st', 'nd', 'rd'] +     # 21-23
        7 * ['th'] +             # 24-30
        ['st', 'nd', 'rd'] +     # 31-33
        7 * ['th'] +             # 34-40
        ['st', 'nd', 'rd'] +     # 41-43
        7 * ['th']               # 44-50
          )

# Create variable for suffix to access the ordinal index
suffix_ending = ending[sorted_order - 1]

# create variable for displaying correct ordinal number with ending
ordinal = str(sorted_order) + suffix_ending

# Display results to the user
print('\nThe state capital for', find_state, 'is', state_capitals[state_index])
print(find_state, 'was the', ordinal, 'state to join the union')  # add order of state joining the union
print('As of 2024, the current U.S. Census reported that,', find_state, 'has', state_districts[state_index], 'congressional', district)

# Print a closing message to the user
time.sleep(4)
print('Thank you for using the State Savvy program! \nHave a great day!')
print('If you enjoyed using this program, please feel free to start following my progress on my github page:')
print('https://github.com/trudruskii')