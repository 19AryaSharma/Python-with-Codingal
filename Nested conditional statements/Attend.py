medical_cause = input("Is there a medical cause for your absence? (Y/N): ")
atten = int(input("Enter the attendence of the student: "))

if medical_cause == "Y":
 print("You are allowed")
else:
 if atten >= 75:
  print("you are allowed")

 else:
  print("go back to your home")