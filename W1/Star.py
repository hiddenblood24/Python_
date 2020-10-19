ertefah = int(input("enter the number of ertefah: "))
ghaede = int(input("enter the number of ghaede: "))

print()
print()

for row in range(1, ertefah):

    for col in range(1, ghaede):

        if row + col == 5 or col - row == 3:
            print("*", end="")

        else:
            print(end=" ")

    print()

print(ghaede * "*")