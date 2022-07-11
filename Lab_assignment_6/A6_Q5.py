def hyphen(sent):
    words=sent.split("-")
    word=sorted(words)
    new="-".join(word)
    print(new)
n=input()
hyphen(n)
