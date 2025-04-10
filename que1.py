def instruction(email_address):
    for adderate in email_address:
        if adderate=='@':
            print("Ok correct you may proceed!!")
            return
    print("No, it is wrong")
            
instruction("Ghimirearnav@gmail.com")