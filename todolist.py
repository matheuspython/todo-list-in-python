tasks = ['program', 'exercise myself', 'eat']#initial tasks placed on the list

def fillList():
    for i in tasks:
        print(i)

print("your tasks today are: ")
fillList()

questionToAddTheTaskList = 0

def userQuestions():
    questionToAddTheTaskList = input('do you want to add any new tasks? ')

    if questionToAddTheTaskList == 'yes' or questionToAddTheTaskList == 'yea' or questionToAddTheTaskList == 'yep':
        inputAddedToTaskList = input('which task you want to add to the list ')
        tasks.append(inputAddedToTaskList)

    elif questionToAddTheTaskList == 'not' or questionToAddTheTaskList == 'no' or questionToAddTheTaskList == 'non' or questionToAddTheTaskList == 'nay' or questionToAddTheTaskList == 'nope':
        print('ok')

    else:
        print('invalid response')


def deleteTaks():
    pass

userQuestions()
print('________')
fillList()