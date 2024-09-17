import re

category_pattern = r"\[\w+\]\.\w+$"

def verify_protocol(file_name: str):
    return bool(re.search(category_pattern, file_name))