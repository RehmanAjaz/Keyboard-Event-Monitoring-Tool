Keyboard Event Monitoring Tool (Internship Project)
Overview

This project implements a structured keyboard event monitoring tool using Python and the pynput library. The application captures real-time keyboard input events, formats special keys, attaches timestamps, performs basic log rotation, and generates session summaries.

The purpose of this project is to study how keyboard event listeners operate at the operating system level and to understand the behavioral mechanisms commonly associated with keylogging software in cybersecurity contexts.

This tool was developed strictly for educational and defensive security research in a controlled lab environment.

Features

Real-time keyboard event capture

Timestamped keystroke logging

Special key formatting (Enter, Space, Ctrl, etc.)

Log file management with size-based rotation

Session summary statistics

Controlled execution (manual start/stop)

Local file storage only (no transmission)

Technologies Used

Python 3

pynput

Kali Linux (Lab Environment)

File system logging

System Architecture

Keyboard Input
↓
Event Listener (pynput)
↓
Key Formatting Logic
↓
Timestamp Attachment
↓
Log File Writer
↓
Session Summary Output

The tool passively records keyboard events and does not conceal itself, escalate privileges, or transmit data externally.
