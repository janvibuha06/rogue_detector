# 🛡️ Rogue Device Detector

A lightweight Python CLI tool that monitors a local network (LAN) and detects unauthorized/unknown devices by comparing live network scans against a saved baseline of trusted devices.

## 🎯 What It Does

This tool uses ARP (Address Resolution Protocol) requests to discover all devices currently connected to a network. It then compares this live scan against a previously saved "baseline" of known devices — flagging any new/unrecognized device as a potential security concern.

This simulates a basic version of Network Access Control (NAC) — a concept used in enterprise cybersecurity to prevent unauthorized devices from joining a network undetected.

## ⚙️ Features

- **Network Scanning** — Discovers all active devices on a LAN using ARP requests
- **Baseline Management** — Save a snapshot of trusted/known devices
- **Rogue Device Detection** — Compares live scans against the baseline and alerts on new devices
- **Interactive CLI Menu** — Simple menu-driven interface for easy use
- **JSON-based Storage** — Baseline data stored in a readable JSON file

## 🛠️ Built With

- Python 3
- [Scapy](https://scapy.net/) — for crafting and sending ARP packets
- JSON — for baseline data storage

## 📋 How It Works

1. Tool scans the network using ARP requests and collects IP/MAC addresses of active devices
2. On first run, it saves this list as a "baseline" (trusted devices)
3. On subsequent runs, it compares the new scan against the baseline
4. If a device appears that wasn't in the baseline, it raises an alert with the device's IP and MAC address

## 🚀 Usage

```bash
pip install scapy
python rogue_detector.py
```

Menu options:
1. **Scan Now** — Run a scan and compare against the baseline
2. **View Saved Baseline** — See the list of currently trusted devices
3. **Reset Baseline** — Save the current network state as the new baseline
4. **Exit**

## ⚠️ Note

- Requires Npcap (Windows) for raw packet capture — [download here](https://npcap.com)
- Must be run with administrator/root privileges
- Update the `TARGET_IP` variable in the script to match your network's IP range

## 🔮 Future Improvements

- Continuous background monitoring with scheduled scans
- Email/desktop notifications for alerts
- Web-based dashboard for visualization
- Logging with timestamps for historical tracking

## 📚 What I Learned

Building this project helped me understand ARP protocol mechanics, network scanning techniques, and how basic intrusion detection concepts work in real-world cybersecurity tools.
