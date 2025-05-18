inputs = ["Ram", "Kavi", "siva"]
correct_password = "siva"
for attempt in inputs:
    if attempt == correct_password:
        print("Access Granted")
        break
else:
    print("Account Locked")