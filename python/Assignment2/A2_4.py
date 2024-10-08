from collections import defaultdict

class AttendanceSystem:
    def __init__(self):
        self.attendance_records = defaultdict(list)
        self.absence_records = defaultdict(int)
    
    def add_attendance(self, employee_name, date, hours_worked):
        self.attendance_records[employee_name].append({"date": date, "hours_worked": hours_worked})
        if hours_worked == 0:
            self.absence_records[employee_name] += 1
    
    def total_hours_worked(self, employee_name):
        total_hours = sum(record["hours_worked"] for record in self.attendance_records[employee_name])
        return total_hours
    
    def perfect_attendance(self):
        perfect_employees = [name for name, records in self.attendance_records.items() if all(record["hours_worked"] > 0 for record in records)]
        return perfect_employees
    
    def most_absences(self):
        if not self.absence_records:
            return None
        max_absences = max(self.absence_records.values())
        most_absent_employees = [name for name, absences in self.absence_records.items() if absences == max_absences]
        return most_absent_employees
    
    def display_attendance_summary(self):
        print("\nAttendance Summary:")
        for employee_name in self.attendance_records:
            total_hours = self.total_hours_worked(employee_name)
            print(f"{employee_name}: Total Hours Worked: {total_hours}, Absences: {self.absence_records[employee_name]}")
    
def main():
    attendance_system = AttendanceSystem()
    
    while True:
        print("\nEmployee Attendance System")
        print("1. Add Attendance Record")
        print("2. View Total Hours Worked")
        print("3. View Employees with Perfect Attendance")
        print("4. View Employees with Most Absences")
        print("5. Display Attendance Summary")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            employee_name = input("Enter employee name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            hours_worked = float(input("Enter hours worked (0 if absent): "))
            attendance_system.add_attendance(employee_name, date, hours_worked)
            print(f"Attendance record added for {employee_name} on {date}.")
        
        elif choice == "2":
            employee_name = input("Enter employee name: ")
            total_hours = attendance_system.total_hours_worked(employee_name)
            print(f"Total hours worked by {employee_name}: {total_hours}")
        
        elif choice == "3":
            perfect_employees = attendance_system.perfect_attendance()
            if perfect_employees:
                print("\nEmployees with Perfect Attendance:")
                for name in perfect_employees:
                    print(name)
            else:
                print("No employees with perfect attendance.")
        
        elif choice == "4":
            most_absent_employees = attendance_system.most_absences()
            if most_absent_employees:
                print("\nEmployees with the Most Absences:")
                for name in most_absent_employees:
                    print(name)
            else:
                print("No absences recorded.")
        
        elif choice == "5":
            attendance_system.display_attendance_summary()
        
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()