# Turn book into Q/A/Explanation dataset

import os
import google.generativeai as genai
import json

# configure gemini API
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def generate_qa_explanation(text_chunk: str) -> dict:
    """
    Generates a question, answer, and explanation from given text chunk using Gemini API
    
    Args:
        text_chunk (str): The paragraph or chunk of text to be processed
    
    Returns:
        dict: A dictionary with 'question', 'answer', and 'explanation'
    """
    # instruction prompt
    prompt = f"""
    You are an assistant that creates educational datasets.
    Given the following text, generate:
    1. A clear and consise question about the content.
    2. A correct answer to that question.
    3. A detailed explanation of why that answer is correct.

    Text:
    {text_chunk}

    Respond ONLY in Valid JSON format as:
    {{
        "question": "...",
        "answer": "...",
        "explanation": "..."
    }}
    """
    model = genai.GenerativeModel("gemini-1.5-pro")

    response = model.generate_content(prompt)

    output_text = response.text.strip()
    # print(output_text)
    try:
        import regex as re
        qa_data = re.sub(r"^```[a-zA-Z]*\n","",output_text, flags=re.MULTILINE)
        qa_data = json.loads(re.sub(r"\n```$", "", qa_data, flags=re.MULTILINE))
    except json.JSONDecodeError:
        qa_data = {"question": None, "answer": None, "explanation": None}
    
    return qa_data


def create_dataset(texts: list[str], filename: str = "dataset.csv"):
    """
    Generate Q/A/Explanation dataset from a list of text chunks and save as CSV.
    
    Args:
        texts (list[str]): List of text chunks to process.
        filename (str): Name of the output CSV file (default 'dataset.csv').
    """
    try:
        output_dir = os.path.join("data", "processed")
        file_path = os.path.join(output_dir, filename)
    except Exception as e:
        return f"Cannot find folder path with error: {(e)}"

    import pandas as pd
    df = pd.DataFrame(columns=["question", "answer", "explanation"])
    
    print("Generating Dataset....\n")
   
    from tqdm import tqdm
    for text in tqdm(range(100, 101), desc="Generating Q&A"):
        json_data = generate_qa_explanation(texts[text])
        row = pd.DataFrame([json_data])
        df = pd.concat([df, row], ignore_index=True)
    
    print(f"Sample of generated data: \n",df.sample())
    print("Saving dataset...")
    print(f"Dataset saved to: {file_path}")
    df.to_csv(file_path, index=False, encoding="utf-8")
    return df

# example usage
if __name__ == "__main__":
    sample_text = """
    Conversation length can be an indicator of user engagement or inefficiency,
    depending on the chatbot's purpose. AI companions might benefit from long conversations,
    while productivity-focused chatbots may see them as inefficiency.
    """
    
    qa = generate_qa_explanation(sample_text)
    print(json.dumps(qa, indent=4))