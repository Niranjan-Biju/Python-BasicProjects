bill = float(input("Enter the bill amount : "))
ppl = int(input("Enter the number of people : "))
tip = int(input("Enter tip % : "))
final_bill = bill * ( 1 + tip / 100)
bpp = final_bill/ppl
bpp = "{:.2f}".format(bpp)
print(f"\nEach person should pay {bpp}")