from core.usecases import CheckPromoCode, CreatePromoCode
from core.repository import core_repository
from core.usecases import  CreatePreUser

# Usecase 1: Create Promo Code
create_promo_code = CreatePromoCode()
create_promo_code.repo = core_repository

# Usecase 2: Check Promo Code
check_promo_code = CheckPromoCode()
check_promo_code.repo = core_repository

# Usecase 3: Create Pre User
create_pre_user = CreatePreUser()
create_pre_user.core_repo=core_repository