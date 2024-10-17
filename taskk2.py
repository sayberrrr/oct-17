single_array = [ "bugs", "kibuloy", "alimatuk", "fablo", "burnok"]
two_array = [["kibu", "ali", "ampungol"], ["sayber", "ryan", "tantan"], ["micco", "blanza", "balot"]]


def display_single_array(arr):
    for item in arr:
        print(item)


def display_two_array(arr):
    for sublist in arr:
        for item in sublist:
            print(item, end=' ')
        print()


user_choice = input("Enter '1' to display single-dimensional array or '2' to display two-dimensional array: ")

if user_choice == '1':
    display_single_array(single_array)
elif user_choice == '2':
    display_two_array(two_array)
else:
    print("Invalid choice. Please enter either '1' or '2'.")
