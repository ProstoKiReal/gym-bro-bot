from aiogram.filters import BaseFilter
from aiogram.types import Message


class WeightFilter(BaseFilter):
    def __init__(self, min_kg: float = 20, max_kg: float = 400):
        self.min_kg = min_kg
        self.max_kg = max_kg

    async def __call__(self, message: Message) -> bool | dict:
        if not message.text:
            return False

        text = message.text.strip().lower().replace(",", ".")
        text = text.removesuffix("kg").removesuffix("кг").strip()

        try:
            weight = float(text)
        except ValueError:
            return False

        if not (self.min_kg <= weight <= self.max_kg):
            return False

        return {"weight": weight}