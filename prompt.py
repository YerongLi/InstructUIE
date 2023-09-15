import json
import random

def generate_instruction_prompts(config_file, num_prompts=8):
    # Load instruction config from the JSON file
    with open(config_file, 'r') as f:
        instruction_config = json.load(f)

    # Initialize a dictionary to store prompts from all sections
    all_prompts = {}

    # Loop through each section in the instruction config
    for section, instructions in instruction_config.items():
        # Randomly sample 'num_prompts' instructions from the section
        sampled_instructions = random.sample(instructions, num_prompts)

        # Create template prompts using the sampled instructions
        prompts = []
        for idx, instruction in enumerate(sampled_instructions, start=1):
            prompt = f"{idx}. {instruction['instruction']}"
            prompts.append(prompt)

        # Create the final header and combine prompts into a single string
        header = f"Come up with various instructions for {section}"
        instruction_string = "\n".join(prompts)

        # Store the prompts for this section in the dictionary
        all_prompts[section] = f"{header}\n{instruction_string}"

    # Add a placeholder for the 9th instruction
    all_prompts["9. Placeholder"] = ""

    # Combine prompts from all sections into a single string
    combined_prompts = "\n\n".join(all_prompts.values())

    return combined_prompts

# Example usage:
if __name__ == "__main__":
    instruction_prompts = generate_instruction_prompts("configs/instruction_config.json")
    print(instruction_prompts)
