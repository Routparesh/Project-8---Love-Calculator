print("Welcome love calculator!")
name_1 = input("Enter name1: ")
name_2 = input("Enter name2: ")
combine = name_1+name_2
lower_case = combine.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = str(t+r+u+e)

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = str(l+o+v+e)

score = int(true+love)
if score < 10 or score > 85:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 70:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")