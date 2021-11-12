# sentence = "Roses are {} violets are {}, I love {}"
# color = input("Enter a color: ")
# print()
# noun = input("Enter a noun: ")
# print()
# celebrity = input("Enter a name of a celebrity: ")
# print()
#
# print(sentence.format(noun, color, celebrity));

word_dict = {
    "Name of person in room": [],
    "Noun": [],
    "Superlative": [],
    "Noun ": [],
    "Body part": [],
    "Verb (Ending in -ing)": [],
    "Noun  ": [],
    "Verb": [],
    "Event": [],
    "Day of the week": [],
    "Verb ": [],
    "Verb  ": [],
    "Place": [],
    "Time span": [],
    "Verb   ": [],
    "Adverb": [],
    "Name of person in room ": []
}


def get_user_input():
    # Getting user input
    for types, word in word_dict.items():
        word_dict[types] = str(input("Please enter a/an {}: ".format(types)))


love_letter_three = (
    "Dear {Name of person in room} it has come to my {Noun} that you are the {Superlative} "
    "girl in the {Noun } my {Body part} starts {Verb (Ending in -ing)} a  {Noun  } "
    "everytime you speak. I would like to {Verb} if you went to the {Event} "
    "with me next week {Day of the week} if you {Verb } please {Verb  } me at the {Place} "
    "in {Time span} I {Verb   } you and everything about you, {Adverb}, {Name of person in room }"
)


get_user_input()
for key, value in word_dict.items():
    print(word_dict[key])


print(love_letter_three.format(**word_dict))


#
# print(love_letter_three.format(
#     word_dict["Name of person in room"],
#     word_dict["Noun"],
#     word_dict["Superlative"],
#     word_dict["Noun "],
#     word_dict["Body part"],
#     word_dict["Verb (Ending in -ing)"],
#     word_dict["Noun  "],
#     word_dict["Verb"],
#     word_dict["Event"],
#     word_dict["Day of the week"],
#     word_dict["Verb "],
#     word_dict["Verb  "],
#     word_dict["Place"],
#     word_dict["Time span"],
#     word_dict["Verb   "],
#     word_dict["Adverb"],
#     word_dict["Name of person in room "]
# ))
