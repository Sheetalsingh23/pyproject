import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
ankitrai326@gmail.com
my.ownsite@our-earth.org
ankitrai326.com
'''
string = '''Paste your text 'he45re' ':)'
'%^&%^*'
"dfer455"
'hello'
'''

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# pattern = re.compile(r"['][a-zA-Z0-9!@#$%^&*()-_+=]+[']")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile(
    r'\b[a-zA-Z0-9.-]*@*[a-zA-Z0-9.-]*[a-zA-Z0-9]*\b')
matches = pattern.finditer(emails)
ans = []
for match in matches:
    if(re.fullmatch(regex, match.group(0))):
        ans.append("Valid Email")
    else:
        ans.append("Invalid Email")
# matches = pattern.finditer(emails)

for match in matches:
    print(match.group(0))
    # print(match)
# print(['hello', "from", ''the'', "'other'"])
