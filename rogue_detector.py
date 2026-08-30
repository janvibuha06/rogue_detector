from scapy.all import ARP, Ether, srp, conf
import json

conf.iface = "Wi-Fi"

def scan_network(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})

    return devices


def save_baseline(devices, filename="baseline.json"):
    with open(filename, "w") as f:
        json.dump(devices, f, indent=4)
    print(f"Baseline saved with {len(devices)} devices.")


target_ip = "192.168.1.0/24"
found_devices = scan_network(target_ip)

save_baseline(found_devices)