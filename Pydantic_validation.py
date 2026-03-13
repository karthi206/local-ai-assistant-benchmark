import ollama
import json
import re
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

prompt = """
Extract the information from the text.

Return ONLY JSON.

Text:
John is a 25 year old developer living in Chennai.

Output format:
{
 "name": "string",
 "age": number,
 "city": "string"
}
"""

response = ollama.generate(
    model="mistral",
    prompt=prompt
)

output = response['response']

print("MODEL OUTPUT:\n", output)

# Extract JSON block
match = re.search(r'\{.*\}', output, re.DOTALL)

if match:
    json_text = match.group()
    data = json.loads(json_text)   # convert JSON → dictionary

    print("PARSED DATA:", data)

    person = Person(**data)

    print("\nVALIDATED OBJECT:", person)

else:
    print("No JSON found in output")