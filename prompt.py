import json
import random

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
            prompt = f"{idx}. {instruction['instruction']}"
            prompts.append(prompt)

        # Create the final header and combine prompts into a single string
        header = "Come up with various instructions for information extraction tasks, Coreference Resolution, Relation Extraction, Aspect Extraction, Argument Mining"
        instruction_string = "\n".join(prompts)

        return f"{header}\n{instruction_string}"
    else:
        return ""

# Example usage:
if __name__ == "__main__":
    instruction_prompts = generate_instruction_prompts("configs/instruction_config.json")
    print(instruction_prompts)
