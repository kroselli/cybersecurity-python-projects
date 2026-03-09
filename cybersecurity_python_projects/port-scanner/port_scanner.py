
import socket
import argparse

def scan_target(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                print(f"[OPEN] Port {port} ({service})")
                open_ports.append(port)

            s.close()

        except KeyboardInterrupt:
            print("\nScan interrupted.")
            exit()

    print("\nScan complete.")
    print(f"Open ports found: {len(open_ports)}")

def main():
    parser = argparse.ArgumentParser(description="Python Network Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")

    args = parser.parse_args()

    scan_target(args.target, args.start, args.end)

if __name__ == "__main__":
    main()
