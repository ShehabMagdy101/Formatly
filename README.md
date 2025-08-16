# Formatly

Formatly is an open-source tool for generating datasets tailored for fine-tuning large language models (LLMs) on domain-specific content.

Instead of relying solely on expensive API calls or powerful cloud GPUs, Formatly leverages lightweight local models (e.g., LLaMA 3.2) to generate high-quality training samples. This approach significantly reduces compute and API costs while maintaining dataset quality.

Formatly optimizes local machine performance by:

- Efficiently using available GPU and Optimizes CPU thread usage to avoid overloading the system during long runs.
- Applying a configurable cooldown to prevent hardware overheating
- Automatic and Fast extracting of semantically meaningful text chunks from PDFs using LangChain smart splitting
- Calculate and Estimate Precise time required for completing Dataset Generation

By default, Formatly generates Question–Answer–Explanation triplets for each text chunk, but supports multiple output formats for different fine-tuning frameworks.

## Supported Output Formats

- CSV (generic)
- Alpaca (Unsloth - llama3.2 - llama3.1)
- ShareGPT
- ChatML

## Architecture


![alt text](image.png)

The architecture includes:

- **PDF Parser** → Extracts and cleans raw text.
- **Smart Text Splitter** → Breaks content into logical, context-preserving chunks.
- **Model Interface** → Generates Q/A/Explanation using local or API-based models.
- **Dataset Formatter** → Saves in CSV, ChatML, Alpaca, or ShareGPT formats.
- **Fine-tuning Export** → Prepares ready-to-use datasets for cloud fine-tuning


## Installation


Install and Setup Ollama from (here)[https://ollama.com/]

in CMD run the following command (this will download the base model used in Formatly architecture):

```
ollama run llama3.2
```

Clone the repository:

```
git clone https://github.com/ShehabMagdy101/Formatly.git
cd Formatly

```
Create and activate a virtual environment:

```
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate

```

Install dependencies:

```
pip install -r requirements.txt
```
## How to Generate a Dataset using local model (llama3.2)
---


Go to folder `Formatly/src`:

```
cd src

```

Get help command:

```
python main.py --help
```

Run the `main.py` with the path to your PDF and the prefered data format (default is CSV):

```
python main.py --pdf "path/to/your/document.pdf" --format csv
```
![alt text](image-1.png)

After generatating 10 data points Formalty will calculate the estimated time required to finish all generated data in minutes
Formatly will show you a sample text chunk for user review
Formatly will ask you if you want to continue or discard operations for more manual edits in `config.py`
to continue input y or Y:

![alt text](image-2.png)

```
y
```

after choosing to continue you should find the dataset generated saved in `Formatly/data/processed`

<img width="233" height="69" alt="image" src="https://github.com/user-attachments/assets/dc0a9303-6d64-4cd9-bb2a-d45129739306" />



