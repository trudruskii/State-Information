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


# Create the lists to establish parallel connections
# Create a list of states
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# Have the user enter a state to find
find_state = input("\nLet's get started! \nPlease enter a state name: ")
if find_state not in states:
    print('State not found')
    exit()

# Find the index of the state
state_index = states.index(find_state)

# Interim message to the user
print('\nFinding information about', find_state, '\nThis should only take a moment...')
time.sleep(3.5)

# Display the state index
print('The state index is:', state_index)

# Create a list of state capitals
state_capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St. Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

# Create a list of districts for each state
congressional_state_districts = [7, 1, 9, 4, 52, 8, 5, 1, 28, 14, 2, 2, 17, 9, 4, 4, 6, 6, 2, 8, 9, 13, 8, 4, 8, 1, 3, 4, 2, 12, 3, 26, 14, 1, 15, 5, 6, 17, 2, 7, 1, 9, 38, 4, 1, 11, 10, 2, 8, 1]

# Create list of when state joined the union
# state_joined_union = ['December 14, 1819', 'January 3, 1959', 'February 14, 1912', 'June 15, 1836', 'September 9, 1850', 'August 1, 1876', 'January 9, 1788', 'December 7, 1787', 'March 3, 1845', 'January 2, 1788', 'August 21, 1959', 'July 3, 1890', 'December 3, 1818', 'December 11, 1816', 'December 28, 1846', 'January 29, 1861', 'June 1, 1792', 'April 30, 1812', 'March 15, 1820', 'April 28, 1788', 'February 6, 1788', 'January 26, 1837', 'May 11, 1858', 'December 10, 1817', 'August 10, 1821', 'November 8, 1889', 'March 1, 1867', 'October 31, 1864', 'June 21, 1788', 'December 18, 1787', 'January 6, 1912', 'July 26, 1788', 'November 21, 1789', 'November 2, 1889', 'March 1, 1803', 'November 16, 1907', 'February 14, 1859', 'December 12, 1787', 'May 29, 1790', 'May 23, 1788', 'November 2, 1889', 'June 1, 1796', 'December 29, 1845', 'January 4, 1896', 'March 4, 1791', 'June 25, 1788', 'November 11, 1889', 'June 20, 1863', 'May 28, 1848', 'July 10, 1890']

state_joined_union = [1819, 1959, 1912, 1836, 1850, 1876, 1788, 1787, 1845, 1788, 1959, 1890, 1818, 1816, 1846, 1861, 1792, 1812, 1820, 1788, 1788, 1837, 1858, 1817, 1821, 1889, 1867, 1864, 1788, 1787, 1912, 1788, 1789, 1889, 1803, 1907, 1859, 1787, 1790, 1788, 1889, 1796, 1845, 1896, 1791, 1788, 1889, 1863, 1848, 1890]

sorted_years = sorted(state_joined_union)
print(sorted_years)
print(sorted_years[32])
join_year = state_joined_union[state_index]
order_of_joining = sorted_years.index(join_year)
print('The order is:', order_of_joining)

# print(state_joined_union[state_index])
# state_joined_union.sort()
# print(state_joined_union.index(1817))


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

suffix = ending[order_of_joining % 100]



# print(suffix)

# Display results to the user

print('The state capital for', find_state, 'is', state_capitals[state_index])
print(find_state, 'joined the union on', state_joined_union[state_index], 'making it the', 'state to join the union')  # add order of state joining the union
print('As of 2024, based on the current data from the United States Census,', find_state, 'has', congressional_state_districts[state_index], 'congressional districts.')
