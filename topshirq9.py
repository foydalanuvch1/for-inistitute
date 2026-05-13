import os

def create_initial_data(filename):
   

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Aliyev Vali,85\n")
        file.write("Karimova Nargiza,92\n")
        file.write("Toshmatov Jasur,78\n")
        file.write("Olimova Zebo,95\n")

def add_student(filename, name, grade):
   
  
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{name},{grade}\n")

def process_and_analyze(input_filename, output_filename):
    
    students = []
  
    with open(input_filename, 'r', encoding='utf-8') as file:
    
        lines = file.readlines() 
        for line in lines:
            line = line.strip()
            if line: 
                name, grade = line.split(',')
                students.append({'name': name, 'grade': int(grade)})

    if not students:
        print("Ma'lumot topilmadi.")
        return

    
    grades = [s['grade'] for s in students]
    total_students = len(students)
    avg_grade = sum(grades) / total_students
    max_grade = max(grades)
    min_grade = min(grades)

   
    sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)

    with open(output_filename, 'w', encoding='utf-8') as out_file:
        out_file.write(" TALABALAR BAHOLARI TAHLILI \n")
        out_file.write(f"Umumiy talabalar soni: {total_students} ta\n")
        out_file.write(f"O'rtacha ball: {avg_grade:.2f}\n")
        out_file.write(f"Eng yuqori ball: {max_grade}\n")
        out_file.write(f"Eng past ball: {min_grade}\n")
        out_file.write("-" * 35 + "\n")
        out_file.write("Talabalar reytingi (yuqoridan pastga):\n")
        for s in sorted_students:
            out_file.write(f"{s['name']} -> {s['grade']} ball\n")

    print(f"Ma'lumotlar qayta ishlandi va '{output_filename}' fayliga saqlandi.")


if __name__ == "__main__":
    baza_fayli = 'baholar.txt'
    natija_fayli = 'tahlil_natijasi.txt'

 
    create_initial_data(baza_fayli)
    

    add_student(baza_fayli, "Sodiqov Anvar", 88)
    
 
    process_and_analyze(baza_fayli, natija_fayli)








    