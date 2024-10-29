def main():
    n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    answer(n)


def answer(a):
    match a:
        case "42":
            print("Yes")
        case "forty Two":
            print("Yes")
        case "forty two":
            print("Yes")
        case "forty-two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":

    main()