import json

# Read the JSONL file
with open('output/predict_eval_predictions.jsonl', 'r') as file:
    lines = file.readlines()

# Create a dictionary to store datasets and instructions for each task
task_datasets_instructions = {}

# Extract and store "Task," "Dataset," and "Instruction" pairs
for line in lines:
    data = json.loads(line)
    task = data.get('Task')
    dataset = data.get('Dataset')
    instruction = data.get('Instance', {}).get('instruction', '')

    if "The output1 format" in instruction:
        instruction_before = instruction.split("The output format")[0].strip()
    elif "Output1 format" in instruction:
        instruction_before = instruction.split("Output format")[0].strip()
    else:
        instruction_before = None

    if task and dataset:
        task_dataset = (task, dataset)
        if task_dataset in task_datasets_instructions:
            task_datasets_instructions[task_dataset].add(instruction_before)
        else:
            task_datasets_instructions[task_dataset] = {instruction_before}

# Print the "Task," "Dataset," and corresponding unique "Instructions" sets
for (task, dataset), instructions in task_datasets_instructions.items():
    print(f'Task: {task}')
    print(f'Dataset: {dataset}')
    print(f'Instructions: {json.dumps(list(instructions))}')
    print()
