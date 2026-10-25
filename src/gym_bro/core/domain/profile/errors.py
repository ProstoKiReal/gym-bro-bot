from gym_bro.core.domain.common.errors import BaseDomainError


class InvalidNameError(BaseDomainError):
    def __init__(self, name: str):
        super().__init__("Profile name cannot be empty.")
        self.name = name


class InvalidTelegramIDError(BaseDomainError):
    def __init__(self, telegram_id: object):
        super().__init__(f"Telegram ID must be a positive integer; got {telegram_id}.")
