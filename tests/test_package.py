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

    