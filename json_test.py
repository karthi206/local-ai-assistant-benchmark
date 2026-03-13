import ollama

prompt = """
Extract the following information and return ONLY JSON.

Text:
John is a 25 year old software developer living in Chennai.

Output format:
{
 "name": "",
 "age": "",
 "city": ""
}
"""

response = ollama.generate(
    model="mistral",
    prompt=prompt
)

print(response['response'])