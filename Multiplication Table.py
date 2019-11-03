print(" ")
print('"Multiplication Table"')
print(" ")

tble = int(input("'Table of': "))

print(" ")
print('TABLE OF ' + str(tble) + '!')
print(" ")

for x in range(1,11):
    print(str(tble) + ' x ' + str(x) + ' = ' + str(tble * x))

print(" ")