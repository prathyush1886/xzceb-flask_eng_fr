import translator
#for english to french

e2f_test1 = None
e2f_test1_result = None
e2f_test2 = 'Hello'
e2f_test2_result = 'Bonjour'

if translator.english_to_french(e2f_test1) == e2f_test1_result :
    print(f'English to French translation for testcase 1:{e2f_test1} is correct \n')
else:
    print(f'English to French translation for testcase 1:{e2f_test1} is incorrent \n')

if translator.english_to_french(e2f_test2) == e2f_test2_result :
    print(f'English to French translation for testcase 1:{e2f_test2}    is correct \n')
else:
    print(f'English to French translation for testcase 2:{e2f_test2}    is incorrent \n')

#for french to english

f2e_test1 = None
f2e_test1_result = None
f2e_test2 = 'Bonjour'
f2e_test2_result = 'Hello'

if translator.french_to_english(f2e_test1) == f2e_test1_result :
    print(f'French to English translation for testcase 1:{f2e_test1} is correct \n')
else:
    print(f'French to English translation for testcase 1:{f2e_test1} is incorrent \n')

if translator.french_to_english(f2e_test2) == f2e_test2_result :
    print(f'French to English translation for testcase 1:{f2e_test2} is correct \n')
else:
    print(f'French to English translation for testcase 1:{f2e_test2} is incorrent \n')
