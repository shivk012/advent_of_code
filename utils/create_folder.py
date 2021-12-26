# Create the folder structure for advent of code for a particular year

import click
import os
import requests
from dotenv import load_dotenv
from templates import PYTHON_TEMPLATE

load_dotenv()

URL = "https://adventofcode.com/"
SESSION = os.getenv("SESSION")


@click.command()
@click.argument("year", type=int)
@click.argument("day_in", type=int)
@click.argument("day_out", type=int)
@click.argument("language", type=str)
def create_folder(year, day_in, day_out, language):
    dir_path = os.getcwd()

    if not os.path.exists(os.path.join(dir_path, str(year))):
        os.mkdir(os.path.join(dir_path, str(year)))

    for day in range(day_in, day_out + 1):
        if not os.path.exists(os.path.join(dir_path, str(year), str(day))):
            os.mkdir(os.path.join(dir_path, str(year), str(day)))
            
        r = requests.get(f"{URL}{year}/day/{day}/input", cookies={"session": SESSION})
        if r.status_code == 200:
            with open(os.path.join(dir_path, str(year), str(day), "input.txt"), "w") as f:
                f.write(r.text)
        else:
            print(f"Error with {day=}", r.status_code)

        if language == "python":
            with open(os.path.join(dir_path, str(year), str(day), "main.py"), "w") as f:
                f.write(PYTHON_TEMPLATE)
        else:
            print(f"Error: {language} is not a valid language")


if __name__ == "__main__":
    create_folder()
