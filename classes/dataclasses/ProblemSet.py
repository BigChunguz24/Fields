from dataclasses import dataclass


@dataclass
class ProblemSet:
    title: str
    author: str
    filename: str
    last_edit: str
