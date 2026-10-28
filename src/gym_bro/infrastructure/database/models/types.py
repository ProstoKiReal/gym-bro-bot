from sqlalchemy import Enum as SAEnum, JSON
from sqlalchemy.ext.mutable import MutableList

from gym_bro.domain.profile.value_objects import Gender
from gym_bro.domain.workout.value_objects import Equipment


profile_gender_type = SAEnum(
    Gender,
    name="profile_gender",
    native_enum=False,
    create_constraint=True,
    values_callable=lambda enum_type: [item.value for item in enum_type],
)
equipment_type = SAEnum(
    Equipment,
    name="equipment",
    native_enum=False,
    create_constraint=True,
    values_callable=lambda enum_type: [item.value for item in enum_type],
)
planned_sets_type = MutableList.as_mutable(JSON)
