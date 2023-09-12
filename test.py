A = 6
B = 6
C = 5
if A == B and B == C:
    print("A,B,C")
elif A > B and A > C:
    print("A")
elif B > A and B > C:
    print("B")
elif C > A and C > B:
    print("C")
elif A == B and A > C:
    print("A,B")
elif A == C and A > B:
    print("A,C")
elif B == C and B > A:
    print("B,C")