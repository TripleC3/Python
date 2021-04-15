import socket


def scan_port(host, port):
    try:
        s = socket.socket()
        s.connect((host, int(port)))
        return True
    except:
        return False


def main():
    ip = socket.gethostbyname(input("Introduce una IP o un dominio: "))
    print(f"{socket.getfqdn(ip)} | {ip}")
    ports = input("Introduce los puertos separados por comas: ").replace(" ", "").split(",")

    print("\n{:<20}{:<10}{:<5}".format("IP", "Port", "State"))
    print("-------------------------------------")
    for port in ports:
        if scan_port(ip, port):
            print("{:<20}{:<10}{:<5}".format(ip, port, "Open"))
        else:
            print("{:<20}{:<10}{:<5}".format(ip, port, "Closed"))


# Start
socket.setdefaulttimeout(1)

main()
