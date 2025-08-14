# include different formats ready for model fine-tuning
import json
import os
from colorama import Fore

# Aplaca - Unsloth 
def alpaca(df):
    '''
    Converts a Q/A/Explanation Dataframe to Alpaca format and saves as .jsonl
    '''

    filename =  "alpaca_dataset.jsonl"  
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(BASE_DIR, "data", "processed", filename)
    except Exception as e:
        return Fore.RED+f"Cannot find folder path with error: {(e)}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            instruction = f"Answer the question and provide an explanation: {row['question']}"
            output = f"{row['answer']}. {row['explanation']}"

            alpaca_item = {
                "instruction": instruction,
                "input": "",
                "output": output
            }
            f.write(json.dumps(alpaca_item, ensure_ascii=False)+ '\n')

    print(Fore.GREEN+ f"Alpaca dataset saved to {file_path}")


# ShareGPT
def sharegpt(df):
    """
    Converts a Q/A/Explanation DataFrame to ShareGPT format and saves as .jsonl in a given folder.
    """
    filename =  "sharegpt_dataset.jsonl"
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(BASE_DIR, "data", "processed", filename)
    except Exception as e:
        return Fore.RED+f"Cannot find folder path with error: {(e)}"
    
    with open(file_path, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            conversations = [
                {"from": "human", "value": f"{row['question']} Please explain."},
                {"from": "gpt", "value": f"{row['answer']}. {row['explanation']}"}
            ]
            
            sharegpt_item = {"conversations": conversations}
            f.write(json.dumps(sharegpt_item, ensure_ascii=False) + "\n")
    
    print(Fore.GREEN+ f" ShareGPT dataset saved to {file_path}")


# ChatML
def chatml(df):
    """
    Converts a Q/A/Explanation DataFrame to OpenAI ChatML format and saves as .jsonl in data/processed.
    """
    filename =  "chatml_dataset.jsonl"
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(BASE_DIR, "data", "processed", filename)
    except Exception as e:
        return Fore.RED + f"Cannot find folder path with error: {(e)}"
    
    with open(file_path, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{row['question']} Please explain."},
                {"role": "assistant", "content": f"{row['answer']}. {row['explanation']}"}
            ]
            
            chatml_item = {"messages": messages}
            f.write(json.dumps(chatml_item, ensure_ascii=False) + "\n")
    
    print(Fore.GREEN + f" ChatML dataset saved to {file_path}")

