# Test strings

# Test strings: NP_cause (and NP_cause) [verb] NP_effect (and NP_effect)

# NP (singular) causes NP
test_text1 = "It is commonly known that economic development causes prosperity."
test_text11 = "It is commonly known that economic development leads to prosperity."

# NP caused NP
test_text2 = "Economic development caused prosperity."
test_text12 = "Economic development led to prosperity."

# NP and NP cause NP
test_text3 = "Economic development and robust institutions cause prosperity."
test_text13 = "Economic development and robust institutions lead to prosperity."

 # NP and NP caused NP
test_text4 = "Economic development and robust institutions caused prosperity."
test_text14 = "Economic development and robust institutions led to prosperity."

# NP causes NP and NP
test_text5 = "Economic development causes prosperity and social mobility."
test_text15 = "Economic development leads to prosperity and social mobility."

# NP caused NP and NP
test_text6 = "Economic development caused prosperity and social mobility."
test_text16 = "Economic development led to prosperity and social mobility."

# NP and NP caused NP
test_text7 = "Economic development and good governance caused prosperity and mobility."
test_text17 = "Economic development and good governance led to prosperity and mobility."

# NP and NP cause NP and NP
test_text8 = "Economic development and good governance cause prosperity and mobility."
test_text18 = "Economic development and good governance lead to prosperity and mobility."

# NP (plural) cause NP
test_text9 = "Billionaires cause economic development."
test_text19 = "Recessions lead to fiscal reforms."

# Simple patterns but multiple sentences...
test_text10 = "Economic development and robust institutions cause prosperity. We also know that excessive cigarette smoking causes lung cancer."
test_text20 = "Economic development and robust institutions lead to prosperity. We also know that excessive cigarette smoking leads to lung cancer."

test_strings = []

# TODO: Find a way to automatically generate test string names and
# create a loop to include into the test_strings list.
test_strings_list = [test_text1, test_text2, test_text3, test_text4,
                test_text5, test_text6, test_text7, test_text8, test_text9,
                test_text10, test_text11, test_text12, test_text13, test_text14,
                test_text15, test_text16, test_text17, test_text18, test_text19,
                test_text20]

# Print out list of test strings to confirm all strings are as expected
for test_string_index in range(len(test_strings_list)):
    print(str(test_string_index+1)+":", test_strings_list[test_string_index], "\n")
