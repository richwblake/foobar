def solution(xs):
    if not xs:
        return 0
    lowest_negative = max(xs)
    product = 1
    odd_amount_of_negatives = False
    for number in xs:
        if number != 0:
            if number < 0:
                odd_amount_of_negatives = not odd_amount_of_negatives
                lowest_negative = min(lowest_negative, abs(number))
            product *= abs(number)

    if odd_amount_of_negatives:
        return str(product / lowest_negative)
    else:
        return str(product)

def print_test(got, expected):
    print("----------------")
    print("Expected " + expected)
    print("Got " + got)
    if got == expected:
        print("Correct")
    else:
        print("Incorrect")

str1 = "Hello there"
str2 = "Hello there"
str3 = "Hello World!"

l1 = [1, 2, 3, 4, 5]

tl1 = [2, 0, 2, 2, 0]
tl2 = [-2, -3, 4, -5]

s1 = solution(tl1)
s2 = solution(tl2)

print_test(s1, "8")
print_test(s2, "60")
