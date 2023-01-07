from rest_framework_simplejwt.tokens import RefreshToken

from users.repository import user_repo
from users.usecases import CreateUser


# Usecase 1: Create User and generate token
create_user = CreateUser()
create_user.repo = user_repo
create_user.token_service = RefreshToken.for_user