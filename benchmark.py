import time
import psutil
import ollama

model_name = "llama3.2:1b-instruct-q4_0"

prompt = "Explain Artificial Intelligence in simple terms."

start_memory = psutil.virtual_memory().used / (1024 ** 3)

start_time = time.time()
first_token_time = None
full_response = ""
 
response_stream = ollama.generate(
    model=model_name,
    prompt=prompt,
    stream=True
)

for chunk in response_stream:
    if first_token_time is None:
        first_token_time = time.time()
    full_response += chunk['response']

end_time = time.time()

end_memory = psutil.virtual_memory().used / (1024 ** 3)

latency = end_time - start_time
time_to_first_token = first_token_time - start_time if first_token_time else 0
tokens = len(full_response.split())

tokens_per_second = tokens / latency


print("Key Metrics to measure the performance of the model\n")
print("Model:", model_name)
print("Response:", full_response)
print("Time to First Token:", time_to_first_token, "seconds")
print("Latency:", latency, "seconds")
print("Memory before start:",start_memory,"GB")
print("Memory after end:",end_memory,"GB")
print("Tokens Generated:", tokens)
print("Tokens Per Second:", tokens_per_second)
print("Memory Used:", end_memory - start_memory, "GB")