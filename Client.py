import socket
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    print('Welcome to Course Registration')
    print('Please Enter your full name!')
    message = input("->")  # take input

    while message != 'Bye':
        client_socket.send(message.encode())  # send message
        print('please enter your Matric Number! \n To close this program type "Bye"')
        Matric = input('->')
        client_socket.send((Matric.encode()))
        print('Please choose one course 1 or 2 or 3 \n 1. Digital Communication \n 2. Optical Communication \n 3. Network Programming \n To close this program type "Bye"')
        First_Course = input(" -> ")
        client_socket.send((First_Course.encode()))
        print('Please choose one course 1 or 2 or 3 \n 1. French Language \n 2. Mandarin Language \n 3. Arab Language \n To close this program type "Bye"')
        Second_Course = input('->')
        client_socket.send((Second_Course.encode()))
        data = client_socket.recv(1024).decode()
        data = str(data)
        if data == 'Wrong input':
            print('Wrong input \n Please try again!')
            print('Please Enter your full name! \n To close this program type "Bye"')
            message = input("->")
        else:
            print('Please Enter your full name! \n To close this program type "Bye"')
            message = input("->")
    client_socket.close()  # close the connection
if __name__ == '__main__':
    client_program()