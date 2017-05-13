# -*- coding: utf-8 -*-
from socket import *
from datetime import datetime                                   

def main():
    serverName = 'localhost'                                    
    serverPort = 12000                                        
    counter = 0;                                              

    message = input("Input Lowercase Message").encode('ascii')           

    while counter < 10:                                        
        counter = counter +1                                 
        mainSocket = socket(AF_INET,SOCK_DGRAM)                

        try:
            mainSocket.settimeout(1.0)                       
            startTime = datetime.now()                        

            mainSocket.sendto(message,(serverName, serverPort)) 
            modifiedMessage, serverAddress = mainSocket.recvfrom(1024)  
            endTime = datetime.now()                          

        except timeout:                                         
            print ('PINg ' +str(counter)+' '+ str(startTime)+ ': Request timed out!') 
            mainSocket.close()                                 
        else:                                                  
            print ('PING ' +str(counter)+' '+ str(startTime)+': Returned: ' + modifiedMessage.decode('ascii') + ' after '+ str(endTime-startTime))

    mainSocket.close()                                         
    pass

if __name__ == '__main__':
    main()
