import ollama

prompt = """
Extract information and return JSON only.

Text:
John is a 25 year old developer living in Chennai.

Output format:
{
 "name": "",
 "age": "",
 "city": ""
}
"""

temperatures = [0.9, 0.5, 0.1]

for temp in temperatures:

    print("\nTemperature:", temp)

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={"temperature": temp}
    )

    print(response['response'])