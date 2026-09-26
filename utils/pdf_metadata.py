import pymupdf

from typing import List
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ProblemSet:
    title: str
    author: str
    filename: str
    last_edit: str


def extract_pdf_metadata(pdf_path: Path) -> List[ProblemSet]:
    problem_set = []
    for pdf_file in pdf_path.iterdir():
        with pymupdf.open(pdf_file) as document:
            # Extract and format raw data from first page
            first_page_data = [
                i.strip()
                for i in document[0].get_text("text", sort=True).split("\n")
                if i.strip()
            ]

        problem_set.append(
            ProblemSet(
                title=first_page_data[0],
                author=first_page_data[1].split(" - ")[0],
                filename=pdf_file.name,
                last_edit=first_page_data[1].split(" - ")[-1],
            )
        )

    return problem_set


if __name__ == "__main__":
    test_path = Path(Path(__file__).parent.parent, "static", "problem_sets_junior")
    test_problem_set = extract_pdf_metadata(test_path)
    print(test_problem_set)
