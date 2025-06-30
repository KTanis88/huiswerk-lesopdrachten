def caesar_cipher(text, shift) :
    result = ""
    shift = shift % 26
    for char in text :
        if char.isalpha():
            start = ord('A') if char.isupper() else ord("a")
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char
    return result

def caesar_cipher_interactief() :
    while True:
        action = input("Typ 'encode' to encrypt, typ 'decode' to decode:\n") .strip() .lower()
        if action not in ['encode', 'decode'] :
            print("Ongeldige keuze. Typ 'encode' of 'decode'.")
            continue
        text = input("Typ je boodschap:\n")
        try:
            shift = int(input("Typ het shift nummer:\n"))
        except ValueError :
            print("Voer een geldig getal in voor de shift.")
            continue
        if action == 'decode':
            shift = -shift
        result = caesar_cipher(text, shift)
        print(f"de {action}d tekst is : {result}\n")
        again = input("Wil je overnieuw encrypten/decrypten? (J/N)\n").strip().lower()
        if again not in ['j', 'ja', 'y', 'yes']:
            print("Bedankt voor het gebruiken van de applicatie.")
            break

if __name__ == "__main__" :
    caesar_cipher_interactief()