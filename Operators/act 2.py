Amount = int(input("Please enter Amount for withdraw: "))

note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = ((Amount % 100) % 50) // 10

print ("Note of 100 is: ", note_1)
print ("Note of 50 is: ", note_2)
print ("Note of 10 is: ", note_3)