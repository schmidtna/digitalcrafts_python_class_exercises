uppercase = str.upper("lowercase")
print(uppercase)

capper = str.capitalize("capitalized")
print(capper)

#  strings are immutable, this  slices the string [start:stop:step] 
#  and returns it, basically returns the whole thing back to front
# creating a new string.
"reverse me!"[: :-1]

mixup = ("Hello world in leetspeak!").upper()
mixup = mixup.replace("A", "4")
mixup = mixup.replace("E", "3")
mixup = mixup.replace("G", "6")
mixup = mixup.replace("I", "1")
mixup = mixup.replace("O", "0")
mixup = mixup.replace("S", "5")
mixup = mixup.replace("T", "7")
print(mixup)


long_vowels = ("A good cheese doesn't need a spoon.")

long_vowels = long_vowels.replace("aa", "aaaaa")
long_vowels = long_vowels.replace("ee", "eeeee")
long_vowels = long_vowels.replace("ii", "iiiii")
long_vowels = long_vowels.replace("oo", "ooooo")
long_vowels = long_vowels.replace("uu", "uuuuu")

print(long_vowels)