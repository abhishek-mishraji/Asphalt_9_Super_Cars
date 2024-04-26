def remove(s, re):
    newstr = s.replace(re, "")
    return (newstr.strip())  # STRIP is use to remove extra space


s = "                abhi is chutiyaaaaaaaaaaaaaaaaaa boy                  "
print(remove(s, "abhi"))
