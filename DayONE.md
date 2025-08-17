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


```bash
WLC#show wireless management trustpoint
Trustpoint Name  : WLC_WLC_TP
Certificate Info : Available
Certificate Type : SSC
Certificate Hash : 67e011a0b24a22f3872d900f116d548c6393a1b8
Private key Info : Available
FIPS suitability : Not Applicable

conf t
! Create RSA key
crypto key generate rsa label WLC-KEY modulus 2048
!
! Define trustpoint
crypto pki trustpoint WLC-TP
 enrollment selfsigned
 subject-name CN=wlc9800.mylab.local
 rsakeypair WLC-KEY
!
! Enroll self-signed certificate
crypto pki enroll WLC-TP
!
end
write memory

!bindIT:
conf t
ip http secure-trustpoint WLC-TP
wireless management trustpoint WLC-TP
end

!

```

```bash
enable
configure terminal
!
! ---------- [Time & DNS – helps avoid cert errors] ----------
clock timezone PHT 8 0
ntp server 0.pool.ntp.org
ntp server 1.pool.ntp.org
ip domain-name lab.local                 ! 🔧 your domain
!
! ---------- [Clean up old bindings – safe to run] ----------
no ip http secure-trustpoint
no wireless management trustpoint
!
! ---------- [Enable HTTPS] ----------
no ip http server
ip http secure-server
!
! ---------- [Generate RSA keypair] ----------
crypto key generate rsa label WLC-KEY modulus 2048
!
! ---------- [Create self-signed trustpoint] ----------
crypto pki trustpoint WLC-TP
 enrollment selfsigned
 subject-name CN=wlc9800.lab.local       ! 🔧 set FQDN
 fqdn wlc9800.lab.local                  ! 🔧 set FQDN
 rsakeypair WLC-KEY
 usage ssl-server
 revocation-check none
 exit
!
! ---------- [Enroll (issues the self-signed cert)] ----------
crypto pki enroll WLC-TP
!
! ---------- [Bind to wireless mgmt & HTTPS] ----------
wireless management trustpoint WLC-TP
ip http secure-trustpoint WLC-TP
end
!
write memory
!
! ---------- [Quick refresh of HTTPS] ----------
configure terminal
no ip http secure-server
ip http secure-server
end
!
! ---------- [Verification – run these show cmds] ----------
show clock
show crypto pki trustpoints
show crypto pki trustpoints WLC-TP status
show wireless management trustpoint
show ip http server secure status

```

```bash

In this Video I will show you how to be resolved Virtualized Intel VT-X/EPT is not supported on this platform:
1-systeminfo
2-bcdedit /set hypervisorlaunchtype off
3-Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
4-Disable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform
5-Local Group Policy Computer Configuration Administrative Templates System Device Guard Turn On Virtualization Security Disabled
6-Windows Security Device Security Core Isolation Core Isolation Details Memory Integrity Off
7-Turn Windows Features on or off
Uncheck Hyper-V
Uncheck Windows Hypervisor Platform

bcdedit /set hypervisorlaunchtype off
dism /online /disable-feature /featurename:Microsoft-Hyper-V-All
dism /online /disable-feature /featurename:VirtualMachinePlatform
dism /online /disable-feature /featurename:WindowsHypervisorPlatform

```

```
bash
enable
configure terminal
!
! 0) Prereqs: valid clock + HTTP(S) for enrollment
!    (If you have NTP, ensure time is already correct.)
clock calendar-valid
ip http server
ip http secure-server
end
!
! 1) Build a tiny local CA on the WLC (IOS PKI server)
!
configure terminal
crypto key generate rsa general-keys modulus 2048 label WLC_CA
crypto pki server WLC_CA
 issuer-name O=YOUR-ORG, CN=CA-vWLC
 grant auto
 hash sha256
 lifetime ca-certificate 3650
 lifetime certificate 1825
 database archive pkcs12 password 0 STRONG_CA_ARCHIVE_PASSWORD
 no shutdown
end
!
! 2) Create a device trustpoint + keys for the controller’s SSC
!
configure terminal
crypto key generate rsa exportable general-keys modulus 2048 label EWLC-TP1
crypto pki trustpoint EWLC-TP1
 rsakeypair EWLC-TP1
 subject-name O=YOUR-ORG, CN=DEVICE-vWLC
 revocation-check none
 hash sha256
 serial-number
 eku request server-auth client-auth
 password 0 STRONG_TP_ENROLL_PASSWORD
 ! Use the controller's management IP for the CA URL (uses the local CA you started above)
 enrollment url http://WLC-MGMT-IP:80
end
!
! 3) Fetch the CA cert and enroll the controller cert
!
crypto pki authenticate EWLC-TP1
! (type 'yes' to accept the CA fingerprint)
crypto pki enroll EWLC-TP1
! At prompts: "Include an IP address in the subject name? no"
!             "Request certificate from CA? yes"
end
!
! 4) Tag the SSC to the Wireless Management Trustpoint (WMI)
!
configure terminal
wireless management trustpoint EWLC-TP1
end
!
! 5) (9800-CL specific) Let MIC APs join a controller using SSC
!    a) (Optional but handy for labs/legacy APs) Allow MIC from Cisco Mfg CA and accept expired MICs
!
configure terminal
crypto pki certificate map MIC-MAP 1
 issuer-name co Cisco Manufacturing CA
exit
crypto pki trustpool policy
 match certificate MIC-MAP allow expired-certificate
exit
!
!    b) Authorize MIC APs against this SSC chain (vWLC requires this)
!
ap auth-list ap-cert-policy allow-mic-ap trustpoint EWLC-TP1
ap auth-list ap-cert-policy allow-mic-ap
!
!    c) Add allowed APs (repeat per AP; or bulk via GUI .csv)
!       Use EITHER MAC or serial number per line
ap auth-list ap-cert-policy mac-address AAAA.BBBB.CCCC policy-type mic
! or:
! ap auth-list ap-cert-policy serial-number FGLXXXXXXXX policy-type mic
end
!
! 6) (Optional) Stop the local CA now that enrollment is done
!
configure terminal
crypto pki server WLC_CA
 shutdown
end
!
! 7) Verify
!
show crypto pki server
show crypto pki trustpoint EWLC-TP1 status
show wireless management trustpoint
show ap auth-list ap-cert-policy


```
