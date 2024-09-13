from reprompt import Reprompt

reprompt = Reprompt()
original_prompt = "is the earth round or flat?"
improved_prompt = reprompt.improve(original_prompt)
print(f"Original: {original_prompt}")
print(f"Improved:\n{improved_prompt}\n")

original_prompt = "how to bake cake?"
improved_prompt = reprompt.improve(original_prompt)
print(f"Original: {original_prompt}")
print(f"Improved:\n{improved_prompt}\n")

original_prompt = "what is the meaning of life?"
improved_prompt = reprompt.improve(original_prompt)
print(f"Original: {original_prompt}")
print(f"Improved:\n{improved_prompt}\n")