import json
import random
'''
Fill instructions into a big prompt
'''
def generate_instruction_prompts(config_file, num_prompts=8):
    # Load instruction config from the JSON file
    with open(config_file, 'r') as f:
        instruction_config = json.load(f)

    # Check if the "RE" key exists in the config
    if "RE" in instruction_config:
        # Randomly sample 'num_prompts' instructions from "RE"
        sampled_instructions = random.sample(instruction_config["RE"], num_prompts)

        # Create template prompts using the sampled instructions
        prompts = []
        for idx, instruction in enumerate(sampled_instructions, start=1):
            prompt = f"{instruction['instruction']}"
            prompts.append(prompt)

        return prompts
    else:
        return []

# Example usage:
if __name__ == "__main__":
    instruction_prompts = generate_instruction_prompts("configs/instruction_config.json")
    for idx, prompt in enumerate(instruction_prompts, start=1):
        print(f"{idx}. {prompt}")
