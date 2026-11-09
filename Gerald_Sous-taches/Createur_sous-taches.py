#Welcome to the program that creates subtasks for you.
#Please choose one of the following options:
#1. Add a subtask
#2. Delete a subtask
#3. Exit the software
print("Give me the name of the task")
taks=input()
print("""What kind of task is it?
Choose one of following options:
1) Test
2) Homework
3) Reading
4) Groupswork
5) Presentation""")
k_task=int(input())
if k_task==1:
    print("Okay it is a test")
elif k_task==2:
    print("Okay it is a homework")
elif k_task==3:
    print("Okay it is a reading")
elif k_task==4:
    print("Okay it is a groupswork")
elif k_task==5:
    print("Okay it is a presentation")
else:
    print("Input is not valable")