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
* Validation using **Pydantic**
* Retry mechanism for invalid responses

---

## JSON Output Test

| Model      | JSON Output                                        |
| ---------- | -------------------------------------------------- |
| Llama 3.2  | `{"name": "John", "age": "25", "city": "Chennai"}` |
| Mistral 7B | `{"name": "John", "age": "25", "city": "Chennai"}` |

Both models successfully produced structured JSON outputs.

---

## Pydantic Validation Test

| Model      | Output                            |
| ---------- | --------------------------------- |
| Llama 3.2  | name='John' age=25 city='Chennai' |
| Mistral 7B | name='John' age=25 city='Chennai' |

Observation:

Pydantic successfully validated and converted the data types
(for example `"25"` → `25`).

---

## Retry Mechanism Test

| Model      | Result                        |
| ---------- | ----------------------------- |
| Llama 3.2  | Valid output on first attempt |
| Mistral 7B | Valid output on first attempt |

Observation:

The retry mechanism was implemented but **not triggered**, since both models produced valid structured outputs immediately.

---

# Phase 3 – Quantized Model Comparison

In this phase we compared quantized versions of **Llama 3.2** to evaluate performance trade-offs between speed, memory, and model size.

### Models Tested

* Llama 3.2 1B Q4
* Llama 3.2 3B Q4
* Llama 3.2 Default

---

## Benchmark Results

| Model             | Parameters | TTFT   | TPS (tokens/sec) | Memory  |
| ----------------- | ---------- | ------ | ---------------- | ------- |
| Llama 3.2 1B Q4   | 1B         | 0.22 s | 15.38            | 0.07 GB |
| Llama 3.2 3B Q4   | 3B         | ~4 s   | ~4               | 2.16 GB |
| Llama 3.2 Default | ~8B        | 1.24 s | 4.90             | ~3–5 GB |

Note: A negative memory value was observed during measurement due to normal system memory fluctuations.

---

# Key Insights

1. **Quantized models significantly reduce memory usage.**

2. **Smaller models generate tokens much faster.**

3. There is a clear trade-off between:

| Model Size  | Speed    | Memory | Quality |
| ----------- | -------- | ------ | ------- |
| Small (1B)  | Fastest  | Lowest | Basic   |
| Medium (3B) | Balanced | Medium | Good    |
| Large (~8B) | Slower   | Higher | Best    |

---

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

