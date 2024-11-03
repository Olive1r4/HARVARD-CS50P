def main():
    m = input("Enter a name of the file: ").lower().strip()
    #print(get_extension(m))
    test_extension(get_extension(m))

#Retorna a extensão do arquivo
def get_extension(m):
    if "." in m:
        return m.split(".")[-1]
    else:
        return "application/octet-stream"
    
#Verifica o tipo de extensão do arquivo   
def test_extension(t):
    if t == "txt":
        print("image/gif")
    elif t == "jpg":
        print("image/jpeg")
    elif t == "jpeg":
        print("image/jpeg")
    elif t == "png":
        print("image/png")
    elif t == "pdf":
        print("application/pdf")
    elif t == "text":
        print("text/plain")
    elif t == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()