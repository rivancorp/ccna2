# 200-301 CCNA v1.1 Exam Topics

Now Available
Exam Description
CCNA Exam v1.1 (CCNA 200-301) is a 120-minute exam associated with the CCNA certification. This exam tests a candidate's knowledge and skills related to network fundamentals, network access, IP connectivity, IP services, security fundamentals, and automation and programmability. The course, Implementing and Administering Cisco Solutions (CCNA), helps candidates prepare for this exam.

```bash
config t
hostname FirewallVPN1
enable secret pass
no logging console
no ip domain-lookup
line cons 0
 password pass
 login
 exec-timeout 0 0
line vty 0 14
 password pass
 login
 exec-timeout 0 0
 transport input all
int gi 0/0
 no shut
 ip add 172.23.0.1 255.255.0.0
int gi 0/1
 no shut
 ip add 192.168.69.150 255.255.255.0
```
![image](https://github.com/user-attachments/assets/4eb717a5-0fb0-4d04-babf-d8e0dcfa0b1f)

<details>
<summary>Click to expand!</summary>
1.1 Explain the role and function of network components
1.1.a Routers
1.1.b Layer 2 and Layer 3 switches
1.1.c Next-generation firewalls and IPS
1.1.d Access points
1.1.e Controllers (Cisco DNA Center and WLC)
1.1.f Endpoints
1.1.g Servers
1.1.h PoE

1.2 Describe characteristics of network topology architectures
1.2.a Two-tier
1.2.b Three-tier
1.2.c Spine-leaf
1.2.d WAN
1.2.e Small office/home office (SOHO)
1.2.f On-premise and cloud

1.3 Compare physical interface and cabling types
1.3.a Single-mode fiber, multimode fiber, copper
1.3.b Connections (Ethernet shared media and point-to-point)

1.4 Identify interface and cable issues (collisions, errors, mismatch duplex, and/or speed)

1.5 Compare TCP to UDP

1.6 Configure and verify IPv4 addressing and subnetting

1.7 Describe private IPv4 addressing

1.8 Configure and verify IPv6 addressing and prefix

1.9 Describe IPv6 address types
1.9.a Unicast (global, unique local, and link local)
1.9.b Anycast
1.9.c Multicast
1.9.d Modified EUI 64

1.10 Verify IP parameters for Client OS (Windows, Mac OS, Linux)

1.11 Describe wireless principles
1.11.a Nonoverlapping Wi-Fi channels
1.11.b SSID
1.11.c RF
1.11.d Encryption

1.12 Explain virtualization fundamentals (server virtualization, containers, and VRFs)

1.13 Describe switching concepts
1.13.a MAC learning and aging
1.13.b Frame switching
1.13.c Frame flooding
1.13.d MAC address table
</details>
