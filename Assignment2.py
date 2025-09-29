username = "admin"
password = "1234"
attempt = 1
while attempt <= 3:
    user_username = input("Username: ")
    user_pw = input("Password: ")
    if user_username == username and user_pw == password:
        N = int(input("Enter a number: ")) 
        startingn = 2
        while startingn <= N:
            M = 2
            while M <= startingn:
                if M == startingn:
                    print(startingn)
                    break
                if startingn%M == 0:
                    break
                else: 
                    M += 1
            startingn += 1
        print("Complete")
        break   
    else:
        attempt += 1
        if attempt > 3:
            print("Account locked")
            break
        print("Try again")
