# Test strings

# Test strings: NP_cause (and NP_cause) [verb] NP_effect (and NP_effect)

# NP (singular) causes NP
test_text1 = "It is commonly known that economic development causes prosperity."

# NP caused NP
test_text2 = "Economic development caused prosperity."

# NP and NP cause NP
test_text3 = "Economic development and robust institutions cause prosperity."

 # NP and NP caused NP
test_text4 = "Economic development and robust institutions caused prosperity."

# NP causes NP and NP
test_text5 = "Economic development causes prosperity and social mobility."

# NP caused NP and NP
test_text6 = "Economic development caused prosperity and social mobility."

# NP and NP caused NP
test_text7 = "Economic development and good governance caused prosperity and mobility."

# NP and NP cause NP and NP
test_text8 = "Economic development and good governance cause prosperity and mobility."

# NP (plural) cause NP
test_text9 = "Billionaires cause economic development."

# Simple patterns but multiple sentences...
test_text10 = "Economic development and robust institutions cause prosperity. We also know that excessive cigarette smoking causes lung cancer."

test_strings = []

# TODO: Find a way to automatically generate test string names and
# create a loop to include into the test_strings list.
test_strings_list = [test_text1, test_text2, test_text3, test_text4,
                test_text5, test_text6, test_text7, test_text8, test_text9,
                test_text10]

# Print out list of test strings to confirm all strings are as expected
for test_string_index in range(len(test_strings_list)):
    print(str(test_string_index+1)+":", test_strings_list[test_string_index], "\n")
