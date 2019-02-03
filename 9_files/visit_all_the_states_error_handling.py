""" A program for a user to keep track of states they have visited,
and states they have not visited.
"""


def main():

    visited = read_states_file('visited_states.data')
    all_states = read_states_file('states.data')

    print('These are the states you have visited:')
    print(visited)

    while True:
        new_state = input('Enter the name of the state you have visited or enter to quit.')
        if not new_state:
            break
        if new_state not in all_states:
            print('That is not a state name. Try again')
        else:
            visited.append(new_state)


    # Sort into alphabetical order and save.
    visited.sort()
    save_visited_states(visited, 'visited_states.data')


def read_states_file(filename):
    states_list = []
    try:
        with open(filename) as f:
            for state in f:
                state = state.strip()  # Remove newline
                states_list.append(state)
    except IOError:
        print(f'Warning - {filename} not found.')

    return states_list


def save_visited_states(states, filename):
    try:
        with open(filename, 'w') as f:
            for state in states:
                f.write(state)
                f.write('\n')
    except IOError:
        print('Error writing states file.')

main()

