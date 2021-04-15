import socket
import optparse


def scan_port(host, port):
    try:
        s = socket.socket()
        s.connect((host, int(port)))
        return True
    except:
        return False


def main():

    parser = optparse.OptionParser("Checks what ports are open on an IP")
    parser.add_option("--target", "-t", dest="target", type="string",
                      help="Target host, ip (x.x.x.x) or domain (example.com)")
    parser.add_option("--ports", "-p", dest="ports", type="string",
                      help="Target ports, separated by commas (22,80,443,9090)")
    options, args = parser.parse_args()

    ip = socket.gethostbyname(options.target)
    print(f"{socket.getfqdn(ip)} | {ip}")
    ports = options.ports.split(",")

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
