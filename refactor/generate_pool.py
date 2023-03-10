"""
Module provided by Mova801
A simple module that creates a pool of random integers in a given range and store them to a file.
The values are associated with specific prefixed characters.
The characters in the pool are:
' ', A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l,
m, n, o, p, q, r, s, t, u, v, w, x, y, z, ?, \", \#, $, %, &, ', (, ), *, +, -, ., ',', /, {, |, }, ~
"""
import random
import logging

# number of values to associate to each char
NUM_ASSOCIATED_VAL: int = 4

# range min value (included)
MIN: int = 0

# range max value (excluded)
MAX: int = 1000000001

# generated file name
FILENAME: str = "pool.csv"

logging.basicConfig(format=f'[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def main() -> None:
    def generate_randint_list(dim: int) -> tuple:
        """
        Return a list of random int between MIN and MAX of length :param dim:.
        :param dim: length of the list
        :return: random int list
        """
        return tuple(random.randint(MIN, MAX) for _ in range(dim))

    def format_values() -> str:
        """
        Format a list of values and associate it to a character, return a :type str:
        Format:
        - remove first and last char (assumed '[' and ']' as it is a list->str)
        - remove spaces
        - add newline (\\n)
        - associate to a character
        :return: formatted values
        """
        return f"{char},{str(values)[1:-1].replace(' ', '')}"

    characters: list = [
        '\' \'', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U',
        'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '?', '\"', '\#', '$', '%', '&', '\'', '(', ')', '*', '+', '-', '.',
        ',', '/', '{', '|', '}', '~'
    ]
    values: tuple[int] = tuple()
    logging.info(f"Opening {FILENAME} file")
    with open(FILENAME, 'w') as file:
        for char in characters:
            values = generate_randint_list(NUM_ASSOCIATED_VAL)
            formatted_vals = format_values()
            file.write(formatted_vals + "\n")
            logging.info(f"stored in {FILENAME}: {formatted_vals}")
    logging.info(f"Closed {FILENAME} file")
    logging.info(f"Task completed successfully! Check your file '{FILENAME}'")
    input("\nPress any key to exit...")


if __name__ == "__main__":
    logging.info(f"Script started")
    main()
