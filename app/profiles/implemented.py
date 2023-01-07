from profiles.usecases import (
    CreateBusinessProfile, 
    CreateStandardProfile,
    CreatePROProfile,
    CreateFreeProfile,
    FetchPROProfile,
    FetchStandardProfile
)
from profiles.repository import ProfilesRepository
from users.repository import UserRepository

repo = ProfilesRepository()
user_repo = UserRepository()

# Usecase 1: Create Business Profile
create_business = CreateBusinessProfile()
create_business.repo = repo
create_business.user_repo = user_repo

# Usecase 2: Create Standard Profile
create_standard = CreateStandardProfile()
create_standard.repo = repo
create_standard.user_repo = user_repo

# Usecase 3: Create VIP Profile
create_pro = CreatePROProfile()
create_pro.repo = repo
create_pro.user_repo = user_repo

# Usecase 4: Create Free Profile
create_free = CreateFreeProfile()
create_free.repo = repo 
create_free.user_repo = user_repo

# Usecase 5: Fetch VIP Profile
fetch_pro = FetchPROProfile()
fetch_pro.repo = repo
fetch_pro.user_repo = user_repo

# Usecase 6: Fetch Standard Profile
fetch_standard = FetchStandardProfile()
fetch_standard.repo = repo
fetch_standard.user_repo = user_repo