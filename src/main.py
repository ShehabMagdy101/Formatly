import config
path = config.PATH
from core.pdf_parser import process_pdf_to_chunks
from core.dataset_generator import create_dataset

def main():
    print(r""" 
 _____                          _   _         _             ____  _          _           _     
 |  ___|__  _ __ _ __ ___   __ _| |_| |_   _  | |__  _   _  / ___|| |__   ___| |__   __ _| |__  
 | |_ / _ \| '__| '_ ` _ \ / _` | __| | | | | | '_ \| | | | \___ \| '_ \ / _ \ '_ \ / _` | '_ \ 
 |  _| (_) | |  | | | | | | (_| | |_| | |_| | | |_) | |_| |  ___) | | | |  __/ | | | (_| | |_) |
 |_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\__, | |_.__/ \__, | |____/|_| |_|\___|_| |_|\__,_|_.__/ 
                                       |___/         |___/                                      
""")
    create_dataset(process_pdf_to_chunks(path))

if __name__ == "__main__":
    main()