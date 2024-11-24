import difflib
import json
from typing import List, Union, Any
from config import ABSOLUTE_PATH


def check_lists_similarity(list1: List[dict], list2: List[dict]) -> Union[bool, List[str]]:
    """
    Compare two lists of dictionaries and return True if they are similar or a list of lines
    showing the differences between them.
    """
    list1_str = [json.dumps(item) for item in list1]
    list2_str = [json.dumps(item) for item in list2]

    difference = list(difflib.ndiff(list1_str, list2_str))

    if all(line.startswith(' ') for line in difference):
        return True
    else:
        return difference


def load_json_file(file_name: str) -> Any:
    """Load a JSON file and return its contents."""
    with open(f'{ABSOLUTE_PATH}/files/{file_name}', 'r') as file:
        return json.load(file)
