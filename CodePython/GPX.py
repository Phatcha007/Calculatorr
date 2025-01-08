score = int(input('Enter your Score: '))    
print ("คะแนนของคุณ คือ  ",score)
garde = None

if score >= 80 and score <= 100:
    grade = "A"
elif score >= 70 and score < 79:
    grade = "B"
elif score >= 60 and score < 69:
    grade = "C"
elif score >= 50 and score < 59:
    grade = "D"
elif score >= 0 and score < 49:
    grade = "F"

print ("Your Grade is: ", grade)