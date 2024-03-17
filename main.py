def verify_card_number(card_number):
    card_number_reversed = card_number[::-1]
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    # example valid card number: 4111-1111-4555-1142
    # example invalid card number: 4111-1111-4555-1141
    while True:
        card_number = input('Digite número de tarjeta [XXXX-XXXX-XXXX-XXXX]: ')
        card_translation = str.maketrans({'-': '', ' ': ''})
        translated_card_number = card_number.translate(card_translation)
        if not translated_card_number.isnumeric():
            print('INVALID FORMAT...')
        else:
            break

    if verify_card_number(translated_card_number):
        print('VALID CARD NUMBER!')
    else:
        print('INVALID CARD NUMBER!')


# If the program is run (instead of imported), run the main:
if __name__ == '__main__':
    main()