from stories import story, arguments, Success, Failure, Result


class CreatePreUser:
    """
        Create usecase for creating pre-registration user
    """
    @story
    @arguments('email', 'category_name')
    def create(I):
        I.validate_inputs
        I.check_user_existance
        I.fetch_category
        I.create_user
        I.finish

    def validate_inputs(self, ctx):
        if isinstance(ctx.email, str) and isinstance(ctx.category_name, str) and ctx.email != "":
            return Success()
        return Failure(reason="not_validated")
            
    def check_user_existance(self, ctx):
        user = self.core_repo.get_pre_register_user_by_email(email=ctx.email)
        return Failure(reason="user_exists") if user else Success()
    
    def fetch_category(self, ctx):
        ctx.category = self.core_repo.get_category_by_name(name=ctx.category_name)
        return Failure(reason="category_not_found") if not ctx.category else Success()

    def create_user(self, ctx):
        ctx.new_pre_user = self.core_repo.create_pre_register_user(
            email=ctx.email,
            category=ctx.category
        )
        return Success() if ctx.new_pre_user else Failure(reason="repo_error")

    def finish(self,ctx):
        return Result(ctx.new_pre_user)

CreatePreUser.create.failures([
    "not_validated", 
    "user_exists", 
    "category_not_found", 
    "repo_error"
])