# Pronto Coding Challenge

## Table of Contents

- [Description](#Description)
- [Examples](#examples)
- [Files](#files)
- [Installation](#installation)
- [CLI Arguments](#cli_arguments)

## Description

This is a simple program that traverses a robot from a starting point based on a series of commands. After the traversal the program outputs the robot's distance from it's starting point. This distance is the minimum amount of units the robot will need to traverse in order to get back to it's starting point. The robot can only turn 90 degrees at a time and can go in north, south, east, west directions.

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
Current direction -  N
Current position  -  (-2, -2)
Distance to start -  4
Time taken -  0.00022101402282714844 seconds
```

## Files
- [robot.py](https://github.com/ParthTrehan/Pronto-Coding-Challenge/blob/master/robot.py "robot.py") - This is the main python script that implements the CLI application for robot traversal and distance calculation.

## Installation

- All the `code` is available in this repo to get started

### Clone

- Clone this repo to your local machine using `https://github.com/ParthTrehan/Pronto-Coding-Challenge.git`

### Setup

> You would require Python 3 to run "robot.py". There are no external libraries required to run this project. 
```bash
#code away!
python robot.py --commands "F1,R1,B2,L1,B3"
```

## CLI Arguments

 -h, --help            show this help message and exit
  --verbose, -v         display more information about the robot traversal
  --commands COMMANDS, -c COMMANDS
                        a string of comma-separated commands eg:
                        "F1,R1,B2,L1,B3"

| Argument                  | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -h, --help       	        |	-           | Shows the CLI help message and exits
| -v  --verbose             | False         | Displays more information about the robot traversal
| -c -–commands 	        | -	            | This is a required argument that takes a string of comma-separated commands. For example: "F1,R1,B2,L1,B3"