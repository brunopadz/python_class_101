score = input("Enter Score: ")

xscore = float(score)

if xscore >= 0.9:
    print("A")
elif xscore >= 0.8:
    print("B")
elif xscore >= 0.7:
    print("C")
elif xscore >= 0.6:
    print("D")
elif xscore < 0.6:
    print("F")
else:
    print("Error!")
