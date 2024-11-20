'''
Regexp:
        regexp are sequences of characters that define search patterns.
        They're often used for findinv ,replacing , or validating text patterns.
        in python,regexp are supported by re module.
'''
import re
a="cha@gmail.com"
pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

match=re.search(pattern,a)



if match:
    print("found an email:",match.group())
else:
    print("no emil found")
