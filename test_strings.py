# Test strings

class TestSent:
    'Common base class for all test sentences'

    def __init__(self, test_sent, cause_NP, verb_phrase, effect_NP):
        self.test_sent = test_sent
        self.cause_NP = cause_NP
        self.verb_phrase = verb_phrase
        self.effect_NP = effect_NP

def generate_NP_list(string1, string2, string3, is_effect):
    # Description: Given 3 strings, returns list of 3 noun
    #              noun phrases of the form [NP],
    #              [NP and NP], and [NP, NP, and NP]
    # Inputs:      string1, string2, string3 are inputs
    #              representing noun phrases to concatenate
    #              for test sentences
    #              is_effect = True implies noun phrases are
    #              "effect" noun phrases
    # Outputs:     list [np1, np2, np3] which can be used
    #              to generate test sentences

    # First noun phrase = string1
    # Cause noun phrases are capitalized
    if not is_effect:
        np1 = string1.capitalize()
    else:
        np1 = string1.lower() + "."

    # Second noun phrase = string1 and string2
    # string2 is lowercase
    if not is_effect:
        np2 = np1 + " and " + string2.lower()
    else:
        np2 = string1.lower() + " and " + string2.lower() + "."

    # Third noun phrase = string1, string2, and string3
    # string2 and string3 are lowercase
    # Effect noun phrases end in period
    if not is_effect:
        np3 = np1 + ", " + string2.lower() + ", and " + string3.lower()
    else:
        np3 = string1.lower() + ", " + string2.lower() + ", and " + string3.lower() + "."

    # Return noun phrases in a list
    return ([np1, np2, np3])

cause_NP_list = generate_NP_list("economic DEVELOPMENT", "Social development", "good governance", is_effect=False)
effect_NP_list = generate_NP_list("prosperity", "social mobility", "improved living standards", is_effect=True)

def generate_cause_NP_dict(NP_list, plural_NP):
    # Description: Generate dictionary from noun phrase list,
    #              specifying whether it is singular/plural
    # Inputs:      NP_list, list of noun phrases for test sentences
    #              plural_NP, noun phrase in plural form
    # Output:      Dictionary with each noun phrase as key and
    #              "singular"/"plural" as value

    NP_dict = {}

    # For each noun phrase, add to
    # dictionary with key="noun phrase"
    # and value="singular"/"plural"
    for NP in NP_list:
        # " and " implies multiple NP's
        if (" and " in NP):
            NP_dict[NP]="plural"
        else:
            NP_dict[NP]="singular"

    # Add additional plural noun phrase
    # Capitalize noun phrase as it starts the sentence
    NP_dict[plural_NP.capitalize()]="plural"

    return(NP_dict)

cause_NP_dict = generate_cause_NP_dict(cause_NP_list, "effective states")

# for verb phrases, possibly just define a dictionary with singular/plural
# over time, you can simply add other verbs to this list...

cause_vp_dict = {"cause": "plural",
                 "causes": "singular",
                 "caused":"singular/plural",
                 "has caused":"singular",
                 "have caused":"plural",
                 "would cause":"singular/plural",
                 "had caused":"singular/plural",
                 "causes":"singular",
                 "will cause":"singular/plural",
                 "will have caused":"singular/plural",
                 "would have caused":"singular/plural",
                 "is causing":"singular",
                 "are causing":"plural",
                 "has been causing":"singular",
                 "have been causing": "plural",
                 "was causing":"singular",
                 "were causing":"plural",
                 "had been causing":"singular/plural",
                 "will be causing":"singular/plural",
                 "will have been causing":"singular/plural",
                 "would be causing":"singular/plural",
                 "would have been causing":"singular/plural"}

# Generate Test Sentences

def generate_test_sents(cause_NP_dict, cause_vp_dict, effect_NP_list):
    # Description: generate test sentences given cause and effect
    #              noun phrases as well as a verb phrase.
    # Inputs:      cause_NP_dict: dictionary of cause noun phrases & tenses
    #              cause_vp_dict: dictionary of verb phrases & tenses
    #              effect_NP_list: list of effect noun phrases
    # Output:      test_sents_list: list of generated sentences

    # Initialize counter: my_sum
    my_sum = 1

    test_sents_list = []

    # For each cause noun phrase, concatenate
    # verb phrase of compatible tense and
    # each possible verb phrase.
    for noun_phrase in cause_NP_dict:
        for verb_phrase in cause_vp_dict:
            # Ensure that tense of noun and verb phrases agree
            if cause_NP_dict[noun_phrase] in cause_vp_dict[verb_phrase]:
                # Concatenate verb phrases
                for effect_NP in effect_NP_list:
                    # print(my_sum, noun_phrase, verb_phrase, effect_NP)
                    test_sent_string = noun_phrase + " " + verb_phrase + " " + effect_NP
                    test_sent = TestSent(test_sent_string, noun_phrase, verb_phrase, effect_NP)

                    test_sents_list.append(test_sent)
                    my_sum += 1

    return (test_sents_list)

test_strings_list = generate_test_sents(cause_NP_dict, cause_vp_dict, effect_NP_list)

# Print out list of test strings to confirm all strings are as expected
for test_string_index in range(len(test_strings_list)):
    print(str(test_string_index+1)+":", test_strings_list[test_string_index].test_sent, "\n")
