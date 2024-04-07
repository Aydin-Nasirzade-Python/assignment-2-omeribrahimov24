#import libraries here

def main(): 
vowel=["a","e","i","o","u"]
a=input("Enter a letter of the alphabet")
if a=="y":
    print("Sometimes it is a vowel, and sometimes it is a consonant!")
elif a in vowel:
    print("Entered alphabet is a vowel!")
else:
    print("Entered alphabet is a consonant!")
  pass

if __name__ == "__main__":
  main()
