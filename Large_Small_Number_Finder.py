largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    try:
        number = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
            continue

    if largest is None:
        largest = number
    elif number > largest:
        largest = number

    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

print("Maximum is ", largest)
print("Minimum is ", smallest)