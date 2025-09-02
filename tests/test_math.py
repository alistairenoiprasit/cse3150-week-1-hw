import os
import subprocess
import glob
import pytest

# AI DECLARATION:
# I used AI for the following function to compile a math program
# within the test environment so that I could run the following test
# I did not use AI to create any of the .cpp files.
# Compile once before running tests
@pytest.fixture(scope="session", autouse=True)
def build_program():
    # Find all cpp files in src/
    cpp_files = glob.glob("src/*.cpp")
    if not cpp_files:
        raise FileNotFoundError("No .cpp files found in src/")

    # Compile with include/ directory for headers
    subprocess.run(
        ["g++", "-std=c++14", "-O2", "-Iinclude", *cpp_files, "-o", "math_program"],
        check=True
    )
    yield
    if os.path.exists("math_program"):
        os.remove("math_program")
# End of AI Function

def run_program():
    result = subprocess.run(
    ["./math_program"], capture_output=True, text=True, check=True
    )
    return result.stdout.strip().splitlines()
def test_add_and_multiply_and_square():
    output = run_program()
    assert "a + b = 7" in output[0]
    assert "a * b = 12" in output[1]
    assert "square(a) = 9" in output[2]