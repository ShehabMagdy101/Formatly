import config
path = config.PATH
from core.pdf_parser import process_pdf_to_chunks
from core.dataset_generator import create_dataset

def main():
    create_dataset(process_pdf_to_chunks(path))

if __name__ == "__main__":
    main()