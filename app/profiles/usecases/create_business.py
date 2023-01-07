from stories import story, arguments, Success, Failure, Result


class CreateBusinessProfile:
    @story
    @arguments('user_id', 'args')
    def create(I):
        I.validate_inputs
        I.fetch_user
        I.fetch_business
        I.create_business
        I.finish
    
    def validate_inputs(self, ctx):
        if (isinstance(ctx.args.get('name'), str) and
            isinstance(ctx.args.get('type'), str)):
            # If validation is successful method will return Success
            return Success()
        return Failure(reason='not_validated')
    
    def fetch_user(self, ctx):
        ctx.user = self.user_repo.get_user(id=ctx.user_id)
        return Success() if ctx.user else Failure(reason='user_not_exists')
    
    def fetch_business(self, ctx):
        business = self.repo.get_business(name=ctx.args.get('name'))
        return Failure(reason='business_exists') if business else Success()

    def create_business(self, ctx):
        ctx.profile = self.repo.create_business(
            user=ctx.user,
            name=ctx.args.get('name'),
            business_type=ctx.args.get('type'),
        )
        return Success() if ctx.profile else Failure(reason='repo_error')

    def finish(self, ctx):
        return Result(ctx.profile)


CreateBusinessProfile.create.failures([
    'not_validated', 
    'user_not_exists',
    'business_exists', 
    'repo_error'
])
