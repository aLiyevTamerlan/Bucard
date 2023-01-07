from stories import story, arguments, Success, Failure, Result


class CheckPromoCode:
    @story
    @arguments('name')
    def check(I):
        I.validate_input
        I.fetch_promo_code
        I.check_code
        I.done
    
    def validate_input(self, ctx):
        if isinstance(ctx.name, str) and ctx.name:
            return Success()
            
        return Failure(reason="not_validated")

    def fetch_promo_code(self, ctx):
        ctx.code = self.repo.get_promo_code(name=ctx.name)
        return Success() if ctx.code else Failure(reason="code_not_exists")
    
    def check_code(self, ctx):
        if ctx.code.is_active:
            return Success()
        return Failure(reason="code_not_active")
    
    def done(self, ctx):
        return Result(ctx.code)

CheckPromoCode.check.failures(["not_validated", "code_not_exists", "code_not_active"])
