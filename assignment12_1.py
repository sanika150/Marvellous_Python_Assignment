def vowels(ch):
    
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("Vowel")
    else:
        print("Consonant")

def main():
    Res =0
    print("Enter the character :")
    ch= (input())
    Res=vowels(ch)

if __name__ == "__main__":
    main()
    