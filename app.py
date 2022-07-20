from random import randint, randrange, shuffle

# one_hundred_prisoners_problem








def o():
    '''Simulates the famous 100 prisoners problem'''
    PRISONERS = list(range(1, 101))
    cupboard = {}
    CUPBOARD_LABELS = (list(range(1, 101)))
    numbers_in_cupboard = (list(range(1, 101)))
    shuffle(numbers_in_cupboard)

    for label in CUPBOARD_LABELS:
        cupboard[label] = numbers_in_cupboard[CUPBOARD_LABELS.index(label)]
    
    status = ""
    prisoners_status = {}
    ATTEMPTS_LIST = list(range(1, 51)) 
    attempt_count = 50
    prisoner_attempts = [{prisoner: []} for prisoner in PRISONERS]
    print(prisoner_attempts[0])

    for prisoner in PRISONERS:
        choice = cupboard[prisoner]
        for attempt in ATTEMPTS_LIST:
            attempt_count -= 1
            if attempt_count == 0:
                status = "LOSE"
                prisoners_status[prisoner] = status
                break
            if attempt_count < 50:
                choice = cupboard[choice]
            if choice == prisoner:
                status = "WIN"
                prisoners_status[prisoner] = status
                break
            prisoner_attempts[prisoner.index()][prisoner].append("test")
        if status == "LOSE":
            break
    
    # return [f"PRISONERS STATUS: {prisoners_status}", f"CUPBOARD: {cupboard}", f""]




    







    


















