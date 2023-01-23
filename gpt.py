#!/usr/bin/env python
# Chat GPT integration
# Magnus Glantz, sudo@redhat.com, 2023
# https://github.com/mglantz/chatgpt/

import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_prompt = sys.argv[1]

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])
