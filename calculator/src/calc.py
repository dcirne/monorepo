from compute import add, sub, mul, div
from termcolor import cprint

if __name__ == "__main__":
    answer = add(5, 10)
    answer = sub(answer, 1)
    answer = div(answer, 2)
    answer = mul(answer, 6)

    cprint(f"The answer to the ultimate question of life, the universe, and everything is: {answer}", "cyan")
