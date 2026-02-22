_RSTvX = "1"
_RSTvX_Subnet = "2"
_RSTvX_Hosts__Day_5 = "3"
_RSTvX_Mini = "4"
_RSTvX_MultiSite = "5"
_MPLSCloud = "6"
_WAN = "7"
_3Tier = "8"
_NetAuto = "9"
_InterNetwork = "10"

rst_ip = crt.Dialog.Prompt("What is your RST IPv4 Address? ")
lab = crt.Dialog.Prompt("""
What Lab will you be using? (Input the number of the corresponding lab.)

RSTvX = 1
RST Subnet = 2
RST Hosts (Day 5) = 3
RST Mini = 4
RST Multisite = 5
MPLS = 6
WAN = 7
3Tier = 8
NetAuto = 9
InterNetwork = 10

Manually enter a series of port numbers = 0 

""")


if lab == "1":
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2003",
        "/TELNET " + rst_ip + " 2004",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006",
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2009",
        "/TELNET " + rst_ip + " 2010",
        "/TELNET " + rst_ip + " 2011",
        "/TELNET " + rst_ip + " 2012",
        "/TELNET " + rst_ip + " 2013",
        "/TELNET " + rst_ip + " 2014",
        "/TELNET " + rst_ip + " 2015",
        "/TELNET " + rst_ip + " 2016"
    ]
elif lab == "2":
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2003",
        "/TELNET " + rst_ip + " 2004",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006",
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2009"
    ]
elif lab == "3":
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006",
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2009",
        "/TELNET " + rst_ip + " 2010",
        "/TELNET " + rst_ip + " 2011",
        "/TELNET " + rst_ip + " 2012",
        "/TELNET " + rst_ip + " 2013",
        "/TELNET " + rst_ip + " 2014",
        "/TELNET " + rst_ip + " 2015",
        "/TELNET " + rst_ip + " 2016"
    ]
elif lab == "4":
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006",
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2009",
        "/TELNET " + rst_ip + " 2010",
        "/TELNET " + rst_ip + " 2013"
    ]
elif lab == "5":
    connections = [
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2010",
        "/TELNET " + rst_ip + " 2012",
        "/TELNET " + rst_ip + " 2013",
        "/TELNET " + rst_ip + " 2015",
        "/TELNET " + rst_ip + " 2016"
    ]
elif lab == "6":
    connections = [
        "/TELNET " + rst_ip + " 2017",
        "/TELNET " + rst_ip + " 2018",
        "/TELNET " + rst_ip + " 2019",
        "/TELNET " + rst_ip + " 2020",
        "/TELNET " + rst_ip + " 2021",
        "/TELNET " + rst_ip + " 2022",
        "/TELNET " + rst_ip + " 2023",
        "/TELNET " + rst_ip + " 2024",
        "/TELNET " + rst_ip + " 2025",
        "/TELNET " + rst_ip + " 2026",
        "/TELNET " + rst_ip + " 2027",
        "/TELNET " + rst_ip + " 2028"
    ]
elif lab == "7":
    connections = [
        "/TELNET " + rst_ip + " 2135",
        "/TELNET " + rst_ip + " 2136",
        "/TELNET " + rst_ip + " 2137",
        "/TELNET " + rst_ip + " 2138",
        "/TELNET " + rst_ip + " 2139",
        "/TELNET " + rst_ip + " 2140",
        "/TELNET " + rst_ip + " 2141",
        "/TELNET " + rst_ip + " 2142",
        "/TELNET " + rst_ip + " 2143",
        "/TELNET " + rst_ip + " 2144",
        "/TELNET " + rst_ip + " 2145",
        "/TELNET " + rst_ip + " 2146",
        "/TELNET " + rst_ip + " 2147",
        "/TELNET " + rst_ip + " 2148",
        "/TELNET " + rst_ip + " 2149",
        "/TELNET " + rst_ip + " 2150",
        "/TELNET " + rst_ip + " 2151",
        "/TELNET " + rst_ip + " 2152",
        "/TELNET " + rst_ip + " 2153",
        "/TELNET " + rst_ip + " 2154"
    ]
