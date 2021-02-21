import subprocess
import sys
import json

tests = list()
script_name = "robot.py"
tests_file = "test_cases.json"


def capture(command):
    '''
    This function process and runs the CLI command and captures
    the result from it.
    '''
    result = subprocess.run(command,
                            capture_output=True,
                            text=True)
    return result.stdout, result.stderr, result.returncode


def test_cli():
    '''
    This is the testing function that is used by pytest library and 
    this function executes the test cases from the test_cases.json 
    file.
    '''
    command = ["python", script_name, "-c"]
    test_count = 0
    with open(tests_file) as json_file:
        test_cases = json.load(json_file)
        for test_case in test_cases['testCases']:
            test_count += 1
            out, err, exitcode = capture(command + [test_case['command']])
            assert exitcode == (test_case['returnCode'])
            assert out == test_case['output']
            assert err == test_case['error']
            sys.stdout.write(f"\n \033[32m test case {test_count} PASSED")