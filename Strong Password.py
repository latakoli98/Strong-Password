print("Enter your password")
pswd = input(" ")
if (pswd>="a" and pswd<="z") or (pswd>="A" and pswd<="Z") or (pswd>=0) or pswd=="#" or pswd=="@" or pswd=="&" or   pswd=="?" or pswd=="!":
    if len(pswd)>8:
        print("Strong password")
    else:
        print("Weak password")