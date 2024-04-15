def convert_to_words(number):
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def convert_below_thousand(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + " " + convert_below_thousand(num % 10)
        else:
            return ones[num // 100] + " hundred " + convert_below_thousand(num % 100)

    if number == 0:
        return "zero"

    words = ""
    for i in range(len(thousands)):
        if number % 1000 != 0:
            words = convert_below_thousand(number % 1000) + " " + thousands[i] + " " + words
        number //= 1000

    return words.strip()


# Test the function
number = int(input("Enter a number: "))
print(convert_to_words(number))
