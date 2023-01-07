from core.models import PromoCode, PreRegister, Category

class CoreRepository:
    
    def create_promo_code(
        self,
        name: str,
        discount_percentage: int,
        limit: int,
        is_active: bool) -> PromoCode:
        obj = PromoCode.objects.create(
            name = name,
            discount_percentage = discount_percentage,
            limit = limit,
            is_active = is_active
        )
        return obj
    
    def create_pre_register_user(
        self,
        email: str,
        category: Category) -> PreRegister:
        obj = PreRegister.objects.create(
            email = email,
            category = category
        )
        return obj

    def get_promo_code(self, name: str) -> PromoCode:
        return PromoCode.objects.filter(name=name).first()
    
    def check_promo_code(self, name: str) -> bool:
        return self.get_promo_code(name=name).is_active
    
    def get_pre_register_user_by_email(self, email: str) -> PreRegister:
        return PreRegister.objects.filter(email=email).first()
    
    def get_category(self, id: int) -> Category:
        return Category.objects.filter(id=id).first()
    
    def get_categories(self) -> Category:
        return Category.objects.all()
    
    def get_category_by_name(self, name: str) -> Category:
        return Category.objects.filter(name=name).first()
    
core_repository = CoreRepository()
