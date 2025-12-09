import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from va import route_command

def test_audio():
    assert route_command("Play music") == "audio"

def test_phone():
    assert route_command("Call mom") == "phone"

def test_nav():
    assert route_command("Start route to home") == "nav"

def test_empty():
    assert route_command("") == "empty"
