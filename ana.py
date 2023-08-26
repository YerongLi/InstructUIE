import json

# Read the JSONL file
with open('output/predict_eval_predictions.jsonl', 'r') as file:
    lines = file.readlines()

# Extract and print all "Task" strings
for line in lines:
    data = json.loads(line)
    task = data.get('Task')
    if task:
        print(task)
