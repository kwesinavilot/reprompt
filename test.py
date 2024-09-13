from reprompt import Reprompt

reprompt = Reprompt()
original_prompt = "How do I bake a cake?"
improved_prompt = reprompt.generate_improved_prompt(original_prompt)
print(f"Original: {original_prompt}")
print(f"Improved:\n{improved_prompt}")