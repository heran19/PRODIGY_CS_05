# Network Packet Analyzer
 
A Python tool that captures and analyzes network packets in real time. This project was completed as part of the **Prodigy InfoTech Cybersecurity Internship** (Task-05).
 
> ⚠️ **Disclaimer:** This tool is intended strictly for educational purposes. Only use it on networks and devices you own or have explicit permission to monitor. Unauthorized packet sniffing on networks you do not control is illegal.
 
## About
 
This project demonstrates the fundamentals of network traffic analysis by capturing live packets and displaying key details such as source and destination IP addresses, protocol type, port numbers, and payload data. It provides hands-on insight into how data travels across a network at the packet level.
 
## Features
 
- Captures live network packets in real time
- Displays source and destination IP addresses
- Identifies the protocol used (TCP, UDP, ICMP)
- Shows source and destination port numbers for TCP/UDP traffic
- Displays a preview of the packet's payload data
- Limits capture to a fixed number of packets per run (configurable)
## How It Works
 
The program uses the `scapy` library to sniff packets directly from the network interface. For every captured packet, it inspects the IP layer to extract the source/destination addresses and protocol, then checks for TCP or UDP layers to extract port information. If the packet contains a raw payload, the first portion of that data is printed for analysis.
 
## Requirements
 
- Python 3.x
- scapy library
- **Npcap** (Windows) — required for packet capture at the network layer
- Administrator/root privileges to run
Install scapy with:
 
```bash
pip install scapy
```
 
If `pip` is not recognized, try:
 
```bash
py -m pip install scapy
```
 
### Windows-specific setup
 
Scapy requires Npcap to capture packets on Windows:
 
1. Download Npcap from [https://npcap.com/#download](https://npcap.com/#download)
2. During installation, check **"Install Npcap in WinPcap API-compatible Mode"**
3. Restart your computer if errors persist after installation
## Usage
 
1. Clone this repository or download the script.
```bash
git clone https://github.com/your-username/network-packet-analyzer.git
cd network-packet-analyzer
```
 
2. Run the script **as Administrator/root**:
```bash
python packet_analyzer.py
```
 
3. The tool will begin sniffing packets and print details for each one captured, for example:
```
Source IP: 192.168.1.10
Destination IP: 142.250.183.206
Protocol: TCP
Source Port: 52344
Destination Port: 443
Payload (first 50 bytes): b'\x17\x03\x03\x00\x4a...'
```
 
## File Structure
 
```
network-packet-analyzer/
│
├── packet_analyzer.py   # Main program
└── README.md            # Project documentation
```
 
## Learning Outcomes
 
- Understanding how network packets are structured (IP, TCP, UDP layers)
- Using the `scapy` library for live packet capture and analysis
- Differentiating between protocols and interpreting port-based traffic
- Practical exposure to network monitoring concepts and their security implications
- Reinforcing the importance of ethical and authorized use when working with network tools
## Acknowledgements
 
This project was completed as part of the Cybersecurity Internship offered by **Prodigy InfoTech**. Ethical use and proper authorization were emphasized throughout this task.
 
## License
 
This project is open source and available for educational purposes only.
 
