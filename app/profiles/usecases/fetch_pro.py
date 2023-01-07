from stories import story, arguments, Success, Failure, Result


class FetchPROProfile:
    @story
    @arguments('user_id')
    def apply(I):
        I.validate_inputs
        I.fetch_user
        I.fetch_profile
        I.finish
    
    def validate_inputs(self, ctx):
        if ctx.user_id:
            # If validation is successful method will return Success
            return Success()
        return Failure(reason='not_validated')
    
    def fetch_user(self, ctx):
        ctx.user = self.user_repo.get_user(id=ctx.user_id)
        return Success() if ctx.user else Failure(reason='user_not_exists')
    
    def fetch_profile(self, ctx):
        ctx.profile = self.repo.get_pro_profile(user=ctx.user)
        return Success() if ctx.profile else Failure(reason='repo_error')

    def finish(self, ctx):
        return Result(ctx.profile)


FetchPROProfile.apply.failures([
    'not_validated', 
    'user_not_exists',
    'repo_error', 
])
