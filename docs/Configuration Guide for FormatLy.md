# 🛠️ Configuration Guide for FormatLy

This document explains all configuration variables available in the project, their purpose, usage, and possible values. These settings control model behavior, dataset generation, and system performance.

---

## 🔑 Authentication

### `API_KEY`

* **Purpose**: Stores your API key for connecting to external LLM services (if using a cloud-hosted model instead of a local one).
* **Default**: `""` (empty string).
* **Possible Values**:

  * Your provider’s API key (e.g., Gemini).
  * Leave empty when running only **local models**.

---

## 📂 File Paths

### `PATH`

* **Purpose**: Defines the directory path where input files (PDFs, docs) are located or where output datasets will be saved.
* **Default**: `r""` (empty).
* **Possible Values**:

  * Any valid **absolute or relative path**.
  * Example: `r"C:\Users\Shehab\Documents\datasets"`

---

## 📖 Document Processing

### `START_PAGE`

* **Purpose**: Sets the starting page when extracting text from a PDF or document. Useful for skipping introductory pages.
* **Default**: `21`.
* **Possible Values**:

  * Any integer ≥ 1.
  * Example: `1` (start from the beginning).

---

## 🤖 Model Settings

### `LOCAL_MODEL`

* **Purpose**: Specifies the local LLM to use for text generation.
* **Default**: `'llama3.2'`.
* **Possible Values**:

  * `'llama3.2'`, `'mistral'`, `'qwen'`, etc.
  * Must be installed/available in your environment.

### `TEMPERATURE`

* **Purpose**: Controls randomness of the generated output.
* **Default**: `0.7`.
* **Range**: `0.0 – 1.5`.

  * `0.0` → deterministic & factual.
  * `1.0+` → creative, diverse, but less predictable.

### `TOP_P`

* **Purpose**: Nucleus sampling – probability cutoff for token selection.
* **Default**: `0.9`.
* **Range**: `0.0 – 1.0`.

  * Lower values = focused, safe outputs.
  * Higher values = more diversity.

### `NUM_CTX`

* **Purpose**: Maximum context window (number of tokens the model can “see”).
* **Default**: `1024`.
* **Possible Values**:

  * Depends on the model (e.g., LLaMA 3.2 may support 4K–8K).

### `NUM_PREDICT`

* **Purpose**: Maximum tokens the model will generate in a response.
* **Default**: `256`.
* **Possible Values**:

  * Any positive integer (limited by GPU/CPU memory).

### `NUM_THREADS`

* **Purpose**: Number of CPU threads allocated for model inference.
* **Default**: `4`.
* **Possible Values**:

  * Typically set to the number of CPU cores available.
  * Example: `8` for an 8-core CPU.

---

## 📝 Prompt Template

### `PROMPT_TEMPLATE`

* **Purpose**: Defines the structure of the input prompt given to the LLM.
* **Default**:

```text
You are an assistant that creates educational datasets.
Given the following text, generate:
1. A clear and concise question about the content.
2. A correct answer to that question.
3. A detailed explanation of why that answer is correct.

Text:
{text}

Respond ONLY in Valid JSON format as:
{
    "question": "...",
    "answer": "...",
    "explanation": "..."
}
```

* **Notes**:

  * More Prompts can be found in `Prompt Templates` folder in Docs
  * The `{text}` placeholder will be replaced with the input chunk.
  * Output must strictly follow **valid JSON format**.

---

## ✂️ Text Chunking

### `CHUNK_SIZE`

* **Purpose**: Maximum number of characters per text chunk (before being sent to the model).
* **Default**: `600`.
* **Possible Values**:

  * Larger chunks → fewer calls, but heavier on context length.
  * Smaller chunks → more precise, but slower.

### `CHUNK_OVERLAP`

* **Purpose**: Number of overlapping characters between consecutive chunks. Helps preserve context between splits.
* **Default**: `50`.
* **Possible Values**:

  * Any integer ≥ 0.
  * Example: `100` → ensures smoother transitions.

---

## ⏳ Cooldown & Throttling

### `COOLDOWN`

* **Purpose**: Enables or disables cooldown to prevent system overload.
* **Default**: `True`.
* **Possible Values**:

  * `True` → cooldown enabled.
  * `False` → no cooldown.

### `COOLDOWN_ITERATIONS`

* **Purpose**: Number of iterations before cooldown triggers.
* **Default**: `100`.
* **Possible Values**: Any integer ≥ 1.

### `COOLDOWN_TIME`

* **Purpose**: Sleep time (in seconds) once cooldown is triggered.
* **Default**: `10`.
* **Possible Values**: Any positive integer (in seconds).

---

## 🌡️ System Limits

### `MAX_TEMP`

* **Purpose**: Defines the maximum safe system temperature (°C). Helps prevent overheating when running models locally.
* **Default**: `80`.
* **Possible Values**:

  * Any safe CPU/GPU threshold for your hardware.
  * Example: `75` for laptops, `90` for high-end GPUs.

