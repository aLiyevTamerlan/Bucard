from stories import story, arguments, Success, Failure, Result


class CreateUser:
    """
        Create usecase for creating new user
    """
    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        I.check_user_existance
        I.create_user
        I.generate_jwt_token
        I.finish

    def validate_inputs(self, ctx):
        ### Validate inputs ###
        if (isinstance(ctx.args.get('email'), str) and
            isinstance(ctx.args.get('password'), str)):
            return Success()

        return Failure(reason="not_validated")
    
    def check_user_existance(self, ctx):
        ### Checking user existance ###
        user = self.repo.get_user_by_email(email=ctx.args.get('email'))
        return Failure(reason="user_exists") if user else Success() 
    
    def create_user(self, ctx):
        ### Creating new user if user does not exist in db ###
        ctx.new_user = self.repo.create_user(
            email = ctx.args.get('email'),
            password = ctx.args.get('password')
        )
        return Success() if ctx.new_user else Failure(reason="repo_error")
    
    def generate_jwt_token(self, ctx):
        ctx.user_token = self.token_service(ctx.new_user)
        return Success()
    
    def finish(self, ctx):
        return Result((ctx.new_user, ctx.user_token))

CreateUser.create.failures(["not_validated", "user_exists",  "repo_error"])
