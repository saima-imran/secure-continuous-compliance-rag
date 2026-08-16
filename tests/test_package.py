import pytest

from secure_continuous_compliance_rag.domain.models import SoftwareRequirement


def test_software_requirement_stores_its_data() -> None:
    requirement = SoftwareRequirement(
        requirement_id="SR-001",
        title="Human override",
        text="The system shall allow an authorized operator to stop the AI function.",
        version=1,
    )

    assert requirement.requirement_id == "SR-001"
    assert requirement.version == 1


def test_software_requirement_rejects_non_positive_version() -> None:
    with pytest.raises(ValueError, match="version must be positive"):
        SoftwareRequirement(
            requirement_id="SR-001",
            title="Human override",
            text="The system shall allow an operator to stop the AI function.",
            version=0,
        )


def test_software_requirement_rejects_empty_id() -> None:
    with pytest.raises(ValueError, match="requirement_id must not be empty"):
        SoftwareRequirement(
            requirement_id="",
            title="Human override",
            text="The system shall allow an operator to stop the AI function.",
            version=1,
        )


@pytest.mark.parametrize(
    ("field_name", "empty_value", "expected_message"),
    [
        ("title", "", "title must not be empty"),
        ("text", "", "text must not be empty"),
    ],
)
def test_software_requirement_rejects_empty_content(
    field_name: str,
    empty_value: str,
    expected_message: str,
) -> None:
    values = {
        "requirement_id": "SR-001",
        "title": "Human override",
        "text": "The system shall allow an operator to stop the AI function.",
        "version": 1,
    }
    values[field_name] = empty_value

    with pytest.raises(ValueError, match=expected_message):
        SoftwareRequirement(**values)  # type: ignore[arg-type]
