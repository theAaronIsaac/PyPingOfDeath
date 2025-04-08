# Multi-Threaded Ping Utility
USE NICELY PLEASE :D 
A simple yet powerful Python utility for performing multi-threaded ping operations with customizable packet sizes.

## Overview

This script allows you to ping a target IP address or hostname with multiple concurrent threads and specify the packet size for each ping request. It's useful for network testing, troubleshooting, or stress testing network connections.

## Features

- Multi-threaded ping operations
- Customizable packet size (up to 65500 bytes)
- Real-time output from all ping threads
- Simple command-line interface

## Requirements

- Python 3.x
- Operating system with `ping` command available (Windows, Linux, macOS)

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. Follow the prompts:
   - Enter the target IP address or hostname
   - Enter the number of threads (default: 1)
   - Enter the packet size in bytes (default/max: 65500)

3. To stop the script, press `Ctrl+C`

## Function Details

### `f(x, i, size)`
The worker function that runs in each thread.

Parameters:
- `x`: Target IP address or hostname
- `i`: Thread identifier (number)
- `size`: Packet size in bytes

This function:
- Creates a subprocess to run the ping command
- Adds the subprocess to a global list for later cleanup
- Captures and prints the output with thread identifier
- Handles exceptions that may occur during execution

### `m()`
The main function that:
- Collects user input for target, thread count, and packet size
- Validates user input and applies default values if needed
- Creates and starts the requested number of threads
- Waits for user interruption (Ctrl+C)
- Cleans up subprocesses on exit

## Notes

- The script uses the `-t` flag for continuous ping operation
- The maximum packet size is limited to 65500 bytes
- Each thread's output is prefixed with its thread number (`[T1]`, `[T2]`, etc.)
- All ping processes are killed when the script is stopped

## Caution

This tool should be used responsibly and ethically. Misuse may:
- Violate network policies
- Trigger security alerts
- Potentially cause network congestion
- Be considered a network attack if used against systems without permission
