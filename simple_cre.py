# Import itertools for permutations
import itertools

# Import Pattern Search and English modules
from pattern.search import search, taxonomy
from pattern.en import parsetree

# Import (and print out) test strings for pattern matching
import test_strings

# Define Taxonomy CAUSALV1 for verbs: e.g., cause*, influence*, determine*
causal_verb_list1 = ['causes', 'caused', 'influences', 'influenced',
    'determines', 'determined']
for c in causal_verb_list1:
    taxonomy.append(c, type='CAUSALV1')

# Define Taxonomy for CAUSALV2 for simple causal verbs tagged as nouns
# in their simple present form, e.g., cause, influence, determine
causal_verb_list2 = ['cause', 'influence', 'determine']
for c in causal_verb_list2:
    taxonomy.append(c, type='CAUSALV2')

# Cause-effect patterns: statements where cause precedes the effect

# Manually-defined noun phrase definitions
# Consider adding noun phrase chunk from NLTK book, which has optional
# determiner, etc.

# TODO: Consider putting all causal patterns in separate Python file and
# importing as a module

# Simple {noun phrase} cause {noun phrase} pattern
# Example: Smoking causes lung cancer.
cause_effect_pattern1 = "{NP} CAUSALV1 {NP and? NP?}"

# First noun phrase is compound noun phrase: noun phrase AND noun phrase
# Here, noun phrase is defined as optional adjective followed by 1+ nouns
# Example: Inequality and extreme poverty cause underdevelopment.

# NP_chunk1: optional determiner or possessive, followed by
# optional adjective and any number of nouns
# Inspired by NLTK, Chapter 7 section on NP chunking
NP_chunk1 = "DT?|PP? JJ? NN*+"

# cause_NP1 is compound noun phrase, based on NP_chunk1
cause_NP1 = "{" + NP_chunk1 + " and " + NP_chunk1 + "}"

# cause_effect_pattern2 based on cause_NP1
cause_effect_pattern2 = cause_NP1 + " CAUSALV2 {NP and? NP?}"
# cause_effect_pattern5 = cause_NP1 + " lead*|led to {NP and? NP?}"

# First noun phrase is optional adjective followed by plural noun
# Example: Recessions cause inequality.
cause_effect_pattern3 = "{JJ? NNS|NNPS} CAUSALV2 {NP and? NP?}"

# Patterns for {NP} leads|led|lead to {NP}
cause_effect_pattern4 = "{NP} lead|led|contribute|contributed to {NP}"
cause_effect_pattern5 = "{NP} leads|contributes to {NP}"
# In this case, "lead" is POS tagged as noun, thus requiring manually defined NP
cause_effect_pattern6 = cause_NP1 + " lead|contribute to {NP}"

# Patterns for {NP} results|resulted|result in {NP}
cause_effect_pattern7 = "{NP} result|resulted in {NP}"
cause_effect_pattern8 = "{NP} results in {NP}"
cause_effect_pattern9 = cause_NP1 + " result in {NP}"
cause_effect_pattern10 = "{" + NP_chunk1 + "}" + " results in {NP}"

# Add patterns to list cause_effect_patterns
cause_effect_patterns = [cause_effect_pattern1, cause_effect_pattern2,
                        cause_effect_pattern3, cause_effect_pattern4,
                        cause_effect_pattern5, cause_effect_pattern6,
                        cause_effect_pattern7, cause_effect_pattern8,
                        cause_effect_pattern9, cause_effect_pattern10]

# TODO: Write a general purpose function to add patterns and test strings
# to a list. One idea is to have a function add_to_list called like so:
# cause_effect_patterns = add_to_list(cause_effect_patterns, "cause_effect_pattern", 3),
# where it first argument is the empty list, second argument is beginning of
# name of each element added to the list, and the third element is a number,
# specifying I want to add all elements from 1 through index 3. This can be
# applied to cause_effect_patterns, effect_cause_patterns, and test_strings.
# Think about where to place this function, esp. if it is used for test_strings.

