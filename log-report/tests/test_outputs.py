import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    """Load report.json, failing the test if it is missing, empty, or invalid JSON."""
    assert REPORT.exists(), "no /app/report.json found"
    assert REPORT.stat().st_size > 0, "report.json is empty"
    with REPORT.open() as f:
        return json.load(f)  # invalid JSON -> raises -> test fails


def test_total_requests():
    """6 request lines in the access log."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """3 distinct client IPs: 192.168.0.1, 192.168.0.2, 10.0.0.5."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """/index.html is requested 3 times, more than any other path."""
    assert load_report()["top_path"] == "/index.html"
