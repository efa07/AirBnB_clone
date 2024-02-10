# AirBnB Clone - The Console

## Background Context
Welcome to the AirBnB clone project! The goal of this project is to build a full web application that replicates the functionality of AirBnB. This README provides an alternative explanation of the project and its first step: building a command interpreter to manage AirBnB objects.

## Project Overview
The AirBnB clone project consists of multiple tasks that are interconnected and build upon each other. The first task is to create a command interpreter that will be used to manage the objects within the AirBnB project. This command interpreter is similar to a shell, but it is specifically designed for the AirBnB use case.

## Command Interpreter
The command interpreter allows you to perform various operations on the AirBnB objects. The following functionalities are supported:

- Creating a new object, such as a user or a place.
- Retrieving an object from a file, a database, or any other storage mechanism.
- Performing operations on objects, such as counting or computing statistics.
- Updating attributes of an object.
- Destroying an object.

## Execution
The command interpreter can be used in interactive mode or non-interactive mode.

### Interactive Mode
In interactive mode, you can start the command interpreter by running the `./console.py` script. Once the command interpreter is running, you can enter commands and see the corresponding output. Here's an example:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode
In non-interactive mode, you can pass commands to the command interpreter through standard input or a file. The command interpreter will execute the commands and display the output. Here's an example using the `echo` command and a file:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Running Tests
To ensure the correctness of the command interpreter, it is recommended to run the provided unit tests. You can run the tests in non-interactive mode using the following command:

```
$ echo "python3 -m unittest discover tests" | bash
```
