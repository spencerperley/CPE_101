list_student=["Ada Lovelace", "Evelyn Boyd Granville ", "Geoffrey Hinton"] 
list_marks = [[79, 90, 89], [91, 78, 89], [81, 82, 89]] 
i = 0
for student in list_student:
    sum = 0
    max = 0
    for marks in list_marks[i]:
        if marks > max:
            max = marks
        sum += marks
    
    print(f"{student} received an average score of {sum/3} and a max score of {max}")
    
    i+=1