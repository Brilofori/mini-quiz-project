answers = {'question_1':25,
        'question_2':2,
        'question_3':3}
#empty array for appending answers
emptyarr = []
#append result to list
def question_one(one):
    if one == answers['question_1']:
        emptyarr.append(one)
        print('correct!')
    else:
        print("incorrect")
        
def question_two(two):
    if two == answers['question_2']:
       emptyarr.append(two)
       print('correct!')
    else:
        print('incorrect!')    
       
def question_three(three):
    if three == answers['question_3']:
        emptyarr.append(three)
        print('correct!')
    else:  
        print('incorrect')
    
one = int(input("whats is 5x5: "))
two = int(input("what is 1+1: "))
three = int(input('what is 10+10: '))

question_one(one)
question_two(two)
question_three(three)


#next we can think of hwo to improve this. e.g specify how many were corrrect out of 3