# Data Engineer Challenge Solution

## Overview

This project provides a solution to the Data Engineer challenge. The challenge involves processing a dataset of tweets to extract meaningful insights, such as the top 10 dates with the most tweets, the most used emojis, and the most influential users based on mentions.

The solution is implemented in Python, leveraging libraries such as `pandas` for data manipulation, `emoji` for handling emojis, and `memory-profiler` for measuring memory usage. The project follows a modular approach with clear separation between data loading, analysis, and testing.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Solution](#running-the-solution)
  - [Running Tests](#running-tests)
- [API Submission](#api-submission)
- [Technologies Used](#technologies-used)
- [Contact Information](#contact-information)

## Project Structure

```
project-root/
│
├── src/                     # Source code directory
│   ├── __init__.py          # Marks 'src' as a package
│   ├── config.py            # Application configuration
│   ├── data_loader.py       # Data loading logic
│   ├── analytics.py         # Tweet analysis logic
│   ├── main.py              # Main entry point to run analysis
│
├── tests/                   # Unit tests
│   ├── __init__.py          # Marks 'tests' as a package
│   ├── test_analytics.py    # Unit tests for analytics functions
│
├── data/                    # Contains data files (e.g., tweets.csv)
│   ├── tweets.csv           # Example dataset (or real data)
│
├── logs/                    # Log files
│   └── app.log              # Log file generated during execution
│
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── .gitignore               # Files to ignore in Git
├── solution.ipynb           # Jupyter notebook explaining the solution
```

## Installation

To set up this project on your local machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/data-engineer-challenge.git
cd data-engineer-challenge
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Solution

To run the analysis and get results for the top 10 dates with the most tweets, the most used emojis, and the most mentioned users, execute the `main.py` script:

```bash
python src/main.py
```

This will:

1. Load the dataset from `data/tweets.csv`.
2. Perform the analysis to extract the required insights.
3. Log the results and the memory usage in `logs/app.log`.

### Running Tests

Unit tests are provided to ensure the correctness of the analysis logic. To run the tests, use `pytest`:

```bash
pytest tests/test_analytics.py
```

The tests include:
- Testing the top 10 dates with most tweets.
- Testing the top 10 most used emojis.
- Testing the top 10 most mentioned users.

## API Submission

To submit the solution, you need to send a `POST` request with your project details to the API endpoint. You can do this with the provided script or manually using a tool like Postman.

To automate this, run the `submit_solution.py` script (make sure to replace your details):

```bash
python submit_solution.py
```

This sends your GitHub URL, name, and email to the challenge server.

```python
import requests

url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"
data = {
    "name": "Your Name",
    "mail": "your.email@example.com",
    "github_url": "https://github.com/your-username/data-engineer-challenge.git"
}

response = requests.post(url, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
```

## Technologies Used

- **Python 3.10+**: The core programming language.
- **pandas**: For data manipulation and processing.
- **emoji**: For handling emojis within the text.
- **memory-profiler**: For measuring memory usage.
- **pytest**: For unit testing.

## Contact Information

For any questions or clarifications, feel free to contact me:

- **Name**: Simon Aguilera
- **Email**: saguilera1608@gmail.com
- **GitHub**: [nomad3](https://github.com/nomad3)

