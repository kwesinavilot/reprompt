# Reprompt

Reprompt is a Python library for improving and structuring prompts without relying on large language models (LLMs). It uses natural language processing techniques to analyze input prompts and generate more effective, structured prompts suitable for various AI applications.

## About Reprompt
The idea for Reprompt came after watching [a talk Zack Witten from Anthropic gave on prompt engineering](https://www.youtube.com/watch?v=hkhDdcM5V94) at the 2024 AI Engineer Conference. What stood out to me was how effective prompts could be, not just when they're written clearly, but when they are structured in a way that "guarantees" that the user gets what they want. 

This got me thinking: what if there was a tool that could take any prompt, understand the bigger picture of what the user is trying to achieve, and then refine it into a clearer, more concise version without extra work for the user?

I realized I'd have to use an LLM, most likely a small open source model. But I also realized that that'll be an extra call to an LLM, which may result in latency issues and even extra cost. Already, people are ok using whatever prompts they have so there's no need making an extra call to an LLM to refine the prompt which will later be giving to an LLM.

I thought it would be fun to create a tool that could help users get exactly what they need from their prompts, just by analyzing and restructuring them using native NLP techniques, without relying on large language models.

As can be seen, some of the best practices discussed in the talk are incorporated into Reprompt.

## Features

- Analyzes input prompts to identify key concepts and intent
- Generates structured prompts using XML tags
- Tailors instructions based on detected intent
- Incorporates best practices from the prompt engineering workshop given at the [2024 AI Engineer Conference by Zack Witten (Anthropic)](https://www.youtube.com/watch?v=hkhDdcM5V94)
- Operates without requiring integration with an LLM



# Installation
To install Reprompt, you need Python 3.6 or later

Currently, you can download the `reprompt.py` file and place it in a location that is accessible by your Python script. You can then import the Reprompt class as usual.

For example, if you place the reprompt.py file in the same directory as your script, you can import it like this:

```
from reprompt import Reprompt
```

Make sure to adjust the import statement according to the location of the reprompt.py file in your project.

I will update this documentation once the library is available on PyPI.


## Dependencies

Reprompt relies on the following Python libraries:

- nltk

You can install these dependencies using:

```
pip install nltk
```

## Usage

Here's a basic example of how to use Reprompt:

```python
from reprompt import Reprompt

reprompt = Reprompt()
original_prompt = "How do I bake a cake?"
improved_prompt = reprompt.improve(original_prompt)

print(f"Original: {original_prompt}")
print(f"Improved:\n{improved_prompt}")
```

This will output an improved prompt in XML format, structured with context, instructions, and output format

## Features in Detail

1. **Preprocessing**: Capitalizes input and performs basic grammar fixes.
2. **Key Concept Identification**: Identifies the most important words/phrases in the input.
3. **Intent Recognition**: Determines the likely intent of the prompt (e.g., instruction, definition, explanation).
4. **Structured Output**: Generates an XML-structured prompt with separate sections for context, instruction,and output format.
5. **Tailored Instructions**: Provides specific instructions based on the detected intent.

## Limitations

- Does not use machine learning or AI for deep understanding of prompts.
- Example generation isn't supported.
- May not handle complex or multi-faceted prompts effectively.
- Intent recognition is rule-based and may not capture all nuances.

## Contributing

It started of as a shower thought after watching the [2024 AI Engineer Conference by Zack Witten (Anthropic)](https://www.youtube.com/watch?v=hkhDdcM5V94) and thought to see if I could do it.

But I'm sure it could become something great and useful so I welcome contributions.

## License

Reprompt is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For contributions or any questions or issues, please open an issue on the GitHub repository or contact me at [andrewsankomahene@gmail.com].