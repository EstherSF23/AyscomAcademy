from source.logging import logger
from source.extract import load_sales

def main():
    print("Hello")
    df = load_sales()

if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")