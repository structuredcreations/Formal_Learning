ENT_SCORE=input("Enter score between 0 and 1")

ENT_SCORE_F=float(ENT_SCORE)
#print(ENT_SCORE_F)

if ENT_SCORE_F < 0.0 :
    print("Number below 0")
elif ENT_SCORE_F > 1.0 :
    print("Number above 1")
else:
    if ENT_SCORE_F>=.9:
        print("A")
    elif ENT_SCORE_F>=.8:
        print('B')
    elif ENT_SCORE_F>=.7:
        print("C")
    elif ENT_SCORE_F>=.6:
        print("D")
    else:
        print("F")

# Note, functions are case sensitive
