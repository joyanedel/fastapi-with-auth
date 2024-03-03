class AuthenticationFailed(BaseException):
	pass


class UserNotFound(AuthenticationFailed):
	pass


class IncorrectPassword(AuthenticationFailed):
	pass
