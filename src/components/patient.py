
from dataclasses import dataclass


@dataclass
class Patient:
    mrn: int
    name: str
    age: int
    sex: str
