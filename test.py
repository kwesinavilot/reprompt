from reprompt_1 import PromptEngineer

engineer = PromptEngineer()
original_prompt = "How do I bake a cake?"
improved_prompt = engineer.generate_improved_prompt(original_prompt)
print(f"Original: {original_prompt}")
print(f"Improved: {improved_prompt}")