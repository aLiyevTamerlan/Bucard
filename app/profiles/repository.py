import ipdb

from .models import FreeProfile, Business, ProProfile, StandardProfile
from users.models import User
from app.utils.helpers import generate_qr_code_and_save


class ProfilesRepository:
    def create_free_profile(
        self, 
        user: User) -> FreeProfile:
        new_profile = FreeProfile.objects.create(user=user)
        return new_profile

    def create_business(
        self, 
        user: User, 
        name: str, 
        business_type: str) -> Business:
        type = 1 if business_type == 'general' else 2
        business = Business.objects.create(
            name = name,
            type = type,
            manager = user
        )
        return business
    
    def create_standard(
        self,
        user: User,
        phone_number: str) -> StandardProfile:
        standard_profile = StandardProfile.objects.create(
            user=user,
            phone_number=phone_number,
        )
        return standard_profile
    
    def create_pro_profile(
        self,
        user: User,
        phone_number: str,
        keywords) -> ProProfile:
        pro_profile = ProProfile.objects.create(
            user=user,
            phone_number=phone_number,
            
        )
        pro_profile.keywords.add(keywords)
        return pro_profile

    def get_business(self, name: str) -> Business:
        return Business.objects.filter(name=name).first()
    
    def get_standard(self, user: User) -> StandardProfile:
        return StandardProfile.objects.filter(user=user).first()
    
    def get_pro_profile(self, user: User) -> ProProfile:
        return ProProfile.objects.filter(user=user).first()
    
    def get_free_profile(self, user: User) -> FreeProfile:
        return FreeProfile.objects.filter(user=user).first()

profile_repo = ProfilesRepository()