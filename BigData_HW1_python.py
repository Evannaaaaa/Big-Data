# Yuqi Chen Assignment4A

def main():
    print("%.2f" % NetPresentValue([0, 100], .05)) # 2-year 0-coupon bond
    print("%.2f" % NetPresentValue([4, 4, 4, 104], .05))  # 4-year bond paying 4% a year, principal+interest at maturity
    print("%.2f" % NetPresentValue([], .05))  # edge case – no cashflows, should return 0

def NetPresentValue(F, r):
    P = 0
    for i in range(len(F)):
        P += F[i] / (1+r) ** (i+1)

    return P

main()

