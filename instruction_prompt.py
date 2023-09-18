import json
import random

with open("configs/instruction_config.json", 'r') as f:
    instruction_config = json.load(f)

def generate_instruction_prompts(num_prompts=8):
    # Initialize a list to store all prompts
    all_prompts = []

    # Loop through each section in the instruction config
    for section, instructions in instruction_config.items():
        if section in {'RC'} : continue
        # Create template prompts for the section
        prompts = [instruction['instruction'] for instruction in instructions]
        
        # Extend the list of all prompts with prompts from this section
        all_prompts.extend(prompts)

    # Randomly sample 'num_prompts' instructions from all sections
    sampled_instructions = random.sample(all_prompts, num_prompts)

    # Create the final header and combine prompts into a single string
    header = "Come up with various instructions for information extraction tasks, i.e. Coreference Resolution, Relation Extraction, Aspect Extraction, Argument Mining etc."
    instruction_string = "\n".join([f"{idx}. {instruction}" for idx, instruction in enumerate(sampled_instructions, start=1)])

    return f"{header}\n{instruction_string}\n{num_prompts + 1}."
# Example usage:
if __name__ == "__main__":
    instruction_prompts = generate_instruction_prompts(num_prompts=10)
    # instruction_prompts = generate_instruction_prompts("configs/instruction_config.bak")
    print(instruction_prompts)
