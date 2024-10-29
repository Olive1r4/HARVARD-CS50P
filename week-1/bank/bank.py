def main():
    n = input("Greetings: ").lower()
    valortopay(n)

def valortopay(valor):
    if valor[0:5] == "hello":
        print("$0")
    elif valor[0] == "h" and valor[1:5] != "ello":
        print("$20")
    else:
        print("$100")
if __name__ == "__main__":
    main()