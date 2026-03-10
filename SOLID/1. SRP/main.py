from user import User
from userRepository import UserRepository

user_obj = User("Vanshika", 50, "info@ghh.com")
user_repo = UserRepository("userDB", "root", "root")

user_obj.get_user_info()
user_repo.save_to_database(user_obj)