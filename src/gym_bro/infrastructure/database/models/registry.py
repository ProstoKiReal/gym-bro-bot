from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship

from gym_bro.infrastructure.database.models.base import mapper_registry
from gym_bro.infrastructure.database.models.body_weight import (
    BodyWeightModel,
    body_weights,
)
from gym_bro.infrastructure.database.models.exercise import ExerciseModel, exercises
from gym_bro.infrastructure.database.models.planned_exercise import (
    PlannedExerciseModel,
    planned_exercises,
)
from gym_bro.infrastructure.database.models.profile import ProfileModel, profiles
from gym_bro.infrastructure.database.models.workout import WorkoutModel, workouts
from gym_bro.infrastructure.database.models.workout_exercise import (
    WorkoutExerciseModel,
    workout_exercises,
)
from gym_bro.infrastructure.database.models.workout_program import (
    WorkoutProgramModel,
    workout_programs,
)
from gym_bro.infrastructure.database.models.workout_set import (
    WorkoutSetModel,
    workout_sets,
)
from gym_bro.infrastructure.database.models.workout_template import (
    WorkoutTemplateModel,
    workout_templates,
)


mapper_registry.map_imperatively(ProfileModel, profiles)
mapper_registry.map_imperatively(BodyWeightModel, body_weights)
mapper_registry.map_imperatively(ExerciseModel, exercises)
mapper_registry.map_imperatively(PlannedExerciseModel, planned_exercises)
mapper_registry.map_imperatively(WorkoutSetModel, workout_sets)
mapper_registry.map_imperatively(
    WorkoutProgramModel,
    workout_programs,
    properties={
        "templates": relationship(
            "WorkoutTemplateModel",
            order_by=workout_templates.c.program_position,
            collection_class=ordering_list("program_position", reorder_on_append=True),
        ),
    },
)
mapper_registry.map_imperatively(
    WorkoutTemplateModel,
    workout_templates,
    properties={
        "exercises": relationship(
            "PlannedExerciseModel",
            order_by=planned_exercises.c.position,
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
mapper_registry.map_imperatively(
    WorkoutModel,
    workouts,
    properties={
        "exercises": relationship(
            "WorkoutExerciseModel",
            order_by=workout_exercises.c.position,
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
mapper_registry.map_imperatively(
    WorkoutExerciseModel,
    workout_exercises,
    properties={
        "sets": relationship(
            "WorkoutSetModel",
            order_by=workout_sets.c.position,
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