print(cause_effect_patterns)

def extract_cause_effect_tuple(possible_matches, pattern_order):
    # Description: Given possible_matches, returns a list of causal tuples
    # Inputs: possible_matches, which contains all matches found in text string
    #         pattern_order, specifying which noun phrase is cause or effect
    # Outputs: list of causal tuples, in form [(cause, effect), ...]

    # Initialize empty list of causal tuples
    causal_tuple_list = []

    # Creates loop to iterate through all possible_matches
    for single_match in possible_matches:
        # Extract cause noun phrase and effect noun phrase
        cause_NP = single_match.group(pattern_order[0]).string
        effect_NP = single_match.group(pattern_order[1]).string

        # Add cause noun phrase and effect noun phrase to causal_tuple
        causal_tuple = (cause_NP, effect_NP)

        # Add causal_tuple to causal_tuple_list
        causal_tuple_list.append(causal_tuple)

    return (causal_tuple_list)

def find_causal_matches(unicode_string, causal_pattern, pattern_order):
    # Description: Searches text string and returns all cause-effect
    #              relationships based on specified pattern.
    # Inputs: unicode_string, raw text in Unicode format for Python 3
    #         causal_pattern, regex defining specific causal statement pattern
    #         pattern_order, specifying which noun phrase is cause or effect
    # Outputs: List of causal tuples [(cause, effect), ...] or empty list []

    # Initialize causal_tuple_list as empty list
    causal_tuple_list = []

    # Convert string to Pattern parsed text (with POS tags)
    t = parsetree(unicode_string)

    # possible_matches is a list of all Pattern matches, given text and pattern
    possible_matches = search(causal_pattern, t, lemmata=True)

    # Add causal matches as tuples (cause, effect) to causal_tuple_list
    # Note, if possible_matches=[], there are no matches
    if possible_matches != []:
        # Extract cause-effect tuples and add to causal_tuple_list
        causal_tuple_list = extract_cause_effect_tuple(possible_matches,
                                pattern_order)

    return(causal_tuple_list)

def is_tuple_subset(causal_tuple1, causal_tuple2):
    # Description: Determines if causal_tuple1 is subset of causal_tuple2
    # Input: causal_tuple1, causal_tuple2 of form (cause_NP, effect_NP)
    # Output: True/False

    # Check if first element of tuple is subset
    first_element_subset = causal_tuple1[0] in causal_tuple2[0]

    # Check if second element of tuple is subset
    second_element_subset = causal_tuple1[1] in causal_tuple2[1]

    # Indicator for whether both elements are subset
    both_elements_subset = first_element_subset and second_element_subset

    # Check if first element of tuple1 is shorter than tuple2
    first_element_shorter = len(causal_tuple1[0]) < len(causal_tuple2[0])

    # Check if second element of tuple1 is shorter than tuple2
    second_element_shorter = len(causal_tuple1[1]) < len(causal_tuple2[1])

    # Indicator that tuple1 is shorter than tuple2
    tuple1_shorter = first_element_subset or second_element_shorter

    # If elements of tuple1 are subsets of tuple2 and
    # tuple1 shorter than tuple2, then tuple1 is subset of tuple2
    if both_elements_subset and tuple1_shorter:
        return True
    else:
        return False

