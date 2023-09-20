import json
import random

# Define the categories you want to sample
categories_to_sample = ["RE", "EEA", "NER", "EET"]

# Create dictionaries to store instances for each category
instances_by_category = {category: [] for category in categories_to_sample}

# Read the JSONL file and categorize instances
with open('seed_task_ie.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        category = data['name']
        instances_by_category[category].append(data)

# Randomly sample 2 instances from each category
sampled_instances = {}
for category in categories_to_sample:
    sampled_instances[category] = random.sample(instances_by_category[category], 2)
idx = 1
print('Generate as many inforomation extraction problem with specified format, in the predefined schema not every field have to have a ground truth value:')
# Print the sampled instances along with instruction, input, and output
for category, instances in sampled_instances.items():
    # print(f"{category} samples:")
    for i, instance in enumerate(instances, start=1):
        print(f"{idx}.\nInstruction:")
        idx+= 1
        print(instance['instruction'])
        print("Input:")
        print(instance['input'])
        print("Output:")
        print(instance['output'])
        print()
