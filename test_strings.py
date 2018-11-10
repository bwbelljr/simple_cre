# Test strings

# Test strings: NP_cause (and NP_cause) [verb] NP_effect (and NP_effect)

# NP (singular) causes NP
test_text1 = "It is commonly known that economic development causes prosperity."
test_text11 = "It is commonly known that economic development leads to prosperity."
test_text21 = "It is commonly known that economic development contributes to prosperity."
test_text31 = "It is commonly known that economic development results in prosperity."

# NP caused NP
test_text2 = "Economic development caused prosperity."
test_text12 = "Economic development led to prosperity."
test_text22 = "Economic development contributed to prosperity."
test_text32 = "Economic development resulted in prosperity."

# NP and NP cause NP
test_text3 = "Economic development and robust institutions cause prosperity."
test_text13 = "Economic development and robust institutions lead to prosperity."
test_text23 = "Economic development and robust institutions contribute to prosperity."
test_text33 = "Economic development and robust institutions result in prosperity."

 # NP and NP caused NP
test_text4 = "Economic development and robust institutions caused prosperity."
test_text14 = "Economic development and robust institutions led to prosperity."
test_text24 = "Economic development and robust institutions contributed to prosperity."
test_text34 = "Economic development and robust institutions resulted in prosperity."

# NP causes NP and NP
test_text5 = "Economic development causes prosperity and social mobility."
test_text15 = "Economic development leads to prosperity and social mobility."
test_text25 = "Economic development contributes to prosperity and social mobility."
test_text35 = "Economic development results in prosperity and social mobility."

# NP caused NP and NP
test_text6 = "Economic development caused prosperity and social mobility."
test_text16 = "Economic development led to prosperity and social mobility."
test_text26 = "Economic development contributed to prosperity and social mobility."
test_text36 = "Economic development resulted in prosperity and social mobility."

# NP and NP caused NP
test_text7 = "Economic development and good governance caused prosperity and mobility."
test_text17 = "Economic development and good governance led to prosperity and mobility."
test_text27 = "Economic development and good governance contributed to prosperity and mobility."
test_text37 = "Economic development and good governance resulted in prosperity and mobility."

# NP and NP cause NP and NP
test_text8 = "Economic development and good governance cause prosperity and mobility."
test_text18 = "Economic development and good governance lead to prosperity and mobility."
test_text28 = "Economic development and good governance contribute to prosperity and mobility."
test_text38 = "Economic development and good governance result in prosperity and mobility."

# NP (plural) cause NP
test_text9 = "Billionaires cause economic development."
test_text19 = "Recessions lead to fiscal reforms."
test_text29 = "Recessions contribute to fiscal reforms."
test_text39 = "Recessions result in fiscal reforms."

# Simple patterns but multiple sentences...
test_text10 = "Economic development and robust institutions cause prosperity. We also know that excessive cigarette smoking causes lung cancer."
test_text20 = "Economic development and robust institutions lead to prosperity. We also know that excessive cigarette smoking leads to lung cancer."
test_text30 = "Economic development and robust institutions contribute to prosperity. We also know that excessive cigarette smoking contributes to lung cancer."
test_text40 = "Economic development and robust institutions result in prosperity. We also know that excessive cigarette smoking results in lung cancer."

test_strings = []

# TODO: Find a way to automatically generate test string names and
# create a loop to include into the test_strings list.
test_strings_list = [test_text1, test_text2, test_text3, test_text4,
                test_text5, test_text6, test_text7, test_text8, test_text9,
                test_text10, test_text11, test_text12, test_text13, test_text14,
                test_text15, test_text16, test_text17, test_text18, test_text19,
                test_text20, test_text21, test_text22, test_text23, test_text24,
                test_text25, test_text26, test_text27, test_text28, test_text29,
                test_text30, test_text31, test_text32, test_text33, test_text34,
                test_text35, test_text36, test_text37, test_text38, test_text39,
                test_text40]

# Print out list of test strings to confirm all strings are as expected
for test_string_index in range(len(test_strings_list)):
    print(str(test_string_index+1)+":", test_strings_list[test_string_index], "\n")
