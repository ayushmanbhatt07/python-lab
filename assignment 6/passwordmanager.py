# Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class Password_manager:
    def __init__(self, initial_password):
        self.old_passwords = [initial_password]
    
    def get_password(self):
        return self.old_passwords[-1]
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        else:
            return False
    
    def is_correct(self, password_to_check):
        return password_to_check == self.get_password()
# Create a Password_manager with initial password "password123"
pm = Password_manager("password123")

# Get current password
print(pm.get_password())  # Output: "password123"

# Try to set a new password (different from old ones)
print(pm.set_password("newPass456"))  # Output: True
print(pm.get_password())  # Output: "newPass456"

# Try to set a password that was used before
print(pm.set_password("password123"))  # Output: False (not set)
print(pm.get_password())  # Output: "newPass456" (unchanged)

# Check if a password is correct
print(pm.is_correct("newPass456"))  # Output: True
print(pm.is_correct("wrongPass"))   # Output: False