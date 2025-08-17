from typing import Optional

# Map categories to license requirements
CATEGORY_LICENSES = {
    "Plumbing": "state_license_required",
    "Electrical": "state_license_required",
    "HVAC": "state_license_required",
    "Pest Control": "licensed_preferred",
    "House Cleaning": "no_license_required",
    "Lawn Care": "no_license_required",
    "Appliance Installation": "licensed_preferred",
    "Painting": "no_license_required",
}

def get_license_requirement(category: Optional[str]) -> str:
    """
    Returns the license requirement for the given service category.
    If category is None or unknown, defaults to 'unknown'.
    """
    if not category:
        return "unknown"
    return CATEGORY_LICENSES.get(category, "unknown")
