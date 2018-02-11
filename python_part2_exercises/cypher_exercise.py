encrypted = "lbh zhfg hayrnea jung lbh unir yrnearq"
alphabet = "abcdefghijklmnopqrstuvwxyz"
off_key = 13
result = " "

for i in encrypted:
    if i not in alphabet:
        decode = i
    else:
        code_idx = alphabet.find(i) 
        shift_idx = code_idx - 13
        if shift_idx < 0:
            shift_idx = shift_idx + 26
        decode = alphabet[shift_idx]
    result += decode

print(result)