import sqlite3


conn = sqlite3.connect('monitordata.db')
print "Opened database successfully"

#create a tables called CPU, with the columns TIME and CPUUSE - both of these values are stored simply as text 
conn.execute('''CREATE TABLE CPU (TIME TEXT, CPUTEMP TEXT, STORAGE TEXT, UPTIME TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()

conn = sqlite3.connect('netdata.db')
print "Opened database successfully"

#create a tables called NET, with the columns TIME ,PACKETSSENT,PACKRECV,ERRPACKS,DROPPACKS - these values are stored simply as text 
conn.execute('''CREATE TABLE NET (TIME TEXT, PACKETSSENT TEXT, PACKETSRECIEVED TEXT, ERRORPACKETS TEXT, DROPPEDPACKETS TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()

conn = sqlite3.connect('packetmin.db')
print "Opened database successfully"

#create a tables called PACK, with the columns TIME ,PACKETPERMIN - these values are stored simply as text 
conn.execute('''CREATE TABLE PACK (TIME TEXT, PACKETPERMIN TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()

conn = sqlite3.connect('port1data.db')
print "Opened database successfully"

#create a tables called PORT, with the columns TIME ,portsopen - these values are stored simply as text 
conn.execute('''CREATE TABLE PORT (TIME TEXT, PORT22 TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()


conn = sqlite3.connect('port2data.db')
print "Opened database successfully"

#create a tables called PORT, with the columns TIME ,portsopen - these values are stored simply as text 
conn.execute('''CREATE TABLE PORT1 (TIME TEXT, PORT25 TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()

conn = sqlite3.connect('port3data.db')
print "Opened database successfully"

#create a tables called PORT, with the columns TIME ,portsopen - these values are stored simply as text 
conn.execute('''CREATE TABLE PORT2 (TIME TEXT, PORT554 TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()
conn = sqlite3.connect('webdata.db')
print "Opened database successfully"

#create a tables called WEB, with the columns TIME ,RGUDOWN, GOOGLEDOWN, CNMDDOWN, DNSDOWN  - these values are stored simply as text 
conn.execute('''CREATE TABLE WEB (TIME TEXT, RGUDOWN TEXT, GOOGLEDOWN TEXT, CNMDDOWN TEXT, DNSDOWN TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()