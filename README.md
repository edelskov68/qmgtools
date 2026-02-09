# QMGTOOLS Auto-Update

IBM i Python program to automatically update QMGTOOLS from IBM.

## Description

This application provides automated update functionality for the QMGTOOLS library on IBM i systems. It executes the QMGTOOLS version comparison and update command (`QMGTOOLS/CMPVER`), monitors the execution status, and notifies the system operator upon successful completion.

## Features

- **Automated Updates**: Executes the QMGTOOLS/CMPVER command to check and apply updates automatically
- **Error Detection**: Monitors IBM i command output for failure indicators (CPF0000)
- **System Notifications**: Sends a message to the system operator message queue upon successful updates
- **Comprehensive Logging**: All operations are logged to `/QOpenSys/containers/qmgtools/main.log` with timestamps and severity levels
- **Exception Handling**: Gracefully handles errors with detailed logging

## Requirements

- Python 3.11 or higher
- IBM i system with Python support
- Access to QSH (POSIX shell) environment
- Proper authorities to execute QMGTOOLS/CMPVER and SNDMSG commands

## Usage

Execute the program as follows:

```bash
python main.py
```

The program will:
1. Attempt to run `QMGTOOLS/CMPVER NOPROMPT(Y)` on the IBM i system
2. Check the result for error indicators
3. Send a system message to the operator if successful
4. Log all activities to the main.log file

## Logging

All events are logged to `/QOpenSys/containers/qmgtools/main.log` with the following format:

```
YYYY-MM-DD HH:MM:SS LEVEL MESSAGE
```

Log levels include:
- **INFO**: Successful operations
- **ERROR**: Failed commands or exceptions

## Author

Brian Edelskov

## Created

09-02-2026
