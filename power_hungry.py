def solution(xs):
    if not xs:
        return 0
    product = 1
    number_of_zeros = 0
    number_of_negatives = 0
    largest_negative = -999999999999
    for number in xs:
        if number != 0:
            if number < 0:
                number_of_negatives += 1
                largest_negative = max(largest_negative, number)
            product *= abs(number)
        else:
            number_of_zeros += 1

    if number_of_zeros == len(xs):
        return str(0)
    
    if number_of_negatives % 2 != 0:
        if number_of_zeros + 1 == len(xs):
            return str(0)
        else:
            return str(product / abs(largest_negative))
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
tl3 = [-2, -4, 0, 4]
tl4 = [0, 0, -1]

s1 = solution(tl1)
s2 = solution(tl2)
s3 = solution(tl3)
s4 = solution(tl4)

print_test(s1, "8")
print_test(s2, "60")
print_test(s3, "32")
print_test(s4, "0")









