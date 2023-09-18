import json
import random

def generate_schema_prompts(config_file, num_prompts=8):
    # Load instruction config from the JSON file
    with open(config_file, 'r') as f:
        instruction_config = json.load(f)

    # Initialize a list to store all prompts
    all_prompts = []

    # Loop through each section in the instruction config
    for section, instructions in instruction_config.items():
        if section in {'RC'}: continue
        # Create prompts with both "instruction" and "schema" fields
        prompts = [f"{instruction['instruction']} \nSchema: {instruction['schema']}" for instruction in instructions if 'schema' in instruction]
        
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
    instruction_prompts = generate_schema_prompts("configs/instruction_config.json", num_prompts=12)
    print(instruction_prompts)
