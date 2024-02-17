import socket
#t ends the code when later set to false
t =True
#Listed are many common ports and their protocols and security
commonPorts={20:'FTP file transfer (not secure)',80:'HTTP web server (not secure)',
443:'HTTPS web server (secure)',
21:'FTP file transfer (not secure)',
22:'SSH transfer protocol (secure)',25:'SMTP (not fully secure)',
53:'DNS domain name system',
57:'MTP',23: 'Telnet: remote access (not secure)', 
110: 'POP3 post office protocol (not secure)',
135: 'MSRPC client-server communication (not secure)',
139: 'NetBIOS-SSN file services (not secure)',
143: 'IMAP 	Internet Message Access Protocol (not secure)',
445: 'SMB server message blocks (not secure)',
1433: 'MSSQL-S (not fully secure)',3128:'HTTPS web proxy',1723:'PPTP', 3306:'MySQL', 
123: 'NTP Network Time Protocol', 179:'BGP Border Gateway Protocol', 
995:'POP3S mail encryption (secure)', 993:'IMAPS email retrieval (secure)'}
#This is the function that will be used to scan the ports
def scan_port(ip, port):
  try:
    s = socket.socket()
    s.settimeout(.5)
    s.connect((ip, port))
    banner = s.recv(1024)
    #If the port is one of the common ones then the extra information will be printed/saved
    if port in commonPorts.keys():
      print(f"Port {port} is open on {ip} with the banner: {banner} \n{commonPorts[port]}")
      open_port.append(f"Port {port} is open on {ip} with the banner: {banner} \n{commonPorts[port]}")
    else:
      print(f"Port {port} is open on {ip} with the banner:\n {banner}")
      open_port.append(f"Port {port} is open on {ip} with the banner:\n {banner}")
  except Exception as e:
    #Exceptions "e" will be printed if show is set to true by the user
    if show:
      print("Port",port,str(e).replace("[Errno 111] ", ""))
    else:
      pass
  finally:
    s.close()

#This is the main loop of the code
while t:
  #initializes the open port list
  open_port = []
  show = False
  if input("Do you want to show error messages? (y/n) ").lower().strip(' ') == "y":
    show = True
  website = str(input("Enter the target website in the format of 'www.example.com'\n"))
  try:
    ip = socket.gethostbyname(website)
    n1=int(input('Enter the first port you want to scan: '))
    n2=int(input('Enter the last port you want to scan: '))
    for i in range(n1, n2+1):
      scan_port(ip, i)
    if (input("Do you want to scan other special ports? (y/n) ") == 'y'):
      try:
        list1 = []
        s = input("Enter the special ports you want to scan,"
            " separated by spaces. (Ex: 8080 3306 3389)\n")
        #The inputs are separated by spaces and mapped from strings to integers
        list1 = list(map(int, s.split()))
        for i in list1:
          scan_port(ip, i)
      except:
        print("Invalid input")

    if show:
      #Prints the open ports without brackets or commas
      print("\n", ' '.join(open_port))
    print("The scan is complete")
    try_again = input("Do you want to try again? (y/n) ")
    if (try_again == 'y'):
      pass
    elif (try_again == 'n'):
      #The while loop exits and the code effectively ends
      t = False
    else:
      #Neither y or n was entered
      print("Invalid input. Exiting program")
      t = False
        
  except:
    #This is here incase the website entered is invalid and 
    #ip = socket.gethostbyname(website) cannot be done, or any other inputs cause errors
    print("Invalid input. Please try again\n")