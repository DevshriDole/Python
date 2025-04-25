
courses = {}

def add_course(courses):
    course_name = input("Enter the course name: ").strip()
    duration = int(input("Enter the duration (in hours): "))
    capacity = int(input("Enter the capacity: "))
    courses[course_name] = (duration, capacity)
    print(f"Course '{course_name}' added successfully.")

def capacity_greater(courses):
    print("Courses with capacity greater than 150: ")
    for course, (duration, capacity) in courses.items():
        if capacity > 150:
            print(f"Course: {course}, Duration: {duration} hours, Capacity: {capacity}")
    
def main():
    while True:
        print("\nMenu:")
        print("1. Add new course")
        print("2. Display all courses with capacity > 150")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_course(courses)

        elif choice == '2':
            capacity_greater(courses)

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
 main()