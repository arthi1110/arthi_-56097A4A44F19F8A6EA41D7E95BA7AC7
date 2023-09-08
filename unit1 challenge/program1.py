#recursive factorial
def rec_fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * rec_fact(n - 1)


number = int(input("Enter the value:"))
res = rec_fact(number)
print("the factorial of {} is {}.".format(number, res))