def greedy_match(causal_tuple_list):
    # Description: Given a list of causal tuples (causeNP, effectNP),
    #              returns a list that removes all subsets of tuples.
    #              e.g., if causal_tuple_list = [("smoking", "cancer"),
    #              ("smoking", "lung cancer")], then it returns
    #              greedy_causal_list = [("smoking", "lung cancer")].
    # Inputs: causal_tuple_list, list of tuples of form (causeNP, effectNP)
    # Outputs: greedy_causal_list, list that removes all subsets of
    #          causal tuples. This list only includes the greedy matches.

    # Initialize empty list of causal_tuple_permutation
    causal_tuple_permutation = []

    # Create list of permutations for each causal_tuple
    # If causal_tuple_list = [(causeNP1, effectNP1), (causeNP2, effectNP2)]
    # Returns causal_tuple_permutation = [[(causeNP1, effectNP1),
    #                                     (causeNP2, effectNP2)],
    #                                     [(causeNP2, effectNP2),
    #                                      (causeNP1, effectNP1)]]
    for a, b in itertools.permutations(causal_tuple_list, 2):
        causal_tuple_permutation.append([a,b])

    # Initialize greedy_causal_list
    greedy_causal_list = []

    # For each combination of causal tuples in causal_tuple_list,
    # only append unique causal tuples, not subsets of other causal tuples
    for combo in causal_tuple_permutation:

        # Check that combo[0] is not a subset of combo[1] and not already
        # in greedy_causal_list

        tuple1_not_subset_tuple2 = not is_tuple_subset(combo[0], combo[1])
        tuple1_not_in_greedy_list = combo[0] not in greedy_causal_list

        if tuple1_not_subset_tuple2 and tuple1_not_in_greedy_list:

            # Initialize num_subsets to count number of times combo[0]
            # is a subset of a tuple in greedy_causal_list
            num_subsets = 0

            # Increment num_subsets everytime greedy_combo is subset of tuple
            # in greedy_causal_list
            for greedy_combo in greedy_causal_list:
                if is_tuple_subset(combo[0], greedy_combo):
                    num_subsets += 1
                elif is_tuple_subset(greedy_combo, combo[0]):
                    # if greedy_combo - what is currently in greedy_causal_list
                    # - is a subset of combo[0], remove greedy_combo from
                    # greedy_causal_list
                    greedy_causal_list.remove(greedy_combo)

            if num_subsets == 0:
                greedy_causal_list.append(combo[0])

    return (greedy_causal_list)

# Defines pattern order
cause_effect_order = (1,2)
effect_cause_order = (2,1)

# print("I made it to the end of the program.")

def extract_patterns_from_text(pattern_list, unicode_string, cause_effect_order):
    # Description: Given a list of patterns, returns a list of tuples
    #              of form [(causeNP, effectNP)], where each tuple is
    #              not a subset of another tuple in the list.
    # Inputs: pattern_list, list of defined patterns to match
    #         unicode_string, text string from which we will extract causal tuples if they exist
    #         cause_effect_order, defines which noun phrase is cause or effect
    # Output: greedy_causal_list, list of distinct, greedy causal tuples

    # Initialize empty list causal_tuple_list
    causal_tuple_list = []

    # Iterate through list of cause_effect patterns
    # If you find a match, add causal_tuple (cause_NP, effect_NP) to causal_tuple_list
    for pattern in pattern_list:
        causal_tuple_pattern_list = find_causal_matches(unicode_string, pattern, cause_effect_order)
        if causal_tuple_pattern_list != []:
            causal_tuple_list.append(causal_tuple_pattern_list[0])

    # Extract only unique elements of causal_tuple_list
    causal_tuple_list = set(causal_tuple_list)

    if len(causal_tuple_list) > 1:
        # print ("more than one match:", causal_tuple_list)

        # return only the greedy matches from causal_tuple_list
        causal_tuple_list = greedy_match(causal_tuple_list)

    print("RESULT:", causal_tuple_list, '\n')

    return causal_tuple_list

# Initialize index for easy referencing
index = 1

# Iterate through all test strings
for sample_string in test_strings.test_strings_list:
    # print test string
    print("test_string:", index, '\n', sample_string)
    index += 1

    extract_patterns_from_text(cause_effect_patterns, sample_string, cause_effect_order)

    # Add each element of causal_tuple_list to database...

# causal_tuple_list = [('excessive cigarette smoking', 'lung cancer'), ('Economic development and robust institutions', 'prosperity'), ('robust institutions', 'prosperity')]

# print(greedy_match(causal_tuple_list))
