class chatbot:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.manu()

    def manu(self):
        user_input = input("""Welcome to the chatbot! Please select an option:
1. sign up
2. sign in
4. forgot password
3. Exit
""")    
        if user_input == "1":
            self.sign_up()
        elif user_input == "2":
            self.sign_in()
        elif user_input == "3":
            print("Exiting the chatbot. Goodbye!")
        elif user_input == "4":
            self.forgot_password()
        else:
            print("Invalid option. Please try again.")
            self.manu() 

    def sign_up(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.name = name
        self.password = password
        print("Sign up successful! You can now sign in.")
        self.manu()
    def sign_in(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name == self.name and password == self.password:
            print("Sign in successful! Welcome back, " + self.name + "!")
        else:
            print("Invalid name or password. Please try again.")
            self.manu()
    def forgot_password(self):        
        name = input("Enter your name: ")
        if name == self.name:
            new_password = input("Enter your new password: ")
            self.password = new_password
            print("Password reset successful! You can now sign in with your new password.")
        else:
            print("Name not found. Please try again.")
            self.manu()

obj=chatbot("Admin","123456")