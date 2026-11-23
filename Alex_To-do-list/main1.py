import json
p_date = input ("1.Give me the date of the task.  ")
p_subclass = input ("2.Give me the subclass of the task.  ") # (test, homework, groupswork, reading, presentation, ...)
p_name = input ("3.Give me the name of the task.  ")
p_task = p_date + "_" + p_subclass + "_" + p_name
task_JSON = {'date': p_date, 'subclass': p_subclass, 'name': p_name}
try:
    with open ("organisateur_scolaire.json", mode = 'r') as f:
        task = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    task = []
task.append(task_JSON)
with open ("organisateur_scolaire.json", mode = 'w') as f:
    json.dump(task, f)
with open ("organisateur_scolaire.json", mode = 'r') as f:
    task = json.load(f)
for 
