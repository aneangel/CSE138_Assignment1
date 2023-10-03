import socket
import json

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 8090))
serverSocket.listen(5)


def handle_request(client_ock):
    request_data = client_ock.recv(1024).decode()
    if request_data:
        request_lines = request_data.split('\n')
        request_method, path, _ = request_lines[0].split()

        # GET Methods for '/hello' '/hello/' '/test'
        # Currently only GET methods work Oct 3, 2023: 12:31pm
        if request_method == 'GET':

            if path == '/hello':
                response_body = json.dumps({"message": "world"})
                response = f'HTTP/1.1 200 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

            elif path.startswith('/hello/'):
                response_body = 'Method Not Allowed'
                response = f'HTTP/1.1 405 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

            elif path == '/test':
                response_body = json.dumps({"message": "test is successful"})
                response = f'HTTP/1.1 200 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

            # Server Catch for potential errors that aren't predefined
            else:
                response_body = 'Server Error: Method Not Supported'
                response = f'HTTP/1.1 400 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

        # POST Methods for '/hello' '/hello/' '/test'
        elif request_method == 'POST':

            if path == '/hello':
                response_body = 'Method Not Allowed'
                response = f'HTTP/1.1 405 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

            elif path.startswith('/hello/'):
                name = path.split('/')[-1]
                response_body = '{"message":"Hi, {}"'.format(name)
                response = f'HTTP/1.1 200 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'

            elif path == '/test':
                pass

            # Server Catch for potential errors that aren't predefined
            else:
                response_body = 'Server Error: Method Not Supported'
                response = f'HTTP/1.1 400 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                           f'\n\n{response_body}'
        else:
            response_body = 'Server Error: Method Not Supported'
            response = f'HTTP/1.1 400 OK\nContent-Type: application/json\nContent-Length: {len(response_body)}' \
                       f'\n\n{response_body}'

        client_ock.send(response.encode())
        client_ock.close()


while True:
    client_socket, addr = serverSocket.accept()
    handle_request(client_socket)
