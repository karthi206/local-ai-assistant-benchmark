import ollama
import json
from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    name: str
    age: int
    city: str

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

for attempt in range(3):

    response = ollama.generate(
        model="mistral",
        prompt=prompt
    )

    try:
        data = json.loads(response['response'])
        person = Person(**data)
        print("Valid output:", person)
        break

    except (json.JSONDecodeError, ValidationError):
        print("Invalid output, retrying...")