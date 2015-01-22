#!/usr/bin/env python

small_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
              'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']

magnitude = ['', 'thousand', 'million', 'billion', 'trillion']

def num_to_string(num, add_and=True):
    """ Converts a number to its string representation.

    Examples:
        1 = "one"
        10 = "ten"
        15 = "fifteen"
        115 = "one hundred and fifteen"
    """
    # Make sure to convert to an integer
    num = int(num)

    if num == 0:
        return "zero"

    if num <= len(small_nums):
        return small_nums[num - 1]
    elif len(str(num)) == 2:
        string = tens[int(str(num)[0])]
        if str(num)[1] != "0":
            string += small_nums[int(str(num)[1])-1]
        return string

    if len(str(num)) == 3:
        string = num_to_string(int(str(num)[0])) + " hundred"
        if int(str(num)[1:]) > 0:
            if add_and:
                string += " and "
            string += num_to_string(int(str(num)[1:]))
        return string

    num_string = str(num)
    three_digit_nums = []
    while len(num_string) > 3:
        three_digit_nums.append(num_string[-3:])
        num_string = num_string[:-3]
    three_digit_nums.append(num_string)

    output = ""
    for i, item in enumerate(three_digit_nums):
        if len(three_digit_nums) > 1 and int(item) == 0:
            continue
        if i > 0:
            output = num_to_string(int(item), False) + " " + magnitude[i] + " " + output
        else:
            output = num_to_string(int(item)) + " " + magnitude[i] + " " + output

    return output

if __name__ == "__main__":
    s = 0
    for i in range(1, 1001):
        num_str = num_to_string(i)
        num_str = num_str.replace(" ", "")
        s += len(num_str)
    print s
