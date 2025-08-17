Install-WindowsFeature  -name dns  -includeManagementTools
Add-DnsServerPrimaryZone -Name "ngcpM.ph" -ZoneFile "ngcpM.ph.dns"
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name ns  -ipv4address 10.m.1.10
add-DnsServerResourceRecord -zonename ngcp12.com -A -name "." -ipv4address 10.12.1.10
#
add-DnsServerResourceRecord -zonename ngcpM.ph -Cname -name www -hostname ns.ngcpM.ph
add-DnsServerResourceRecord -zonename ngcpM.ph -Cname -name imap -hostname ns.ngcpM.ph
add-DnsServerResourceRecord -zonename ngcpM.ph -Cname -name pop -hostname ns.ngcpM.ph
add-DnsServerResourceRecord -zonename ngcpM.ph -Cname -name smtp -hostname ns.ngcpM.ph
###FOR CISCO DEVICES DNS RECORDS;
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name cb  -ipv4address 10.m.1.4
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name ct  -ipv4address 10.m.1.2
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name cm  -ipv4address 10.m.100.8
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name ed  -ipv4address 10.m.m.1
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name p1  -ipv4address 10.m.100.101
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name p2  -ipv4address 10.m.100.102
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name c1  -ipv4address 10.m.50.6
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name c2  -ipv4address 10.m.50.8
add-DnsServerResourceRecord -zonename ngcpM.ph -A -name ap  -ipv4address 10.m.10.3
#
﻿#creating all important zones:
#
Add-DnsServerResourceRecordMX -Preference 10  -Name "." -MailExchange "ns.ngcp12.com" -ZoneName "ngcp12.com"

