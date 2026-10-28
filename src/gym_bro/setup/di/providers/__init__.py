from gym_bro.setup.di.providers.usecases import use_cases_provider
from gym_bro.setup.di.providers.repositories import repositories_provider
from gym_bro.setup.di.providers.db import db_provider
from gym_bro.setup.di.providers.tx_manager import tx_manager_provider


providers = [
    use_cases_provider(),
    repositories_provider(),
    db_provider(),
    tx_manager_provider(),
]
