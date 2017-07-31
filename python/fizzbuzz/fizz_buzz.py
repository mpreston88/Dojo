
def fizz_buzz(number):
    if number:
        numbers = []
        for n in range(0, number):
            numbers.append(n+1)
        return numbers
    return []