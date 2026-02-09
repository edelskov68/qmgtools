"""
QMGTOOLS Auto-Update Program

This module provides automated update functionality for IBM's QMGTOOLS library
on IBM i systems. It executes the QMGTOOLS/CMPVER command and notifies the
system operator upon successful completion.

Filename: main.py
Logfile: /QOpenSys/containers/qmgtools/main.log
Author: Brian Edelskov
Created: 09-02-2026
Description: QMGTOOLS autoupdate program.
"""

import logging
import subprocess

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="/QOpenSys/containers/qmgtools/main.log",
)


def update_qmgtools():
    """
    Execute the QMGTOOLS version comparison and update command.
    
    Runs the IBM i QMGTOOLS/CMPVER command through the qsh shell to check and
    update QMGTOOLS. Logs the result and sends a system message upon success.
    
    Raises:
        Exception: Logs any exception that occurs during command execution.
    """
    try:
        ibmicmd = "QMGTOOLS/CMPVER NOPROMPT(Y)"
        command = f'system -i "{ibmicmd}"'
        result = subprocess.run(
            ["qsh", "-c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = result.stdout.strip()
        error_output = result.stderr.strip()
        failure_indicators = ["CPF0000"]
        if any(indicator in output for indicator in failure_indicators) or any(
            indicator in error_output for indicator in failure_indicators
        ):
            logging.error("Update of QMGTOOLS ended abnormally!")
        else:
            logging.info("Update of QMGTOOLS ended successfully.")
            send_message_info()
    except Exception as e:
        logging.error(f"Error: {e}")


def send_message_info():
    """
    Send a system operator message confirming QMGTOOLS update completion.
    
    Sends an IBM i SNDMSG command to notify the system operator (*SYSOPR message
    queue) that QMGTOOLS has been successfully updated. Logs success or failure
    of the message transmission.
    
    Raises:
        Exception: Logs any exception that occurs during message transmission.
    """
    try:
        ibmicmd = "SNDMSG MSG('QMGTOOLS has been updated') TOMSGQ(*SYSOPR)"
        command = f'system -i "{ibmicmd}"'
        result = subprocess.run(
            ["qsh", "-c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = result.stdout.strip()
        error_output = result.stderr.strip()

        failure_indicators = ["CPF2469"]
        if any(indicator in output for indicator in failure_indicators) or any(
            indicator in error_output for indicator in failure_indicators
        ):
            logging.error("Message ended abnormally!")
        else:
            logging.info("Message sent successfully.")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    update_qmgtools()

