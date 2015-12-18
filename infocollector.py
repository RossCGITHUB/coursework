import sqlite3
import datetime
import socket
import time
import psutil
import os
import urllib2
from uptime import uptime




while True:
 	
	#get uptime of device
	currentuptime = uptime()
  
	currenttime = datetime.datetime.now().time()
	
	#Get CPU temp
	def getCPUtemperature():
		res=os.popen('vcgencmd measure_temp').readline()
		return(res.replace("temp=","").replace("'C\n",""))
		
	temp = float(getCPUtemperature())

	storage = psutil.disk_usage('/').free

	#copy data into table
	conn = sqlite3.connect('monitordata.db')
	print "Opened database successfully"
	conn.execute("INSERT INTO CPU (TIME,CPUTEMP,STORAGE,UPTIME) VALUES ('"+str(currenttime)+"','"+str(temp)+"','"+str(storage)+"','"+str(currentuptime)+"')")
	conn.commit()
	print "Records created successfully";
  
	#close the connection
	conn.close()

	if temp > 50:
		os.system('python TempAlert.py')

	#Try google connection
	reqgoogle = urllib2.Request('http://www.google.com')
	googledown = "no"
	try: urllib2.urlopen(reqgoogle)	
	except urllib2.HTTPError as e:
		googlecode = e.code
		if googlecode == 200:
			googledown = "no"
		else:
			googledown = "yes"
			os.system('GGLAlert.py')

	except urllib2.URLError as e:
		print "url error found"

	#Try RGU connection
	reqrgu = urllib2.Request('http://www.rgu.ac.uk')
	rgudown = "no"
	try: urllib2.urlopen(reqrgu)
	except urllib2.HTTPError as e:
		rgucode = e.code
		if rgucode == 200:
			rgudown = "no"
		else:
			rgudown = "yes"
			os.system('RGUAlert.py')
	except urllib2.URLError as e:
		print "url error found"


	#Try cnmdtest connection
	reqcnmd = urllib2.Request('http://cnmdtest.ddns.net')
	cnmddown = "no"
	try: urllib2.urlopen(reqcnmd)
	except urllib2.HTTPError as e:
		cnmdcode = e.code
		if cnmdcode == 200:
			cnmddown = "no"
		else:
			cnmddown = "yes"
			os.system('CMNDAlert.py')
	except urllib2.URLError as e:
		print "url error found"

	#check the local DNS functionality
	ipname = "10.12.5.100"
	hostnam = socket.getfqdn(ipname)
	if hostnam == "ns3.rgu.ack.uk":
		DNSdown = "no"
	else:
		os.system('DNSAlert.py')
		DNSdown = "yes"

	conn = sqlite3.connect('webdata.db')
	print "Opened database successfully"
	conn.execute("INSERT INTO WEB (TIME,RGUDOWN,GOOGLEDOWN,CNMDDOWN,DNSDOWN) VALUES ('"+str(currenttime)+"','"+str(rgudown)+"','"+str(googledown)+"','"+str(cnmddown)+"','"+str(DNSdown)+"')")
	conn.commit()
	print "Records created successfully";
  
	#close the connection
	conn.close()


	#total packets sent 
	packetsent = psutil.net_io_counters('/')['wlan0'].packets_sent
	
	#total packets recieved
	packetrecv = psutil.net_io_counters('/')['wlan0'].packets_recv

	
	
	#total error packets
	packeterrin = psutil.net_io_counters('/')['wlan0'].errin
	packeterrout = psutil.net_io_counters('/')['wlan0'].errout
	totalerr = packeterrin + packeterrout

	#total dropped packets
	packetdropin = psutil.net_io_counters('/')['wlan0'].dropin
	packetdropout = psutil.net_io_counters('/')['wlan0'].dropout
	ttldropped = packetdropin + packetdropout
	
	conn = sqlite3.connect('netdata.db')
	print "Opened database successfully"
	conn.execute("INSERT INTO NET (TIME,PACKETSSENT,PACKETSRECIEVED,ERRORPACKETS,DROPPEDPACKETS) VALUES ('"+str(currenttime)+"','"+str(packetsent)+"','"+str(packetrecv)+"','"+str(totalerr)+"','"+str(ttldropped)+"')")
	conn.commit()
	print "Records created successfully";
  
	#close the connection
	conn.close()

	#Perform scan on port 22, 554, 25
	remoteServer = "localhost"
	remoteServerIP = socket.gethostbyname(remoteServer)

	
		
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result1 = sock.connect_ex((remoteServerIP, 22))
	if result1 == 0:
		result1 = "OPEN"
		conn = sqlite3.connect('port1data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT VALUES ('"+str(currenttime)+"','"+str(result1)+"')")
		conn.commit()
		conn.close()
	elif result1 == "111":
		result1 = "CLOSED"
		conn = sqlite3.connect('port1data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT VALUES ('"+str(currenttime)+"','"+str(result1)+"')")
		conn.commit()
		conn.close()	
		
			
	sock.close

	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result2 = sock.connect_ex((remoteServerIP, 25))
	if result2 == 0:
		result2 = "OPEN"
		conn = sqlite3.connect('port2data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT1 VALUES ('"+str(currenttime)+"','"+str(result2)+"')")
		conn.commit()
		conn.close()

  	else:
		result2 = "CLOSED"
		conn = sqlite3.connect('port2data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT1 VALUES ('"+str(currenttime)+"','"+str(result2)+"')")
		conn.commit()
		conn.close()
			
	sock.close

		
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result3 = sock.connect_ex((remoteServerIP, 554))
	if result3 == 0:
		result3 = OPEN
		conn = sqlite3.connect('port3data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT2 VALUES ('"+str(currenttime)+"','"+str(result3)+"')")
		conn.commit()
		conn.close()
	
	else:
		result3 = "CLOSED"
		conn = sqlite3.connect('port3data.db')
		print "Opened database successfully"
		conn.execute("INSERT INTO PORT2 VALUES ('"+str(currenttime)+"','"+str(result3)+"')")
		conn.commit()
		conn.close()
				
	sock.close

	
	
	

	
	


	
	#wait ten seconds
	time.sleep(15)



#total packets sent per minute
while True:
	totalpacksent = psutil.net_io_counters('/')['wlan0'].packets_sent - str(packetsent) 
	#copy data into table
	conn = sqlite3.connect('portdata.db')
	print "Opened database successfully"
	conn.execute("INSERT INTO PORT (TIME,PACKETPERMIN) VALUES ('"+str(currenttime)+"','"+str(totalpacksent)+"')")
	conn.commit()
	print "Records created successfully";
  
	#close the connection
	conn.close()
	time.sleep(60)
	


