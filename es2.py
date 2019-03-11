s = input("Inserisci la stringa:\t")
if len(s) < 4:
    out = str()
else:
    out = s[:2] + s[-2:]
print(out)
