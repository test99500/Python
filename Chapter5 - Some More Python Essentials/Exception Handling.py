import numpy as np

def ask_user(a, b):
    """get answer from user: a*b = ?"""
    question = "{:d} * {:d} = ".format(a, b)
    answer = int(input(question))

    return answer


def points(a, b, answer_given):
    """Check answer. Correct: 1 point, else 0"""
    true_answer = a*b

    if answer_given == true_answer:
        print("Correct!")
        return 1
    else:
        print("Sorry! Correct answer was: {:d}".format(true_answer))
        return 0


print("\n*** Welcome to the times tables test! ***\n  (To stop: ctrl-c)")


N = 10
NN = N*N
score = 0
index = list(range(0, NN, 1))
np.random.shuffle(index)

for i in range(0, NN, 1):
    a = index[i] // N + 1
    b = index[i] % N + 1

    try:
        user_answer = ask_user(a, b)
    except:
        print("You must give a valid number!")
        continue # Jump to the next loop iteration

    score = score
