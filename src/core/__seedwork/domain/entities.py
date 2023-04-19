from abc import ABC
from dataclasses import Field, dataclass, field, asdict
from typing import Any

@dataclass(frozen=True, slots=True)
class Entity(ABC):
    @property
    def id(self): 
        return self.id

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict['id'] = self.id
        return entity_dict

    @classmethod
    def get_field(cls, entity_field: str) -> Field:
        # pylint: disable=no-member
        return cls.__dataclass_fields__[entity_field]
