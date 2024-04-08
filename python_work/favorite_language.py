favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if "erin" not in favorite_languages.keys():
    print('Erin, please take our poll!')

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for takeing the poll")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

students_accept_survey = ['jen','sarah','cecilia','edward',
                          'aaron','oliver','phil']
for student in students_accept_survey:
    if student in favorite_languages.keys():
        print(f'Dear {student.title()}, thank you')
    else:
        print(f"Dear {student.title()}, please do the survey!")

#添加列表在dic里面
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['go'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell']
    }

for name, languages in favorite_languages.items():
    if len(languages)==1:
        print(f"\n{name.title()}'s favorite languge is:{languge.title()}")
    else:
        print(f"\n{name.title()}'s favorite language are:")
        for languge in languages:
            print(f"\t{languge.title()}")