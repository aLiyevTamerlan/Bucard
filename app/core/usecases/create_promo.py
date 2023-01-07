from stories import Success, Failure, Result, story, arguments


class CreatePromoCode:
    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        I.check_code_existance
        I.create_code
        I.finish
    
    def validate_inputs(self, ctx):
        if (isinstance(ctx.args.get('name'), str) and 
            isinstance(ctx.args.get('discount_percentage'), int) and
            isinstance(ctx.args.get('limit'), int) and
            isinstance(ctx.args.get('is_active'), bool)):
            return Success()
        return Failure(reason="not_validated")
    
    def check_code_existance(self, ctx):
        code = self.repo.get_promo_code(name=ctx.args.get('name'))

        return Failure(reason='code_exists') if code else Success()

    def create_code(self, ctx):
        ctx.code = self.repo.create_promo_code(
            name = ctx.args.get('name'),
            discount_percentage = ctx.args.get('discount_percentage'),
            limit = ctx.args.get('limit'),
            is_active = ctx.args.get('is_active')
        )

        return Success() if ctx.code else Failure(reason="repo_error")
    
    def finish(self, ctx):
        return Result(ctx.code)

CreatePromoCode.create.failures(["not_validated", "code_exists", "repo_error"])
