class chatbot:
    __user_id=0 #class variable 

    def __init__(self):
        self.id=chatbot.__user_id+1
        chatbot.__user_id=self.id
        self.__username="adi" #hidden attribute
        self.name = 'admin'
        self.password = '123456'
        self.manu()

    @staticmethod
    def get_user_id():
        return chatbot.__user_id
    
    @staticmethod
    def set_user_id(user_id):
        chatbot.__user_id = user_id 
        return chatbot.__user_id
    
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

obj=chatbot()
print("User ID:", obj.id)   