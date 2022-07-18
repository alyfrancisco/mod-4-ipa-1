'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    person_1 = social_graph[from_member]
    person_2 = social_graph[to_member]
    x = to_member in person_1["following"]
    y = from_member in person_2["following"]
    if x == True and y == True:
           return "friends"
    elif x == True and y == False:
           return "follower"
    elif x == False and y == True:
           return "followed by"
    else: 
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i=0
    horizontal_line = [b for b in board]
    vertical_line = [b for b in zip(*board)]
    diagonal_line1=[board[i][i] for i,v in enumerate(board)]
    diagonal_line2=[board[2-i][i] for i,v in enumerate(board)]
    for i,v in enumerate(board):
        if all(c=='X' for c in horizontal_line[i]) == True: 
            return 'X'
            i += 1
        elif all(c=='O' for c in horizontal_line[i]) == True: 
            return 'O'
            i += 1
        elif all(c=='X' for c in vertical_line[i]) == True: 
            return 'X'
            i += 1
        elif all(c=='O' for c in vertical_line[i]) == True:
            return 'O'
            i += 1
    for c in diagonal_line1:
        if all(c=='X' for c in diagonal_line1) == True:
            return 'X'
        elif all(c=='O' for c in diagonal_line1) == True:
            return 'O'
    for c in diagonal_line2:
        if all(c=='X' for c in diagonal_line2) == True:
            return 'X'
        elif all(c=='O' for c in diagonal_line2) == True:
            return 'O'
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i=0
    key_list=(list(route_map.keys()))
    flag=False
    flag2=False
    value=0
    if (first_stop,second_stop) in key_list:  
        return (route_map[(first_stop,second_stop)]["travel_time_mins"])
    else:
        while flag2==False:
            for v in key_list:
                i=key_list.index(v)
                if second_stop==key_list[i][-1] and flag==True:
                    value+=route_map[key_list[i]]["travel_time_mins"]
                    flag2=True
                    return(value)
                if flag==True:
                    value+=route_map[key_list[i]]["travel_time_mins"]
                if first_stop==key_list[i][0]:
                    flag=True
                    value=route_map[key_list[i]]["travel_time_mins"]