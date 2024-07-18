import openai

openai.api_key = "OPENAI_API_KEY"

content = input("What type of chatbot would you like to create?\n")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=[{"role": "user", "content": content}])
print(completion.choices[0].message.content)