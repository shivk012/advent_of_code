# Create the folder structure for advent of code for a particular year

import click
import os
import requests
from dotenv import load_dotenv
from templates import PYTHON_TEMPLATE
from bs4 import BeautifulSoup

load_dotenv()

URL = "https://adventofcode.com/"
SESSION = os.getenv("SESSION")


def get_test_input(year, day):
    """Get the test input for a particular day. Makes a best guess at the test data by looking for 
    the code blocks and ignoring ones with em or span tags"""

    url = f"{URL}{year}/day/{day}"
    response = requests.get(url, cookies={"session": SESSION})
    soup = BeautifulSoup(response.text, "html.parser")

    all_code = soup.find_all("pre")

    code_with_no_tag = [
        x for x in all_code if (not x.find("em") and not x.find("span"))
    ]
    if not code_with_no_tag:
        code_with_no_tag = [x for x in all_code if not x.find("span")]

    code = " " if not code_with_no_tag else code_with_no_tag[0].text

    return code


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
            with open(
                os.path.join(dir_path, str(year), str(day), "input.txt"), "w"
            ) as f:
                f.write(r.text)
        else:
            print(f"Error with {day=}", r.status_code)

        if language == "python":
            with open(os.path.join(dir_path, str(year), str(day), "main.py"), "w") as f:
                code = PYTHON_TEMPLATE.replace("<TEST_DATA>", get_test_input(year, day))
                f.write(code)
        else:
            print(f"Error: {language} is not a valid language")


if __name__ == "__main__":
    create_folder()
