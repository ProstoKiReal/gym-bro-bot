from dataclasses import dataclass
from uuid import UUID, uuid4
from typing import Self


@dataclass(frozen=True, slots=True)
class ID:
    value: UUID

    @classmethod
    def new(cls) -> Self:
        return cls(uuid4())
