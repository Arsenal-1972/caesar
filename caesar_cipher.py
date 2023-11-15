abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Funkcija a definē alfabetu
def encription(text, rotation): # Funkcija e definē šifru
  r = ""
  for c in text: 
    if (abc.find(c) == -1):
      r += c
    else:
      r += (abc[(abc.find(c) + rotation) % len(abc)])
  return r

def decription(text, rotation): # Funkcija d definē atšifrēšanas funkciju
  r = ""
  for c in text: 
    if (abc.find(c) == -1): 
      r += c
    else:
      r += (abc[(abc.find(c) - rotation) % len(abc)])
  return r

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1: # Definē šifra šifrēšanas funkciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encription(text, rotation))
elif mode == 2: # Definē atšifrēšanas funkciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decription(text, rotation))
elif mode == 3: # Definē bruteforce funkciju
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
