from dataclasses import dataclass


@dataclass(frozen=True)
class SoftwareRequirement:
    requirement_id: str
    title: str
    text: str
    version: int
    def __post_init__(self) -> None:
        if self.version <= 0:
            raise ValueError("version must be positive")
        

