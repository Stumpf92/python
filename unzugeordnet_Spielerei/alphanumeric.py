import re

def alphanumeric(password):
    list=[]
    list.append(password)
    if re.findall("[a-zA-Z0-9]+$", password) == list:
        print("True")
        return True
    else:
        print("False")
        return False



alphanumeric("PassW0rd")