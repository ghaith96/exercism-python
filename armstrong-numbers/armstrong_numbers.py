def is_armstrong_number(number):
    str_num = f"{number}"
    number_len = len(str_num)
    raised_sum = sum([int(str_digit) ** number_len for str_digit in str_num])
    return (raised_sum == number)