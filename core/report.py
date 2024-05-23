import os
import json


def split_string(input_string: str, length: int):
    words = input_string.split()
    chunks = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= length:
            current_line += word + " "
        else:
            chunks.append(current_line.rstrip())
            current_line = word + " "
    chunks.append(current_line.rstrip())
    return chunks


def create_report(answer: str, temperature: float):

    chunks = split_string(answer, length=100)

    if not os.path.exists(os.path.join(os.getcwd(), "report.json")):
        fd = os.open(os.path.join(os.getcwd(), "report.json"), os.O_CREAT)
        os.close(fd)

    try:
        with open("report.json", "r") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        data = []

    new_data = {"temperature": temperature, "answer": chunks}
    data.append(new_data)

    with open("report.json", "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
