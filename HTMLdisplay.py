import socket
import HTML
import sqlite3


#setup server
HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
#run forever
while True:
    
    #standard server code
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    http_status = "HTTP/1.1 200 OK \n"
    http_type = "Content-Type: text/html\n"
   
	
    	#create a new table for port1data.db
    port1table = HTML.Table(header_row=['TIME', 'PORT22'])
    
    #open database
    conn = sqlite3.connect('port1data.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, PORT22 FROM PORT")limit 5
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      port1table.rows.append([row[0], row[1]])
    
     	#create a new table for port2data.db
    port2table = HTML.Table(header_row=['TIME', 'PORT25'])
    
    #open database
    conn = sqlite3.connect('port2data.db')
    #get data from database
    cursor1 = conn.execute("SELECT TIME, PORT25 FROM PORT1")limit 5
    #for every row in our database
    for row in cursor1:
      #add a new row to our table
     port2table.rows.append([row[0], row[1]])
    
     	#create a new table for port3data.db
    port3table = HTML.Table(header_row=['TIME', 'PORT554'])
    
    #open database
    conn = sqlite3.connect('port3data.db')
    #get data from database
    cursor2 = conn.execute("SELECT TIME, PORT554 FROM PORT2")limit 5
    #for every row in our database
    for row in cursor2:
      #add a new row to our table
      port3table.rows.append([row[0], row[1]])
    

 #create a new table for netdata.db
    nettable = HTML.Table(header_row=['TIME', 'PACKETSSENT', 'PACKETRECIEVED', 'ERRORPACKETS', 'DROPPEDPACKETS'])
    

    #open database
    conn = sqlite3.connect('netdata.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, PACKETSSENT, PACKETSRECIEVED, ERRORPACKETS, DROPPEDPACKETS FROM NET")limit 5
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      nettable.rows.append([row[0], row[1], row[2], row[3], row[4]])
    
    #close the connection
    conn.close() 
    
	#create a new table for webdata.db
    webtable = HTML.Table(header_row=['TIME', 'RGUDOWN', 'GOOGLEDOWN', 'CNMDDOWN', 'DNSDOWN'])
    
    #open database
    conn = sqlite3.connect('webdata.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, RGUDOWN, GOOGLEDOWN, CNMDDOWN, DNSDOWN FROM WEB")limit 5
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      webtable.rows.append([row[0], row[1], row[2], row[3], row[4]])
    
    #close the connection
    conn.close()

	#create a new table for packetmin.db
    pmintable = HTML.Table(header_row=['TIME', 'PACKETPERMIN'])
    
    #open database
    conn = sqlite3.connect('packetmin.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, PACKETPERMIN FROM PACK")limit 5
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      pmintable.rows.append([row[0], row[1]])
    
    #close the connection
    conn.close()

	#create a new table for monitordata.db
    cputable = HTML.Table(header_row=['TIME', 'CPUTEMP', 'STORAGE', 'UPTIME'])
    
    #open database
    conn = sqlite3.connect('monitordata.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, CPUTEMP, STORAGE, UPTIME FROM CPU")limit 5
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      cputable.rows.append([row[0], row[1], row[2], row[3]])
    
    #close the connection
    conn.close()
    
    #now generate the HTML output
    #the meta tag here forces a page refresh content = 10 means this happens every 10 seconds
    http_body = """
	 <!doctype html>
	 <html>
	 <head>
	 	<title> my server data </title>
	 	<meta http-equiv="refresh" content="15" >
	 </head>
	 <body> 
	 """ + str(cputable) + """ <br/>
	 """ + str(nettable) + """ <br/>
	 """ + str(webtable) + """ <br/>
	 """ + str(pmintable) + """ <br/>
	 """ + str(port1table) + """ <br/>
	 """ + str(port2table) + """ <br/>
	 """ + str(port3table) + """ 
	 </body>
	 </html>"""

    #finally send everything
    client_connection.send(http_status)
    client_connection.send(http_type)
    client_connection.send(http_body)
    client_connection.close()
