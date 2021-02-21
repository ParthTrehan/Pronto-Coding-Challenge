# Pronto Coding Challenge

## Table of Contents

- [Description](#Description)
- [CLI Examples](#examples)
- [Files](#files)
- [Installation](#installation)
- [CLI Arguments](#cli_arguments)
- [Build process](#build)

## Description

This is a simple CLI application that traverses a robot from a starting point based on a series of commands. After the traversal the program outputs the robot's distance from it's starting point. This distance is the minimum amount of units the robot will need to traverse in order to get back to it's starting point. The robot can only turn 90 degrees at a time and can go in north, south, east, west directions.

The robot that can receive commands in order to move.  These commands will tell the robot to go forwards or backwards, and turn left or right.  These commands will be  in the format \<command>\<number>.  For example 'L1' means 'turn left by 90 degrees once'.  'B2' would mean go backwards 2 units.

### Available commands:
* `F` - move forward 1 unit
* `B` - move backward 1 unit
* `R` - turn right 90 degrees
* `L` - turn left 90 degrees

## Examples

```bash
# CLI command
python robot.py --commands "F1,R1,B2,L1,B3"

# Output would be
4
```
```bash
# CLI command with verbosity turned on:
python robot.py --verbose --commands "F1,R1,B2,L1,B3"

# Output would be
##################### Verbose ######################
Current direction -  N
Current position  -  (-2, -2)
Distance to start -  4
Time taken -  0.00020885467529296875 seconds
#####################################################
4
```

## Files
- [robot.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/robot.py "robot.py") - This is the main python script that implements the CLI application for robot traversal and distance calculation.
- [test.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/test.py "test.py") - This is the testing python script that can be used to test the CLI application using the test cases provided in [test_cases.json](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/test_cases.json "test_cases.json"). Some samples are already provided in the file.

## Installation

All the `code` is available in this repo to get started

### Clone

- Clone this repo to your local machine using the following command
```bash
git clone https://github.com/ParthTrehan/Pronto-Coding-Challenge.git
```

### Setup

> You would require Python 3 to run [robot.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/robot.py "robot.py") and Pytest 6.2.2 for running the [test.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/test.py "test.py").
```bash
#code away!
python robot.py --commands "F1,R1,B2,L1,B3"
```

## <a id="cli_arguments"></a>CLI Arguments
The following CLI arguments to run the python script as shown in the above example.

| Argument                  | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -h, --help       	        |	-           | Shows the CLI help message and exits
| -v  --verbose             | False         | Displays more information about the robot traversal
| -c --commands 	        | -	            | This is a required argument that 					takes a string of comma-separated commands. For example: "F1,R1,B2,L1,B3"

## <a id="build"></a>Build Process

### Extensibility and design decisions
This project is build keeping simplicity and extensibility in mind. A robot class has been created to cover all the robot related tasks such as movment, rotation, distance calculation of the robot. Even though this is simple application, adding functionality is very simple in this application. For example:

 1. **Robot Intialization**: To initialize the robot starting position and direction, it is just required to set values when declaring the robot object. This class can be extended to include more robot's features such as actuators and sensors.
 2. **Path finiding algorithm**: calculate_distance() function calculates the robot's distance the start position and this is implemented by calculating manhattan distance. However, this function can also be extended to add more complex path finding algorithms, such as dijkstra and A*, which can include path costs.

For specific function description and logic please refer to [robot.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/robot.py "robot.py").

### Assumptions
There are some assumptions in building the project:

 1. The robot can only move in four directions (North, East, South, West).
 2. The robot can only move 1-9 units in a given command. 
 3. Robot's direction is not considered during calculation of the robot's distance from the starting point. For example if the robot is given a command "F3,R1,F2", the robot will be facing East after the robot has traversed. However, to go back to the start location, the robot has to turn to south direction to go back to the start location. This phenomenon is not incorporated in the distance calulation.

### Testing
For testing the CLI application a testing python script has been developed using [Pytest (6.2.2)](https://pytest.org/) package. To run this script you would require pytest and you can execute the test using the following command.

```bash
#testing!
pytest test.py -s

# Output would be like
================================== test session starts ==================================
platform darwin -- Python 3.7.6, pytest-6.2.2, py-1.9.0, pluggy-0.13.1
rootdir: /Pronto Coding Challenge
collected 1 item                                                                        

test.py 
  test case 1 PASSED
  test case 2 PASSED
  test case 3 PASSED
  test case 4 PASSED
  test case 5 PASSED.

=================================== 1 passed in 0.23s ===================================
```
To add more test cases, it can be done easily by just appending the [test_cases.json](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/test_cases.json "test_cases.json") file with the following json. You can add the commands string and the output that is expected and just execute [test.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/test.py "test.py") file.
```json
{
	"id": "1",
	"command": "F1,L1,F3,R1,B4",
	"output": "6",
	"error": "",
	"returnCode": 1
}
```
> To add a wrong command test cases, just change the command and set the returnCode to 0 as given below.

```json
{
	"id": "2",
	"command": "F1,R1,B2,L1,P3",
	"output": "",
	"error": "error: Invalid input commands",
	"returnCode": 0
}
```