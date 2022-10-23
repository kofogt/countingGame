#ternary operator

# age = int(input("What is your age?\n"))
# drink = "Can drink" if age >= 18 else "Can not drink"
# print(drink)

#loops
# for x in "Python":
#     print (x)
# while True:
#     for x in "numbers":
#         print (x)
#         if x == "s":
#             print("done")
#     break
names = ["Jay", "Kay", "say", "way", "Justin", "Jack", "sam"]
jnames = []
# while True:
#     for x in names:
#         if x.startswith("J"):
#             jnames.append(x)
#     if x == "sam":
#         print(jnames)
#         break

for name in names:
    if name.endswith("z"):
        print ("found")
else:
    print ("Not found")

answer = 0
while answer != 10:
    answer= int(input("What is 5+5?"))

