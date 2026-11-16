n_task = input ("1.Give me the name of the task.  ")
d_task = input ("2.Give me the date of the task.  ")
s_task = input ("3.Give me the subclass of the task.  ") # (test, homework, groupswork, reading, presentation, ...)
task = s_task + "_" + n_task + "_" + d_task
print(task)