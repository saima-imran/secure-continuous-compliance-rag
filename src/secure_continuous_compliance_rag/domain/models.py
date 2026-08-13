from dataclasses import dataclass


@dataclass(frozen=True)
class SoftwareRequirement:
    requirement_id: str
    title: str
    text: str
    version: int
    

