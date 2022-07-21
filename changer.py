from collections import deque
from itertools import count
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
def changer():
    count = 0
    while True:
        selection = input("Should we get rid of a number?: ")
        if count == 2:
            print("No more numbers")
            break
        elif selection.lower() == "no":
            print("Ok we wont be taking any more numbers off")
            break
        elif selection.lower() == "yes":
            queue.popleft()
            print(queue)
        count += 1
        
     

while True:
    play = input("Shall we play?: ")
    if play.lower() == "yes":
        changer()
    else:
        print("We wont be playing I guess")
        break

    again = input("Shall we play again?: ")
    if again.lower() == "yes":
        changer()
    else:
        print("Maybe another time then")
        break
