total_number_of_students, number_of_names_on_list = input().split()
total_number_of_students, number_of_names_on_list = int(total_number_of_students), int(number_of_names_on_list)
names_list = [int(i) for i in input().split()]
initial_order = [int(i) for i in input().split()]

while len(names_list) > 1:
    checklist_name = names_list[0]
    student_checked = initial_order[0]

    if checklist_name == student_checked:
        if student_checked in names_list:
            # If index of number(name) in first list is equal or greater than length of second, move it to back
            if names_list.index(student_checked)+1 >= len(initial_order):
                initial_order.append(student_checked)
            # Otherwise, move the student to the position it appears in
            else:
                initial_order.insert(names_list.index(student_checked)+1, student_checked )
        # If number(name) does not appear, put it to back of the list
        else:
            names_list.append(student_checked)

        names_list.pop(0)
        initial_order.pop(0)

    # Almost identical to above, but if the names dont check out
    else:
        if student_checked not in names_list:
            names_list.append(student_checked)
        else:
            if names_list.index(student_checked) >= len(initial_order):
                initial_order.append(student_checked)
            else:
                initial_order.insert(names_list.index(student_checked), student_checked)

        initial_order.pop(0)
