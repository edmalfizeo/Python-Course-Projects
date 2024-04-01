import CeaserCipher
import art

print(art.logo)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    CeaserCipher.ceaserCipher(text,shift,cipher_direction=direction)
    want_continue = input("Do you want do continue? [Yes or No]").lower()

    if want_continue == "no":
        end = True
        print("GoodBye!")




