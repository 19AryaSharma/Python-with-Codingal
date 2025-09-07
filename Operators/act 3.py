print("Enter marks obtained in 4 subjects:")
Maths = int(input("Maths: "))
Science = int(input("Science: "))
English = int(input("English: "))
Hindi = int(input("Hindi: "))

sum = Maths + Science + English + Hindi
print("Total marks obtained in 4 subjects is", sum)

perc = (sum / 400) * 100

print(end= "percentage marks: ")
print(perc)