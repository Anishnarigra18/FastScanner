import socket
import threading

target = input("Enter Target IP: ")

print(f"\nScanning {target}")
print("-" * 50)

open_ports = []

def scan_port(port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    except:
        pass


threads = []

for port in range(8000, 8101):

    thread = threading.Thread(
        target=scan_port,
        args=(port,)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)

print(f"Total Open Ports: {len(open_ports)}")

if open_ports:

    print("\nOpen Ports Found:")

    for port in open_ports:
        print(port)

else:

    print("\nNo Open Ports Found")
