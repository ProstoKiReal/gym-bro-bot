from gym_bro.core.domain.profile.entities import Profile


class RegisterProfile:
    def __call__(
        self,
        telegram_id: int,
        first_name: str,
        last_name: str | None = None,
    ) -> Profile:
        raise NotImplementedError
