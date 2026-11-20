import json

p_date = input ("1.Give me the date of the task.  ")
p_subclass = input ("2.Give me the subclass of the task.  ") # (test, homework, groupswork, reading, presentation, ...)
p_name = input ("3.Give me the name of the task.  ")
p_task = p_date + "_" + p_subclass + "_" + p_name
task_JSON = {"date": p_date, "subclass": p_subclass, "name": p_name}
#print(type(task_JSON))
with open ("to-do-list.json", mode = 'w') as f:
    json.dump(task_JSON, f)
#p_task = json.dumps(task_JSON)
#print(type(p_task))
#print(type(task_JSON))
with open ("to-do-list.json", mode = 'r') as f:
    p_class = json.load(f)
print(p_class)
