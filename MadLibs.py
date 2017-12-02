def wedding_mad_libs():
    noun_1 = input("Enter a name: ")
    noun_2 = input("Enter a location: ")
    noun_3 = input("Enter a noun: ")
    noun_4 = input("Enter a noun: ")
    noun_5 = input("Enter a noun: ")
    noun_6 = input("Enter a noun: ")
    noun_7 = input("Enter a noun: ")
    noun_8 = input("Enter a noun: ")
    var_num = input("Enter a number: ")
    past_verb = input("Enter a verb ending in -ed: ")
    adjective_1 = input("Enter an adjective: ")
    adjective_2 = input("Enter an adjective: ")
    adjective_3 = input("Enter an adjective: ")
    verb_1 = input("Enter a verb: ")
    verb_2 = input("Enter a verb: ")
    verb_3 = input("Enter a verb: ")
    verb_4 = input("Enter a verb: ")
    verb_5 = input("Enter a verb: ")
    sentence_1 = "My name is {} and I've known Nathaniel and Claire for {} years. "
    sentence_2 = "I {} all the way from {} to celebrate this day. "
    sentence_3 = "I am so {} that Nathaniel and Claire are tying the knot! "
    sentence_4 = "They have to be the most {} {} and I wish them {} {} for years to come. My best advice? "
    sentence_5 = "Don't forget to {} before you {} and {} after the {}. "
    sentence_6 = "Nathaniel, you should always {} Claire's {}, and Claire you should always {} Nathaniel's {}. "
    sentence_7 = "I wish you both a lifetime of happiness and {}!"
    sentence_8 = "Love {}"
    print(sentence_1.format(noun_1, var_num) + sentence_2.format(past_verb, noun_2) + sentence_3.format(adjective_1))
    print(sentence_4.format(adjective_2, noun_3, adjective_3, noun_4) + sentence_5.format(verb_1, verb_2, verb_3, noun_5))
    print(sentence_6.format(verb_4, noun_6, verb_5, noun_7) + sentence_7.format(noun_8))
    print(sentence_8.format(noun_1))

wedding_mad_libs()