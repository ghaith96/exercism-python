import re

VALID_PHONE_REGEX = r"[2-9]{1}\d{2}[2-9]{1}\d{6}"


class PhoneNumber:
    def __init__(self, number: str):
        self.number: str = "".join([digit for digit in number if digit.isdigit()])
        self.number = self.number[1:] if self.number[0] == "1" else self.number
        self.area_code: str = self.number[:3]

        if not re.fullmatch(VALID_PHONE_REGEX, self.number):
            raise ValueError(f"invalid number: {number}")

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
