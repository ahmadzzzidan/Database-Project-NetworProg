import socket
import sqlite3
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        database = sqlite3.connect('course.db')
        cur = database.cursor()
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Full Name: " + str(data))
        Full_Name = str(data)
        data1 = conn.recv(1024).decode()
        print('Matric ID: ' + str(data1))
        data2 = conn.recv(1024).decode()
        print("First course selection: " + str(data2))
        data3 = conn.recv(1024).decode()
        print("Second course selection: " + str(data3))
        Matric = str(data1)
        First_Course = str(data2)
        Second_Course = str(data3)
        if (First_Course == '1'or First_Course =='2'or First_Course =='3') and (Second_Course == '1' or Second_Course =='2'or Second_Course =='3'):
            data = 'Correct'
            conn.send(data.encode())
            cur.execute("CREATE TABLE IF NOT EXISTS course(Full_Name text, Matric text, First_Course text, Second_Course text)");
            cur.execute("INSERT INTO course VALUES ({!r},{!r},{!r},{!r})".format(Full_Name, Matric, First_Course, Second_Course))
            database.commit()
            cur.execute("SELECT * FROM course")
        else:
            Wrong1 = 'Wrong input'
            conn.send(Wrong1.encode())
        database.close()
    conn.close()
if __name__ == '__main__':
    server_program()