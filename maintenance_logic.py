"""
HerCode Property Management Maintenance Automation
Public Portfolio Edition

This module demonstrates the structure used to process maintenance
requests while intentionally omitting the complete production
business rule configuration.
"""


def determine_priority(request):
    """
    Demonstrate rule based maintenance prioritization.
    Additional production rules are intentionally omitted.
    """
    if request.get("safety_hazard", False):
        return "EMERGENCY"

    if request.get("essential_service_issue", False):
        return "URGENT"

    return "ROUTINE"


def determine_vendor(request):
    """
    Route a maintenance request to an appropriate service category.
    The production implementation supports additional routing rules.
    """
    vendor_routes = {
        "plumbing": "PLUMBING SERVICE",
        "electrical": "ELECTRICAL SERVICE",
        "hvac": "HVAC SERVICE",
    }

    return vendor_routes.get(
        request.get("issue_type"),
        "GENERAL MAINTENANCE"
    )


def determine_escalation(priority, hours_open):
    """
    Demonstrate time based escalation logic.

    Production escalation thresholds and workflow conditions
    are intentionally omitted from the public portfolio version.
    """
    portfolio_thresholds = {
        "EMERGENCY": 2,
        "URGENT": 6,
        "ROUTINE": 72,
    }

    threshold = portfolio_thresholds.get(priority)

    if threshold is not None and hours_open >= threshold:
        return "REVIEW REQUIRED"

    return "ON TRACK"


def determine_status(vendor_assigned, work_started, work_completed):
    """
    Determine the current workflow status of a maintenance request.
    """
    if work_completed:
        return "COMPLETED"

    if work_started:
        return "IN PROGRESS"

    if vendor_assigned:
        return "ASSIGNED"

    return "NEW"


def process_maintenance_request(request):
    """
    Process a maintenance request and return structured
    operational information.
    """
    priority = determine_priority(request)

    return {
        "request_id": request.get("request_id"),
        "property": request.get("property"),
        "unit": request.get("unit"),
        "description": request.get("description"),
        "priority": priority,
        "assigned_vendor": determine_vendor(request),
        "escalation_status": determine_escalation(
            priority,
            request.get("hours_open", 0),
        ),
        "request_status": determine_status(
            request.get("vendor_assigned", False),
            request.get("work_started", False),
            request.get("work_completed", False),
        ),
    }
