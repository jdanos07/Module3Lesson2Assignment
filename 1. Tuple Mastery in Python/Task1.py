# Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples 
# as an argument. Each tuple contains information about a flight itinerary: (traveler_name, 
# origin, destination). The function should format and return a string that lists each itinerary.
 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"



def flight_itineraries():

    itineraries = {}
    indvidual_itinerary = []
    while True:
        itinerary_build = input('Is there an itinerary to input? Yes/No ').lower()
        if itinerary_build == 'yes':
            traveler_name = input('Input travelers full name. As printed on ID: ')
            poe = input('Input travelers starting location: ') #port of entry
            pod = input('Input travelers destination: ') #port of debarkation

            new_itinerary = ((
                traveler_name,
                poe,
                pod
            ))

            indvidual_itinerary.append(new_itinerary)

            intinerary_id = f'Itinerary {len(itineraries)+1}'
            itineraries[intinerary_id] = new_itinerary
        else:
            "Terminating Program"
            break

        for key, itinerary in itineraries.items():
            if itinerary:
                print(f'{key} - {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}')

flight_itineraries()