import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

dic = {row.letter : row.code for (index, row) in df.iterrows()}

def main():
    while True:
        word = input("Type your word: ").upper()
        if not word:
            break
        codeList = [dic[letter] for letter in word]
        print(codeList)

if __name__ == "__main__":
    main()
