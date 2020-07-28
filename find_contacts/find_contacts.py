import pyperclip, re
# finds phone numbers and email addresses in the clipboard

phone_regex = re.compile(r'''(
    (\d{3}|\(d{3}\))?       # area code
    (\s|-|\.)?              # seporator
    (\d{3})                 # first 3 digits
    (\s|-|\.)               # seporator
    (\d{4})                 # last 4 digits
    (\s*(ext.)\s*(\d{2,5}))?# extension
)''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-z]{2,4})       # .something
)''', re.VERBOSE)


# find matches in clipboard text
def find_matches():
    """searches the clipboard for regex matches, then copies matches to clipboard"""
    text = str(pyperclip.paste())

    matches =[]

    for groups in phone_regex.findall(text):
        phoneNum = '-'.join([groups[1],groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

    for groups in email_regex.findall(text):
        matches.append(groups[0])
    return matches

def copy_matches(matches):
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard: ')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found')

def find_contacts(text):
    matches = find_matches()
    copy_matches(matches)

if __name__ == "__main__":
    text = str(pyperclip.paste())
    find_contacts(text)

# copy to test

# 123-456-7890
# test@test.com



