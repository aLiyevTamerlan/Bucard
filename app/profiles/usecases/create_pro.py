from stories import story, arguments, Success, Failure, Result
from profiles.models import Keyword

class CreatePROProfile:
    @story
    @arguments('user_id', 'args')
    def create(I):
        I.validate_inputs
        I.fetch_user
        I.fetch_profile
        I.update_user
        I.create_profile
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
    
    def fetch_profile(self, ctx):
        profile = self.repo.get_pro_profile(user=ctx.user)
        return Failure(reason='pro_profile_exists') if profile else Success()
    
    def update_user(self, ctx):
        ctx.updated_user = self.user_repo.update_user(
            user=ctx.user,
            name=ctx.args.get('name'),
            surname=ctx.args.get('surname')
        )
        return Success() if ctx.updated_user else Failure(reason='repo_error')

    def create_profile(self, ctx):
        keyword=Keyword.objects.get(name=ctx.args.get('keyword'))
        ctx.new_profile = self.repo.create_pro_profile(
            user=ctx.user,
            phone_number=ctx.args.get('phone_number'),
            keywords=keyword,
        )
        return Success() if ctx.new_profile else Failure(reason='repo_error')

    def finish(self, ctx):
        return Result(ctx.new_profile)


CreatePROProfile.create.failures([
    'not_validated', 
    'user_not_exists',
    'pro_profile_exists', 
    'repo_error'
])
