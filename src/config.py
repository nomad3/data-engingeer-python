import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE_PATH = os.path.join(BASE_DIR, '../data/tweets.csv')
    LOG_FILE_PATH = os.path.join(BASE_DIR, '../logs/app.log')

    # Processing parameters
    BATCH_SIZE = 10000  # If you are processing in batches

    # Other parameters
    TOP_N = 10
