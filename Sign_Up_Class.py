from abc import ABC, abstractmethod

class Student_Signup:
  def __init__(self, name, mobile, email, password):
    self.name = name
    self.mobile = mobile
    self.email = email
    self.__password = password

  def save_to_file(self):
    student_data = f"{self.name},{self.mobile},{self.email},{self.__password}\n"
    try:
      with open("students.txt", "a") as file:
        file.write(student_data)
      print(f"\n\t[SUCCESS] Account for {self.name} created & saved to file!")
    except Exception as e:
      print(f"\n\t[ERROR] Error saving student data: {e}")


class Student_Login:
  def __init__(self, email, password):
    self.email = email
    self.__password = password

  def verify_login(self):
    try:
      with open("students.txt", "r") as file:
        for line in file:
          parts = line.strip().split(",")
          if len(parts) == 4:
            name, mobile, email, password = parts
            if email == self.email and password == self.__password:
              print(f"\n\t[SUCCESS] Login Successful! Welcome back, {name}.")
              return {"name": name, "mobile": mobile, "email": email}
      print("\n\t[ERROR] Invalid Email or Password!")
      return None
    except FileNotFoundError:
      print("\n\t[ERROR] No registered students found. Please sign up first!")
      return None


class Institute_Portal:
    def __init__(self, institute_name, institute_id, password):
        self.institute_name = institute_name
        self.institute_id = institute_id
        self.__password = password
        self.attendance = 0
        self.marks_10th = 0
        self.marks_12th = 0
        self.marks_plus3_1st_year = 0

    def verify_institute_login(self, input_id, input_password):
        if self.institute_id == input_id and self.__password == input_password:
            print(f"\n\t[INSTITUTE LOGIN SUCCESS] Connected to: {self.institute_name}")
            return True
        else:
            print("\n\t[ERROR] Invalid Institute ID or Password!")
            return False

    def fetch_student_record(self, student_email):
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        name, mobile, email, password = parts
                        if email == student_email:
                            print(f"\t[DATABASE] Record found for student: {name}")
                            return {"name": name, "mobile": mobile, "email": email}
            print("\t[DATABASE] Student not found in database!")
            return None
        except FileNotFoundError:
            print("\t[ERROR] Student database file not found!")
            return None

    def add_academic_records(self, attendance, m10, m12, m_plus3):
        self.attendance = attendance
        self.marks_10th = m10
        self.marks_12th = m12
        self.marks_plus3_1st_year = m_plus3
        print(f"\n\t[PORTAL UPDATE] Academic records imported successfully for [{self.institute_name}].")


class ScholarshipInterface(ABC):
  @abstractmethod
  def evaluate_scholarship(self):
    pass


class LaptopYojanaScholarship(ScholarshipInterface):
  def __init__(self, institute_record_obj, student_data):
    self.record = institute_record_obj
    self.student = student_data

  def evaluate_scholarship(self):
    avg_marks = (self.record.marks_10th + self.record.marks_12th + self.record.marks_plus3_1st_year) / 3
    attendance = self.record.attendance

    print("\n" + "="*60)
    print("\t\t--- SCHOLARSHIP EVALUATION STATUS ---")
    print("="*60)
    print(f"\t• Institute   : {self.record.institute_name}")
    print(f"\t• Student Name: {self.student['name']}")
    print(f"\t• Attendance  : {attendance}%")
    print(f"\t• Average Mark: {avg_marks:.2f}%")
    print("-"*60)

    if attendance >= 75 and avg_marks >= 75:
      print(f"\tCONGRATULATIONS {self.student['name']}!\n\t   You are ELIGIBLE for ₹10,000 Laptop Yojana Grant!")
    else:
      print(f"\tSorry {self.student['name']},\n\t   You do NOT meet the 75% criteria for Laptop Yojana.")
    print("="*60)


while True:
    print("\n" + "="*25 + " SAMS PORTAL MENU " + "="*25)
    print("\t1. Student Signup")
    print("\t2. Student Login")
    print("\t3. Institute Portal & Scholarship Evaluation")
    print("\t4. Exit")
    print("="*68)
    
    choice = input("\tEnter your choice (1-4): ")

    match choice:
        case "1":
            print("\n" + "="*25 + " STUDENT REGISTRATION " + "="*25)
            s_name = input("\tEnter your name          : ")
            s_mobile = input("\tEnter your mobile number : ")
            s_email = input("\tEnter your email         : ")
            s_password = input("\tEnter your password      : ")
            s1 = Student_Signup(s_name, s_mobile, s_email, s_password)
            s1.save_to_file()

        case "2":
            print("\n" + "="*25 + " STUDENT LOGIN VERIFICATION " + "="*25)
            s_email = input("\tEnter your email    : ")
            s_password = input("\tEnter your password : ")
            login_attempt = Student_Login(s_email, s_password)
            login_attempt.verify_login()

        case "3":
            print("\n" + "="*25 + " INSTITUTE PORTAL LOGIN " + "="*25)
            I_name = input("\tEnter Institute Name     : ")
            I_id = input("\tEnter Institute ID       : ")
            I_password = input("\tEnter Institute Password : ")

            college = Institute_Portal(I_name, I_id, I_password)
            is_institute_logged_in = college.verify_institute_login(I_id, I_password)

            if is_institute_logged_in:
                student_email = input("\tEnter Student Email to Fetch Record: ")
                print("\n" + "="*25 + " FETCHING STUDENT RECORD " + "="*25)
                student_info = college.fetch_student_record(student_email)
                
                if student_info:
                    print("\n" + "="*25 + " ENTER ACADEMIC DETAILS " + "="*25)
                    attend = int(input(f"\tEnter {student_info['name']}'s attendance %      : "))
                    m_10 = int(input(f"\tEnter {student_info['name']}'s 10th marks %        : "))
                    m_12 = int(input(f"\tEnter {student_info['name']}'s 12th marks %        : "))
                    m_plus3 = int(input(f"\tEnter {student_info['name']}'s +3 1st year marks % : "))

                    college.add_academic_records(attendance=attend, m10=m_10, m12=m_12, m_plus3=m_plus3)
                    scholarship_app = LaptopYojanaScholarship(college, student_info)
                    scholarship_app.evaluate_scholarship()

        case "4":
            print("\n\tExiting application. Thank you!")
            break

        case _:
            print("\n\t[ERROR] Invalid choice! Please enter a number between 1 and 4.")