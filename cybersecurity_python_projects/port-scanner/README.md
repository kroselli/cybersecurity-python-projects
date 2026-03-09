
# Advanced Python Port Scanner

This project is an improved version of a basic port scanner that demonstrates more realistic
cybersecurity tooling concepts.

## Features

- Scans a configurable range of TCP ports
- Uses command line arguments
- Attempts service identification for open ports
- Handles interrupts gracefully
- Displays scan results clearly

## Requirements

Python 3.x (no external libraries required)

## Usage

Run the scanner from the command line:

python3 advanced_port_scanner.py 127.0.0.1

Scan a custom port range:

python3 advanced_port_scanner.py 127.0.0.1 --start 20 --end 200

## Example Output

Scanning 127.0.0.1 from port 1 to 1024

[OPEN] Port 22 (ssh)
[OPEN] Port 80 (http)

Scan complete.
Open ports found: 2

## Concepts Demonstrated

- TCP socket scanning
- Network reconnaissance
- Service identification
- Command line interface design
- Basic cybersecurity tool development

## Future Improvements

Possible upgrades include:

- Multithreading for faster scans
- Banner grabbing
- Exporting scan results to a file
- UDP scanning
