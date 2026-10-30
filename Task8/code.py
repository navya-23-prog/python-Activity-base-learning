
# Student Timetable Conflict Detection

# Function to convert HH:MM time into minutes
def convert_time(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


# Function to check time overlap
def check_overlap(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1


# Existing timetable stored as tuples
# (Course, Day, Start Time, End Time, Room)

existing_timetable = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Mathematics", "Monday", "10:00", "11:00", "R102"),
    ("Physics", "Tuesday", "09:00", "10:30", "R103"),
    ("Chemistry", "Wednesday", "11:00", "12:00", "R101")
]

# Unavailable rooms
unavailable_rooms = [
    ("R101", "Monday", "11:00", "12:00"),
    ("R102", "Tuesday", "09:00", "11:00"),
    ("R103", "Wednesday", "10:00", "12:00")
]

# Read proposed timetable
proposed_timetable = []

n = int(input("Enter number of proposed courses: "))

for i in range(n):
    print("\nEnter details for course", i + 1)

    course = input("Course name: ")
    day = input("Day: ")
    start = input("Start time (HH:MM): ")
    end = input("End time (HH:MM): ")
    room = input("Room number: ")

    proposed_timetable.append(
        (course, day, start, end, room)
    )

# Conflict detection
conflict_found = False

print("\n========== TIMETABLE VALIDATION ==========")

for proposed in proposed_timetable:

    course, day, start, end, room = proposed

    start_minutes = convert_time(start)
    end_minutes = convert_time(end)

    print("\nCourse:", course)

    if start_minutes >= end_minutes:
        print("Invalid time period.")
        conflict_found = True
        continue

    # Compare with existing timetable
    for existing in existing_timetable:

        old_course, old_day, old_start, old_end, old_room = existing

        if day == old_day:

            old_start_minutes = convert_time(old_start)
            old_end_minutes = convert_time(old_end)

            if check_overlap(
                start_minutes, end_minutes,
                old_start_minutes, old_end_minutes
            ):

                print("Student Timetable Conflict with:",
                      old_course)
                conflict_found = True

                if room == old_room:
                    print("Room Conflict with:",
                          old_course)
                    conflict_found = True

    # Check conflicts between proposed courses
    for other in proposed_timetable:

        if proposed == other:
            continue

        other_course, other_day, other_start, other_end, other_room = other

        if course < other_course and day == other_day:

            other_start_minutes = convert_time(other_start)
            other_end_minutes = convert_time(other_end)

            if check_overlap(
                start_minutes, end_minutes,
                other_start_minutes, other_end_minutes
            ):

                print("Conflict with proposed course:",
                      other_course)
                conflict_found = True

                if room == other_room:
                    print("Same room is assigned to both courses.")

    # Check unavailable rooms
    for unavailable in unavailable_rooms:

        unavailable_room, unavailable_day, u_start, u_end = unavailable

        if room == unavailable_room and day == unavailable_day:

            u_start_minutes = convert_time(u_start)
            u_end_minutes = convert_time(u_end)

            if check_overlap(
                start_minutes, end_minutes,
                u_start_minutes, u_end_minutes
            ):

                print("Room", room, "is unavailable.")
                conflict_found = True

if conflict_found:
    print("\nResult: Timetable Contains Conflicts.")
else:
    print("\nResult: Timetable is Valid.")

