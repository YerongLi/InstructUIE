import json

# Read the JSONL file
with open('output/predict_eval_predictions.jsonl', 'r') as file:
    lines = file.readlines()

# Create and write formatted instances to a JSONL file
with open('seed_task_ie.jsonl', 'w') as jsonl_file:
    for idx, line in enumerate(lines):
        data = json.loads(line)
        task = data.get('Task')
        instruction = None
        
        # Check if "The output format" or "Output format" is in the instruction
        instruction_str = data.get('Instance', {}).get('instruction', '')
        if "The output format" in instruction_str:
            instruction = instruction_str.split("The output format")[0].strip()
        elif "Output format" in instruction_str:
            instruction = instruction_str.split("Output format")[0].strip()
        
        instance = {
            "id": f"seed_task_{idx}",
            "name": task,
            "instruction": instruction,
            "input": data.get('Instance', {}).get('sentence', ''),
            "output": data.get('Prediction', ''),
            "is_classification": False
        }
        
        jsonl_file.write(json.dumps(instance) + '\n')
