# A program that takes in a credit number, and checks if it is a valid number.
# If it is a valid number, the program prints the type of card.

def main():
    number = input('Number: ')
    if (valid_length(number) and number.isnumeric()):
        if (valid_number(number)):
            print(get_card_type(number))
        else:
            print('INVALID')
    else:
        print('INVALID')


# Number comes in as a string
def valid_length(num):
    if len(num) < 13:
        return False
    elif len(num) == 14:
        return False
    elif len(num) > 16:
        return False
    else:
        return True


# Luhn's check sum algorithm
def valid_number(num):
    num = num[::-1]  # Reverse number so we can iterate more easily
    # Add up every other digit starting from the end of the number
    first_sum = 0
    for i in range(len(num)):
        if i % 2 != 0:
            n = int(num[i]) * 2
            if n > 9:  # Add up individual digits, not nums. ex) if n*2 == 10, add 1, then 0 to first_sum
                first_sum += n // 10
                first_sum += n % 10
            else:
                first_sum += n
    # Now add first sum to every other digit originally skipped over
    second_sum = first_sum
    for j in range(len(num)):
        if j % 2 == 0:
            m = int(num[j])
            second_sum += m
    # If number ends with 0, it's a valid number
    if second_sum % 10 == 0:
        return True
    else:
        return False


# Check first digits of number
def get_card_type(num):
    if len(num) == 15:  # AMEX
        if num[0:2] in ['34', '37']:
            return 'AMEX'
        else:
            return 'INVALID'
    elif len(num) == 13:  # VISA
        if num[0] == '4':
            return 'VISA'
        else:
            return 'INVALID'
    elif len(num) == 16:  # VISA or MASTERCARD
        if num[0] == '4':
            return 'VISA'
        elif int(num[0:2]) in range(51, 56):
            return 'MASTERCARD'
        else:
            return 'INVALID'
    else:
        return 'INVALID'


main()