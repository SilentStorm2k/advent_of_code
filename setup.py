import os
import requests # type: ignore
import argparse
import json
from bs4 import BeautifulSoup # type: ignore

def get_secret (key="session"):
    try:
        filename = "secrets.json"
        with open(filename) as f:
            data = json.load(f)
            return data.get(key)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading secrets file: {e}")
        return None


def extract_input(url):
    cookie = {
        "session": get_secret("session")
    }
    response = requests.get(url, cookies=cookie)
    soup = BeautifulSoup(response.content, 'html.parser')
    input_text = soup.text.strip()
    return input_text

def main():
    parser = argparse.ArgumentParser(description='Extract text from <p> tags of a given URL.')
    parser.add_argument('year', type=str, help='Year')
    parser.add_argument('day', type=str, help='Day')
    parser.add_argument('file_path', type=str, help='The file path to save input to')
    args = parser.parse_args()

    year = args.year
    day = int(args.day)
    inputFilePath = args.file_path
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    input = extract_input(url)
    
    if not os.path.exists(inputFilePath):
        with open(inputFilePath, 'a') as f:
            f.write(input)
        print(f"Successfully copied input into {inputFilePath}")
    else:
        print(f"{inputFilePath} already exists, skipping writing")

if __name__ == "__main__":
    main()