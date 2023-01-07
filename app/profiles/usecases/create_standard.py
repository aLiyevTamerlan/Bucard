from stories import story, arguments, Success, Failure, Result


class CreateStandardProfile:
    @story
    @arguments('user_id', 'args')
    def create(I):
        I.validate_inputs
        I.fetch_user
        I.fetch_standard
        I.create_standard
        I.finish
    
    def validate_inputs(self, ctx):
        if (isinstance(ctx.args.get('name'), str) and
            isinstance(ctx.args.get('surname'), str) and
            isinstance(ctx.args.get('phone_number'), str)):
            # If validation is successful method will return Success
            return Success()
        return Failure(reason='not_validated')
    
    def fetch_user(self, ctx):
        ctx.user = self.user_repo.get_user(id=ctx.user_id)
        return Success() if ctx.user else Failure(reason='user_not_exists')
    
    def fetch_standard(self, ctx):
        standard = self.repo.get_standard(user=ctx.user)
        return Failure(reason='standard_profile_exists') if standard else Success()
    
    def update_user(self, ctx):
        ctx.updated_user = self.user_repo.update_user(
            user=ctx.user,
            name=ctx.args.get('name'),
            surname=ctx.args.get('surname')
        )
        return Success() if ctx.updated_user else Failure(reason='repo_error')

    def create_standard(self, ctx):
        ctx.standard = self.repo.create_standard(
            user=ctx.user,
            phone_number=ctx.args.get('phone_number'),
            profile_link=ctx.args.get('profile_link'),
        )
        return Success() if ctx.standard else Failure(reason='repo_error')

    def finish(self, ctx):
        return Result(ctx.standard)


CreateStandardProfile.create.failures([
    'not_validated', 
    'user_not_exists',
    'standard_profile_exists', 
    'repo_error'
])
