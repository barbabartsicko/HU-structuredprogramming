#het hulp van https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
text = input("voer text in:  ")
rotatie = int(input("voer rotatie in: "))

def caesar(txt, rot):
  caesarcijfer = ""
  for i in text:
    if i.isalpha():
      alphabet = ord(i) + rotatie
      if alphabet > ord('z'):
        alphabet -= 26
      Letter = chr(alphabet)
      caesarcijfer += Letter
  print ("Your ciphertext is: ", caesarcijfer)
  return caesarcijfer

caesar(text, rotatie)