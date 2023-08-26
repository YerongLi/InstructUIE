import json

# Read the JSONL file
with open('output/predict_eval_predictions.jsonl', 'r') as file:
    lines = file.readlines()

# Create a dictionary to store datasets for each task
task_datasets = {}

# Extract and store "Task" and "Dataset" pairs
for line in lines:
    data = json.loads(line)
    task = data.get('Task')
    dataset = data.get('Dataset')
    
    if task and dataset:
        if task in task_datasets:
            task_datasets[task].add(dataset)
        else:
            task_datasets[task] = {dataset}

# Print the "Task" and corresponding "Dataset" sets
for task, datasets in task_datasets.items():
    print(f'{{"Task": "{task}", "Dataset": {json.dumps(list(datasets))}}}')
