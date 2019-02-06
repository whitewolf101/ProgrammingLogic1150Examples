""" A program for a user to keep track of states they have visited,
and states they have not visited.
Make sure states.data nd visited_states.data exist before starting the program.

"""


def main():
    visited = read_states_file('visited_states.data')
    all_states = read_states_file('states.data')
    print('These are the states you have visited so far:')
    print(visited)

    while True:
        new_state = input('Enter a state you have visited (enter to quit) ')
        if not new_state:
            break
        if new_state not in all_states:
            print('That is not a state name. Try again')
        else:
            visited.append(new_state)

    visited.sort()     # Sort into alphabetical order
    save_visited_states(visited, 'visited_states.data')


def read_states_file(filename):
    states_list = []
    f = open(filename)
    for state in f:
        state = state.strip()  # Remove newline
        states_list.append(state)
    f.close()
    return states_list


def save_visited_states(states, filename):
    f = open(filename, 'w')
    for state in states:
        f.write(state)
        f.write('\n')
    f.close()


main()

