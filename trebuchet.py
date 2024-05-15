import re


def calibration_sum(
    input_calibration: list[str], enable_word_to_number: bool = True
) -> int:
    """
    Extracts first and last integers from input list items and sums them.

    Note: If only one digit is present in an input string, then it is treated as both first and last integers.
          In other words, every input string will result in a two digit integer.
    """
    digits_search = re.compile(r"\d{1}")
    expanded_search = re.compile(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    )
    cal_sum: int = 0

    for val in input_calibration:
        if enable_word_to_number:
            matches = expanded_search.findall(val)
            matches = [convert_word_to_number(m) for m in matches]
        else:
            matches = digits_search.findall(val)
        cal_val = "".join([matches[0], matches[-1]])
        cal_sum += int(cal_val)

    return cal_sum


def convert_word_to_number(cal_string: str) -> str:
    digit_lookup = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return digit_lookup[cal_string]
