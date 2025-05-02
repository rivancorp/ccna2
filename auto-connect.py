
rst_ip = crt.Dialog.Prompt("What is your RST IPv4 Address? ")

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
	"/TELNET " + rst_ip + " 2016",
]

crt.Screen.Synchronous = True

for connection in connections:
	crt.Session.ConnectInTab(connection)

crt.Screen.Synchronous = False