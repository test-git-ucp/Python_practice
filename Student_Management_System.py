lis = []

while True:
    print("\n--- Student Management System ---")
    print("0: Exit program")
    print("1: Add new student data")
    print("2: View all student data")
    print("3: View total number of students")
    print("4: Search student by different method")
    
    i = int(input("Enter value: "))
    
    if i == 0:
        print("✅ Thank you for exiting the program.")
        break
     
    elif i == 1:
        print("\nEnter new student data:")
        name = input("Enter the name: ")
        age = input("Enter the age of student: ")
        rollno = input("Enter roll no: ")
        classs = input("Enter class: ")
        course = input("Enter course name: ")
        marks = input("Enter marks: ")
        
        student = {
            "Name": name,
            "Age": age,
            "Roll No": rollno,
            "Class": classs,
            "Course": course,
            "Marks": marks
        }
        lis.append(student)
        
        with open("output.txt","a")as f:
           f.write(str(student) +"\n")
        print("✅ Student data added successfully!")
    
    elif i == 2:
        print("\n📋 Student Records:")
        if len(lis) == 0:
            print("No student record found.")
        else:
            for s in lis:
                print(s)
    
    elif i == 3:
        print(f"\n📊 Total students in record: {len(lis)}")
        
    elif i == 4:
        print("1.by name:")
        print("2.by roll no:")
        print("3.by age:")
        print("4.by course")
        print("5.by marks")
        
        k=int(input("enter method which u want to use:"))
        if k==1:
            
            name = input("Enter name to search: ")
            found = False
            for s in lis:
                if s["Name"] == name:   # ✅ Correct field
                   print("✅ Student Found:", s)
                   found = True
                   
                else:
                    print("not found use another method")
               
        elif k==2:
            
            roll = input("Enter roll number to search: ")
            found = False
            for s in lis:
                if s["Roll No"] == roll:   # ✅ Correct field
                   print("✅ Student Found:", s)
                   found = True
                   
                else:
                    print("not found use another method:")
        
        elif k==3:
            
            age = input("Enter age to search: ")
            found = False
            for s in lis:
                if s["Age"] == age:   # ✅ Correct field
                   print("✅ Student Found:", s)
                   found = True
                   
                else:
                    print("not found use another method:")
        
        elif k==4:
            
            course = input("Enter by course to search: ")
            found = False
            for s in lis:
                if s["Course"] == course:   # ✅ Correct field
                   print("✅ Student Found:", s)
                   found = True
                   
                else:
                    print("not found use another method:")
        
        elif k==5:
            
            marks = input("Enter roll number to search: ")
            found = False
            for s in lis:
                if s["Marks"] == marks:   # ✅ Correct field
                   print("✅ Student Found:", s)
                   found = True
                   
               
                else:
                    print("❌ Student not found.use another method")
    
    else:
        print("❌ Invalid choice! Please enter a number between 0-4.")
