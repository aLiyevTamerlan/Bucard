from users.models import User

class UserRepository:
    
    def create_user(
        self, 
        email: str, 
        password: str) -> User:
        user = User.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
    
    def update_user(self, user, **kwargs) -> User:
        if kwargs.get("password"):
            user.set_password(kwargs.pop("password"))
        for key, value in kwargs.items():
            if value:
                if hasattr(user, key):
                    setattr(user, key, value)

        user.save()
        return user
    
    def get_user(self, id) -> User:
        return User.objects.filter(id=id).first()

    def get_user_by_email(self, email: str) -> User:
        return User.objects.filter(email=email).first()

user_repo = UserRepository()