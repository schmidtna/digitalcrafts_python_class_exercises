# Dictionary ex 1

# phonebook_dict = {
#     "Alice" : "703-493-1834",
#     "Bob" : "857-384-1234",
#     "Elizabeth" : "484-584-2923"
# }
# phonebook_dict["Kareem"] = "938-489-1234"
# del phonebook_dict["Alice"]
# phonebook_dict["Bob"] = "968-345-2345"

# for key, value in phonebook_dict.items():
#     print(key, ":", value)


# Dictionary ex 2

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(ramit["email"])
# print(ramit["interests"][0])
# print(ramit["friends"][0]["email"])
# print(ramit["friends"][1]["interests"][1])

# Dictionary ex 3

def letter_count(x):

    input_letters = {}

    for i in x:
        counting = input_letters.get(i, 0)
        input_letters[i] = counting + 1
    
    print(input_letters)

if __name__ == "__main__":
    letter_count()

# Dictionary ex 4

def word_count(input_para):
    tally_list = {}
    word_sets = input_para.split()
    
    for words in word_sets:
        if words not in tally_list:
            tally_list[words] = 1
        else: 
            tally_list[words] += 1

    print(tally_list)

    

if __name__ == "__main__":
    word_count()


