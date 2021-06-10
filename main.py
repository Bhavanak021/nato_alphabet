import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(df)

# Create a dictionary in this format:
phonetic_dic = {value.letter: value.code for (key, value) in data.iterrows()}
# Create a list of the phonetic code words from a word that the user inputs.
is_ok = True
while is_ok:
    try:
        user_input = input("Enter a word: ").upper()
        phonetic_code = {phonetic_dic[letter] for letter in user_input}
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        is_ok = False
        print(phonetic_code)
