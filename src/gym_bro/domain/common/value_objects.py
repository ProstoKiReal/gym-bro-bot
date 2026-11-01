from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ID:
    value: UUID

    @classmethod
    def new(cls) -> Self:
        return cls(uuid4())
