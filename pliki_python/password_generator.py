import random
import string

"""
import itertools

x = list(itertools.permutations([1, 2, 3]))
print(x)
"""
"""
wymagnia
    duze litery
    małe litery
    cyfry
    znaki specjalne
    przynjamniej po 2 symbole z każdej z powyższych ategroii
    Długość min 8 znaków
    losowa kolejność znaków
    żeby ten skrypt działał

"""


def generate_password():
    # potrzebne dane
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    whole = lowercase + uppercase + digits + punctuation
    whole_in_list = [lowercase, uppercase, digits, punctuation]

    password_length = 0
    min_length = 8
    max_length = 20
    count_of_every_char = 2

    # użytkownik wejście
    password_length = 20
    """
    while not(min_length <= password_length <= max_length):
        # print(f"Twoje hasło nie może być krótsze niż {min_length} znaków, ani dłuższe niż {max_length} znaków")
        try:
            password_length = int(input('podaj długość hasła: '))
        except TypeError:
            print('coś poszło nie tak...')
    """

    # test czy mogę edytować plik w VSC
    # moge :)

    # program
    password = []
    for i in range(4):  # wymaganie łukasza żeby były po 2 znaki z każego typu
        x = random.sample(whole_in_list[i], count_of_every_char)  # zwraca [a, b]
        password += (''.join(x))  # rozpakowuje tę listę i dodaje osobno elemnty do listy

    for i in range(password_length-4*count_of_every_char):  # dopełnienie długości hasła losowymi symbolami
        x = random.sample(whole, 1)  # zwraca [a]
        password += (''.join(x))  # rozpakowuje tę listę i dodaje osobno elemnty do listy

    random.shuffle(password)
    fin_password = ''.join(password)

    # końcowy wynik
    return fin_password
