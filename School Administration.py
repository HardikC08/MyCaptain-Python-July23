#Project : Basic School Administration Tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv' , 'a' , newline = '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name" , "Age" , "Contact No." , "Email ID"])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while (condition):
        student_info = input("Enter information for student #{} (Name , Age , Contact no. , Email) : ".format(student_num))

        #split
        student_info_list = student_info.split(' ')

        print("\nThe entered information is -\n Name: {}\n Age: {}\n Contact No.: {}\n Email ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        
        choice_check = input("Is the entered information correct? (Y / N) : ")
        
        if choice_check == "Y":
            write_into_csv(student_info_list)

            condition_check = input("Enter [Yes/No] if you wish to continue for another student : ")
            if condition_check == "Yes":
                condition = True
                student_num = student_num + 1 
            elif condition_check == "No":
                condition = False
        elif choice_check == "N":
            print("\nPlease re-enter the values!")