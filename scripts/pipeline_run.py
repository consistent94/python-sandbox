from extract import extract
from transform import transform
from load import load
from analyse import analyze

def run_pipeline():
    print("Starting ETL pipeline...")
    extract()
    transform()
    load()
    analyze()   
    print("ETL pipeline completed successfully.")

if __name__ == '__main__':
    run_pipeline()