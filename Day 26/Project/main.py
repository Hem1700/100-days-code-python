import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input('Enter a word: ').upper()
output_list = [alphabet_dict[letter] for letter in user_input]
print(output_list)
