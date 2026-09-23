from maintenance_logic import process_maintenance_request


test_requests = [
    {
        "request_id": "DEMO-1001",
        "property": "Demo Property",
        "unit": "101",
        "description": "Example safety-related maintenance request.",
        "safety_hazard": True,
        "essential_service_issue": False,
        "issue_type": "electrical",
        "hours_open": 2,
        "vendor_assigned": False,
        "work_started": False,
        "work_completed": False,
    },
    {
        "request_id": "DEMO-1002",
        "property": "Demo Property",
        "unit": "202",
        "description": "Example essential-service maintenance request.",
        "safety_hazard": False,
        "essential_service_issue": True,
        "issue_type": "hvac",
        "hours_open": 3,
        "vendor_assigned": True,
        "work_started": False,
        "work_completed": False,
    },
    {
        "request_id": "DEMO-1003",
        "property": "Demo Property",
        "unit": "303",
        "description": "Example routine maintenance request.",
        "safety_hazard": False,
        "essential_service_issue": False,
        "issue_type": "general",
        "hours_open": 12,
        "vendor_assigned": True,
        "work_started": True,
        "work_completed": False,
    },
]


expected_results = {
    "DEMO-1001": {
        "priority": "EMERGENCY",
        "assigned_vendor": "ELECTRICAL SERVICE",
        "escalation_status": "REVIEW REQUIRED",
        "request_status": "NEW",
    },
    "DEMO-1002": {
        "priority": "URGENT",
        "assigned_vendor": "HVAC SERVICE",
        "escalation_status": "ON TRACK",
        "request_status": "ASSIGNED",
    },
    "DEMO-1003": {
        "priority": "ROUTINE",
        "assigned_vendor": "GENERAL MAINTENANCE",
        "escalation_status": "ON TRACK",
        "request_status": "IN PROGRESS",
    },
}


def run_tests():
    """
    Validate representative behavior in the public portfolio edition.

    The complete production test suite and business rule scenarios
    are intentionally omitted.
    """
    all_tests_passed = True

    for maintenance_request in test_requests:
        result = process_maintenance_request(maintenance_request)
        request_id = maintenance_request["request_id"]
        expected = expected_results[request_id]

        checks = (
            result["priority"] == expected["priority"]
            and result["assigned_vendor"] == expected["assigned_vendor"]
            and result["escalation_status"] == expected["escalation_status"]
            and result["request_status"] == expected["request_status"]
        )

        if checks:
            print(f"{request_id} PASS")
        else:
            print(f"{request_id} FAIL")
            all_tests_passed = False

    if all_tests_passed:
        print("All public portfolio tests passed.")
    else:
        print("One or more public portfolio tests failed.")

    return all_tests_passed


if __name__ == "__main__":
    run_tests()
