log_file = "server_log.txt"
failed_attempts = 0

print("\nAnalyzing log file...\n")

with open(log_file, "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            failed_attempts += 1
            print("Suspicious activity detected:", line.strip())

print(f"\nTotal suspicious login attempts: {failed_attempts}")