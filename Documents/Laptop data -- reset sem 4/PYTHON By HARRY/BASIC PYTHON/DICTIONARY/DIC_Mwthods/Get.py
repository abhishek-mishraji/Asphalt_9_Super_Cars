my_key = {
    "abhi": "car",
    "vimal": "chess",
    1: 3
}

print(my_key.get("abhi"))
print(my_key["abhi"])
# *************************
print(my_key.get("abhi_5"))  # if not present  rreturn None
# print(my_key["abhi_5"])  # it  will thow error
