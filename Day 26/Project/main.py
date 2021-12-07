import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    user_input = input('Enter a word: ').upper()
    try:
        output_list = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate()
    else:
        print(output_list)
    
generate() 