elif lab == "8":
    connections = [
        "/TELNET " + rst_ip + " 2204",
        "/TELNET " + rst_ip + " 2205",
        "/TELNET " + rst_ip + " 2206",
        "/TELNET " + rst_ip + " 2207",
        "/TELNET " + rst_ip + " 2208",
        "/TELNET " + rst_ip + " 2209",
        "/TELNET " + rst_ip + " 2210",
        "/TELNET " + rst_ip + " 2211",
        "/TELNET " + rst_ip + " 2212",
        "/TELNET " + rst_ip + " 2213",
        "/TELNET " + rst_ip + " 2214",
        "/TELNET " + rst_ip + " 2215",
        "/TELNET " + rst_ip + " 2216",
        "/TELNET " + rst_ip + " 2217",
        "/TELNET " + rst_ip + " 2339"
    ]
elif lab == "9":
    connections = [
        "/TELNET " + rst_ip + " 2262",
        "/TELNET " + rst_ip + " 2263",
        "/TELNET " + rst_ip + " 2264",
        "/TELNET " + rst_ip + " 2265",
        "/TELNET " + rst_ip + " 2266",
        "/TELNET " + rst_ip + " 2267",
        "/TELNET " + rst_ip + " 2268",
        "/TELNET " + rst_ip + " 2269",
        "/TELNET " + rst_ip + " 2270",
        "/TELNET " + rst_ip + " 2271",
        "/TELNET " + rst_ip + " 2272"
    ]
elif lab == "10":
    connections = [
        "/TELNET " + rst_ip + " 2801",
        "/TELNET " + rst_ip + " 2802",
        "/TELNET " + rst_ip + " 2803",
        "/TELNET " + rst_ip + " 2804",
        "/TELNET " + rst_ip + " 2805",
        "/TELNET " + rst_ip + " 2806",
        "/TELNET " + rst_ip + " 2807",
        "/TELNET " + rst_ip + " 2808",
        "/TELNET " + rst_ip + " 2809",
        "/TELNET " + rst_ip + " 2810",
        "/TELNET " + rst_ip + " 2811",
        "/TELNET " + rst_ip + " 2812",
        "/TELNET " + rst_ip + " 2813",
        "/TELNET " + rst_ip + " 2814",
        "/TELNET " + rst_ip + " 2815",
        "/TELNET " + rst_ip + " 2816",
        "/TELNET " + rst_ip + " 2817",
        "/TELNET " + rst_ip + " 2818",
        "/TELNET " + rst_ip + " 2819",
        "/TELNET " + rst_ip + " 2820",
        "/TELNET " + rst_ip + " 2821",
        "/TELNET " + rst_ip + " 2822",
        "/TELNET " + rst_ip + " 2823",
        "/TELNET " + rst_ip + " 2824",
        "/TELNET " + rst_ip + " 2825",
        "/TELNET " + rst_ip + " 2826",
        "/TELNET " + rst_ip + " 2827",
        "/TELNET " + rst_ip + " 2828",
        "/TELNET " + rst_ip + " 2829",
        "/TELNET " + rst_ip + " 2830",
        "/TELNET " + rst_ip + " 2831",
        "/TELNET " + rst_ip + " 2832",
        "/TELNET " + rst_ip + " 2833",
        "/TELNET " + rst_ip + " 2834"
    ]
elif lab == "0":
    port_list = []
    
    specify_ports = crt.Dialog.Prompt("""
    Specify port numbers (separated by spaces):
    ex. 
    
    2001 2002 2003 2004

    """)
    
    port_list = specify_ports.split()
    connections = []
    
    for port in port_list:
        session = ["/TELNET " + rst_ip + " " + port]
        connections.append(session[0])
        
crt.Screen.Synchronous = True

for connection in connections:
	crt.Session.ConnectInTab(connection)

crt.Screen.Synchronous = False
