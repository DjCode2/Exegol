alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class CodeCesar:
    def __init__(self, cle):
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def decale(self, lettre):
        num = self.alphabet.find(lettre)
        decalage = (num - self.cle) % 26
        nouvelle_lettre = self.alphabet[decalage]
        return nouvelle_lettre

    def decryptage(self, message_crypte):
        message_clair = ""
        for lettre in message_crypte:
            if lettre.upper() in self.alphabet:
                message_clair += self.decale(lettre.upper())
            else:
                message_clair += lettre
        return message_clair

def decrypte(text):
    for cle in range(len(alphabet)):
        Cc=CodeCesar(cle)
        message_clair = Cc.decryptage(text)
        print('     ==================================')
        print("     Message decrypter:", message_clair)



print('''

                        ▀██▀▀▀▀█                                  ▀██
                         ██  ▄    ▄▄▄ ▄▄▄   ▄▄▄▄    ▄▄▄ ▄   ▄▄▄    ██
                         ██▀▀█     ▀█▄▄▀  ▄█▄▄▄██  ██ ██  ▄█  ▀█▄  ██
                         ██         ▄█▄   ██        █▀▀   ██   ██  ██
                        ▄██▄▄▄▄▄█ ▄█  ██▄  ▀█▄▄▄▀  ▀████▄  ▀█▄▄█▀ ▄██▄
                                                   ▄█▄▄▄▄▀



''')

print('     --------------------------------------------------------------------------------------')
print('         Bienvenu sur Exegol, le programme est une regroupement de plusieurs autres')
print("         Tel Nmap, Hydra, Gobuster et d'autres")
print('     --------------------------------------------------------------------------------------')

print('')
print('')


print('Que voulez vous faire ? ')
print('     1. Décripter un code Cesar.')
print('     2. Pas encore implémenter.')
print('     3. Pas encore implémenter.')
print('')
print('')

reponse=int(input("Saisissez le numéro souhaiter: "))
if reponse ==1:
    text=str(input("Saisissez le texte a décoder: "))
    print(decrypte(text))





#print(decrypte("PSX"))




