""" You can return two things from a function. Look at the return
statement and the way the variables are saved from the function call """


def main():


    can_donate, reason = can_donate_blood(120, 19)
    if can_donate:
        print('You can donate blood - thank you!')
    else:
        print('You can not donate blood because ' + reason)


def can_donate_blood(weight, age):
    if age < 17:
        problem = 'you are not old enough, must be at least 17'
        return False, problem

    if weight < 110:
        problem = 'you do not weigh enough, must weigh at least 110lbs'
        return False, problem

    return True, None  # None replaces problem if there's no problem to return


main()