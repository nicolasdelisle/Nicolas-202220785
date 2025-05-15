#function to get number
def get_number_input(number) -> float | int:
    while True:
        try:
            num: float = float(input(number))
            if num.is_integer():
                return int(num)
            else:
                return num
        except ValueError:
            print("Enter a number bigger then 2 ")

            #function to check if prime
def prime_set(limit: int) ->set:
    primes = set()
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.add(num)
    return primes

prime_number = prime_set(10000)

#main
answer = get_number_input("Enter a number: ")

#checking if entry using built in function isinstance() checking object(anwser) is of specified type(int)
if isinstance(answer, int):                                                         
    if answer in prime_number:
        prime_status = "prime"
    else:
        prime_status = "not prime"
else:
    prime_status = "not an integer, cannot be prime"

#print the result
print(f"The number {answer} is {prime_status}.")