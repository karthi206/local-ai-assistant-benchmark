# Local AI Assistant Benchmark

This project benchmarks **Small Language Models (SLMs)** running locally using **Ollama**.
The goal is to evaluate model performance, enforce structured outputs, and compare quantized models that can run on consumer hardware.

---

## Tech Stack

* Python
* Ollama
* Pydantic
* psutil (system resource monitoring)

Models Tested:

* Llama 3.2
* Mistral 7B

---

# Phase 1 – Performance Measurement

In this phase we benchmarked local models based on:

* **TTFT (Time To First Token)** – Time taken for the first word to appear
* **TPS (Tokens Per Second)** – Speed of token generation
* **Memory Usage** – RAM consumption during inference

### Results

| Model      | TTFT (s) | TPS (tokens/sec) | Memory Usage |
| ---------- | -------- | ---------------- | ------------ |
| Llama 3.2  | 6.99 s   | 1.87             | 2.09 GB      |
| Mistral 7B | 15.43 s  | 1.02             | 4.11 GB      |

### Observation

* **Llama 3.2** produced faster responses and used less memory.
* **Mistral 7B** showed higher latency and memory consumption on the tested hardware.

---

# Phase 2 – Structured Output Engineering

This phase ensures that the language model produces **reliable structured data**.

Implemented:

* JSON schema outputs
* Validation using Pydantic
* Retry mechanism for invalid responses
* Temperature experiments to observe response variability

---

## JSON Output Test

| Model      | JSON Output                                      |
| ---------- | ------------------------------------------------ |
| Llama 3.2  | {"name": "John", "age": "25", "city": "Chennai"} |
| Mistral 7B | {"name": "John", "age": "25", "city": "Chennai"} |

Observation:

Both models successfully generated **structured JSON outputs** following the prompt instructions.

---

## Pydantic Validation Test

| Model      | Output                            |
| ---------- | --------------------------------- |
| Llama 3.2  | name='John' age=25 city='Chennai' |
| Mistral 7B | name='John' age=25 city='Chennai' |

Observation:

Pydantic validated the output schema and automatically converted `"25"` (string) into `25` (integer).

---

## Retry Mechanism Test

| Model      | Result                        |
| ---------- | ----------------------------- |
| Llama 3.2  | Valid output on first attempt |
| Mistral 7B | Valid output on first attempt |

Observation:

The retry mechanism was implemented to handle invalid outputs, but it was **not triggered during testing** because both models returned valid structured outputs.

---

## Temperature Experiment

Temperature controls the **randomness of model responses**.

Lower temperature → more deterministic outputs
Higher temperature → more creative / variable outputs

### Temperature Test Results

| Model      | Temperature | Output Consistency                     |
| ---------- | ----------- | -------------------------------------- |
| Llama 3.2  | 0.1         | Stable structured JSON                 |
| Llama 3.2  | 0.5         | Slight variation but valid JSON        |
| Llama 3.2  | 0.9         | Higher randomness but schema preserved |
| Mistral 7B | 0.1         | Stable structured JSON                 |
| Mistral 7B | 0.5         | Slight variation                       |
| Mistral 7B | 0.9         | Increased randomness                   |

Observation:

Even with higher temperature values, both models maintained **valid JSON output when the prompt explicitly enforced the schema**.

# Phase 3 – Model Comparison and Quantization Study

This phase evaluates model performance using two approaches:

1. Comparison between the base models used in earlier experiments
2. Performance comparison of quantized variants of the same model

The experiments were conducted using **Ollama** to run models locally.

---

## Base Model Comparison

In this experiment we compared the two models used in Phase 1:

* Llama 3.2
* Mistral 7B

The comparison was based on:

* **TTFT (Time to First Token)** – response delay before the first generated word
* **TPS (Tokens Per Second)** – generation speed
* **Memory Usage** – RAM consumption during inference

### Results

| Model      | TTFT (s) | TPS (tokens/sec) | Memory  |
| ---------- | -------- | ---------------- | ------- |
| Llama 3.2  | 6.99 s   | 1.87             | 2.09 GB |
| Mistral 7B | 15.43 s  | 1.02             | 4.11 GB |

### Observation

* **Llama 3.2** generated responses faster and consumed less memory.
* **Mistral 7B** showed higher latency and memory usage on the tested hardware.
* Based on these metrics, **Llama 3.2 performed better for local deployment on resource-constrained systems**.

---

## Quantized Model Comparison

In this experiment we compared quantized variants of the Llama 3.2 model to understand how **model size and quantization affect performance**.

Quantized models reduce memory usage and improve inference speed by storing model weights with lower precision.

### Models Tested

* Llama 3.2 1B Q4
* Llama 3.2 3B Q4
* Llama 3.2 Default (~8B parameters)

### Benchmark Results

| Model             | Parameters | TTFT   | TPS (tokens/sec) | Memory  |
| ----------------- | ---------- | ------ | ---------------- | ------- |
| Llama 3.2 1B Q4   | 1B         | 0.22 s | 15.38            | 0.07 GB |
| Llama 3.2 3B Q4   | 3B         | ~4 s   | ~4               | 2.16 GB |
| Llama 3.2 Default | ~8B        | 1.24 s | 4.90             | ~3–5 GB |

Note: Minor memory fluctuations were observed due to background system processes during measurement.

---

## Key Insights

This experiment demonstrates an important trade-off in local AI deployment:

| Model Size  | Speed    | Memory  | Response Quality |
| ----------- | -------- | ------- | ---------------- |
| Small (1B)  | Fastest  | Lowest  | Basic            |
| Medium (3B) | Balanced | Medium  | Good             |
| Large (~8B) | Slower   | Highest | Best             |

Smaller quantized models are suitable for **low-resource systems**, while larger models may provide **higher response quality at the cost of performance and memory usage**.

# Conclusion

This project demonstrates how **local language models can be benchmarked and optimized for real-world usage**.

Using **Ollama**, developers can run and evaluate AI models locally while balancing **performance, memory consumption, and output quality**.

---

# Future Improvements

* Automated benchmark testing across multiple models
* Visualization of metrics (TPS, TTFT, Memory)
* Integration with cloud-based AI systems
* Local AI assistant interface

---

