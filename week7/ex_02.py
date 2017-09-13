largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = float(num)
     except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = inum
    if inum > largest:
        largest = inum
    elif inum < smallest:
        smallest = inum

def stop(largest, smallest):
    print("Maximum", int(largest)
    print("Minimum", int(smallest)

stop(largest,smallest)
