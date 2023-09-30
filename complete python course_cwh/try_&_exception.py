a=input("enter number:")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    # or print("invalid input")
    # or print(sorry,error encountered)
print("some imp lines of code")
print("end of program")