# Python 3.8 /usr/local/python
# madlibs  game

from random import randint
import copy

story = (
    "One day my {} friend and I decided to go to the {} game in {}. "
    "We really wanted to see the {} play the {}. "
    "So, we {} our {} down to the {} and bought some {}s. "
    "We got into the game and it was a lot of fun. "
    "We ate some {} {} and drank some {} {}. "
    "We had a great time! We plan to go ahead next year"
)

word_dict = {
    "adjective": [],
    "city_name": [],
    "noun": [],
    "action_verb": [],
    "sports_noun": [],
    "place": []
}


def get_word(type, local_dict):
    words = local_dict[type]


def create_story():
    return story.format(
        word_dict['adjective']
    )


def get_input(type, local_dict):
    """Gets user words"""


print("Story Title")
print(story)
