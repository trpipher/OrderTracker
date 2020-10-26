def cleanString(s):
    if not s[len(s)-1] == " ":
        s+=" "
    if s[0] == " ":
        s = s[1:]
    return s