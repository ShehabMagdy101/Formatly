import argparse
import config
path = config.PATH
from core.pdf_parser import process_pdf_to_chunks
from core.dataset_generator import create_dataset
from colorama import init, Fore, Style
init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Generate Q/A/Explanation dataset from PDFs")
    parser.add_argument(
        "--pdf",
        type=str,
        required=True,
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=['csv', 'alpaca', 'chatml', 'sharegpt'],
        default="csv",
        help="Output fromat: csv, jsonl, or openai"
    )
   
    args = parser.parse_args()

    print(Style.BRIGHT+ Fore.BLUE+ r""" 
 _____                          _   _         _             ____  _          _           _     
 |  ___|__  _ __ _ __ ___   __ _| |_| |_   _  | |__  _   _  / ___|| |__   ___| |__   __ _| |__  
 | |_ / _ \| '__| '_ ` _ \ / _` | __| | | | | | '_ \| | | | \___ \| '_ \ / _ \ '_ \ / _` | '_ \ 
 |  _| (_) | |  | | | | | | (_| | |_| | |_| | | |_) | |_| |  ___) | | | |  __/ | | | (_| | |_) |
 |_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\__, | |_.__/ \__, | |____/|_| |_|\___|_| |_|\__,_|_.__/ 
                                       |___/         |___/                                      
""")
    # process PDF into chunks
    chunks = process_pdf_to_chunks(args.pdf)

    # generate dataset with the right format
    df = create_dataset(chunks, format=args.format)  
    
        

if __name__ == "__main__":
    main()