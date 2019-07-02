# Import itertools for permutations
import itertools

# Import Pattern Search and English modules
from pattern.search import search, taxonomy
from pattern.en import parsetree

# Defining simple causal patterns

# Taxonomy for cause-effect pattern
causal_verb_list1 = ['causes', 'caused', 'would cause', 'will cause',
                     'is causing', 'has been causing', 'was causing',
                     'had been causing', 'will be causing',
                     'will have been causing', 'would be causing',
                     'would have been causing', 'are causing',
                     'have been causing', 'were causing']

for c1 in causal_verb_list1:
    taxonomy.append(c1, type='CAUSALV1')

cause_effect_pattern = "{NP} CAUSALV1 {NP}"

# Taxonomy for effect-cause pattern
causal_verb_list2 = ["is caused", "was caused", "are caused",
                     "were caused", "has been caused", "have been caused",
                     "had been caused", "will have been caused",
                     "would have been caused", "is being caused",
                     "was being caused", "were being caused",
                     "would be caused", "will be caused"]

for c2 in causal_verb_list2:
    taxonomy.append(c2, type='CAUSALV2')

effect_cause_pattern = "{NP} CAUSALV2 by {NP}"

pattern_list = [cause_effect_pattern, effect_cause_pattern]

# Defines pattern order
cause_effect_order = (1,2)
effect_cause_order = (2,1)
pattern_order_list = [cause_effect_order, effect_cause_order]

def extract_cause_effect_tuple(possible_matches, pattern_order):
    # Description: Given possible_matches, returns a list of causal tuples
    # Inputs: possible_matches, a Pattern object containing all pattern matches
    #         found in text string
    #         pattern_order, specifying which noun phrase is cause or effect
    # Outputs: list of causal tuples for pattern, in form [(cause, effect), ...]

    # Initialize empty list of causal tuples
    causal_tuple_list = []

    # Creates loop to iterate through all possible_matches
    for single_match in possible_matches:
        # Extract cause noun phrase and effect noun phrase
        cause_NP = single_match.group(pattern_order[0]).string.replace(" ,",
                                      ",")
        effect_NP = single_match.group(pattern_order[1]).string.replace(" ,",
                                      ",")

        # Add cause noun phrase and effect noun phrase to causal_tuple
        causal_tuple = (cause_NP, effect_NP)

        # Add causal_tuple to causal_tuple_list
        causal_tuple_list.append(causal_tuple)

    return (causal_tuple_list)

def extract_doc_causal_tuples(unicode_doc):
    # Description: unicode text string, returns a list of causal tuples
    # Inputs: unicode_doc, a unicode text string
    # Outputs: list of causal tuples, in form [(cause, effect), ...]

    pattern_doc = parsetree(unicode_doc)

    # Initialize empty list of causal tuples in the document
    document_causal_tuples = []

    # Extract and add causal tuples to document causal tuples
    for i in range(len(pattern_list)):
        possible_matches = search(pattern_list[i], pattern_doc, lemmata=True)
        document_causal_tuples += extract_cause_effect_tuple(possible_matches,
                                                        pattern_order_list[i])

    return(document_causal_tuples)
