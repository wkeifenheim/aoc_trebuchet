from logging import debug
from cal_input import cal_input
import re


def calibration_sum(input_calibration: list[str], enable_text_to_number: bool = True) -> int:
    """
    Extracts first and last integers from input list items and sums them.

    Note: If only one digit is present in an input string, then it is treated as both first and last integers.
          In other words, every input string will result in a two digit integer.
    """
    cal_sum: int = 0
    for val in input_calibration:
        if enable_text_to_number:
            val = convert_text_to_number(val)
        nums = [num for num in val if num.isnumeric()]
        cal_val = "".join([nums[0], nums[-1]])
        debug(cal_val)
        cal_sum += int(cal_val)

    return cal_sum


def convert_text_to_number(cal_string: str) -> str:
    """
    Replaces written representation of a number with its corresponding digit. Leaves the rest of the str alone.

    Input examples could be interpreted as being process left-to-right, however the actual solution only cares about the first and last.
    Anything in between the two bookend digits does not need to be converted.
    """
    digit_lookup = {
        "zero": "0",
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
    while True:
        found_keys = [(key, cal_string.find(key)) for key in digit_lookup.keys()]
        valid_indices = [index for _, index in found_keys if index >= 0]
        if any(valid_indices):
            target_key = next(key for key, _idx in found_keys if _idx == min(valid_indices))
            cal_string = cal_string.replace(target_key, digit_lookup[target_key], 1)
        else:
            break            
    
    return cal_string


search_pattern = re.compile(r"\d{1}|one|two|three|four|five|six|seven|eight|nine")
all_matches = search_pattern.findall("abcone2threexyz")