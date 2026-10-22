
while True:
    print("1. Write Entry\n2. View Entries\n3. Search by Date\n4. Exit")
    choice = input("Choose option  ")
    if choice == '4':
        break
    
    elif choice == '1':
        date = input("Date: ")
        mood = input("Mood (out of 10): ")
        entry = input("Anything you want to write down about today? ")

        with open("journal.txt", "a") as file:
            file.write(f"Date: {date} | Mood: {mood}/10\n")
            file.write(f"Entry: {entry}\n\n")

    elif choice == '2':
        try:
            with open("journal.txt", 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("\nNo entries found yet! Write an entry first.\n")

    elif choice == '3':
        searchdate = input("Enter the date to search for: ")
        try:
            with open("journal.txt", 'r') as file:
                found =  False
                for line in file:
                    if searchdate in line:
                        print("\n--- Entry Found ---")
                        print(line.strip())
                        print(next(file).strip())
                        found = True
                        break

                if not found:
                    print("\nNo entry found for that date.\n")


        except FileNotFoundError:
            print("\nNo journal file found yet! Write an entry first.\n")




    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.\n")