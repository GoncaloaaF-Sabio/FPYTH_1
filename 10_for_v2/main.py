for i in range(30):
    print(i, end=" ") # print(i, end="\n")

print("")
for i in range(30):
    if i == 15:
        break # termina o loop
    print(i, end=" ") # print(i, end="\n")



print("")
for i in range(30):
    if i % 3 == 0 or i % 5 == 0:
        continue # termina a iter, salta para a volta seguinte

    print(i, end=" ") # print(i, end="\n")



print("\n")
print("fora do loop for")