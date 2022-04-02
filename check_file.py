import os

def do_this_with_file (filename,operation,content):
    if operation=='read':
        if os.path.isfile(filename):
            with open(filename, 'r') as fopen:
                if os.path.getsize(filename)==0:
                    print (f'Plik {filename} jest pusty ')
                else:
                    print(f"Wczytano plik {filename}")
                    return fopen.read()
        else:
            print (f"Plik {filename} nie istnieje ")
    elif operation =='write':
        if os.path.isfile(filename):
            with open(filename, 'w') as fopen:
                while True:
                    answer=str(input(f"Plik {filename} istnieje . Czy go nadpisac? T/N: "))
                    if answer=='T':
                        #with open(filename, 'w') as fopen:
                        fopen.write(content)
                        break
                    elif answer=='N':
                        print(f'Pliku {filename} nie zapisano ')
                        break
                    else:
                        print ("Niepoprawna odpowiedz. Spróbuj jeszcze raz")
        else:
            with open(filename, 'w') as fopen:
                print (f"Zapisano do pliku {filename}")
                fopen.write(content)
