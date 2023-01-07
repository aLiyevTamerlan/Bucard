from stories import Success, Failure, Result, story, arguments


class CreateFreeProfile:
    @story
    @arguments('user_id')
    def create(I):
        I.validate_inputs
        I.check_user
        I.check_profile
        I.create_profile
        I.finish
    
    def validate_inputs(self, ctx):
        if ctx.user_id:
            return Success()
        return Failure(reason='user_id_required')

    def check_user(self, ctx):
        ctx.user = self.user_repo.get_user(id=ctx.user_id)
        return Success() if ctx.user else Failure(reason='user_not_exists')
    
    def check_profile(self, ctx):
        profile = self.repo.get_free_profile(user=ctx.user)
        return Success() if not profile else Failure(reason='profile_exists')
    
    def create_profile(self, ctx):
        ctx.new_profile = self.repo.create_free_profile(user=ctx.user)
        return Success() if ctx.new_profile else Failure(reason='repo_error')
    
    def finish(self, ctx):
        return Result(ctx.new_profile)

CreateFreeProfile.create.failures(['user_id_required', 'user_not_exists', 'profile_exists', 'repo_error'])