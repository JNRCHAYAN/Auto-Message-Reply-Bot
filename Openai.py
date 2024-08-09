
## This feature is paid user only
from openai import OpenAI

client = OpenAI(
    api_key= "#",

)
comand = '''
Copy Past chat here
'''

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a person named chayan who speaks English as well as bangla. He is form Bangladesh and is a coder. You analiye chat history and respond like chayan"},

    {"role": "user", "content": comand}
  ]
)

print(completion.choices[0].message.content)


