import socket
from collections import defaultdict
import re
from http import HTTPStatus

address = ('192.168.0.245', 48488)
response_status = '200 OK'

with socket.socket() as s:
    s.bind(address)
    s.listen(10)
    conn, addr = s.accept()
    data = conn.recv(1024)
    message = data.decode('UTF-8')
    response = defaultdict(
        lambda: {"Request Method": "GET", "Request Source": None, "Response Status": "200 OK", "header-name": None}
    )

    response["Request Source"] = addr
    status = re.search(r"status=(\d{3})", message)

    if status is not None:
        for item in list(HTTPStatus):
            code = int(status.groups()[0])
            if item.value == code:
                response_status = f'{item.value} {item.phrase}'
                response["Response Status"] = response_status
                break
            else:
                response_status = f'{code}, OK'
                response["Response Status"] = response_status

    else:
        response["Response Status"] = response_status

    list_headers = re.findall(r'\S+: \S+', message)

    if list_headers is not None:
        response = ' '.join([f'{key}: {value}' for key, value in response.items()] + list_headers)

    conn.send(f'HTTP/1.1 {response_status} Content-Length: 100\n Connection close \n'
              f' Content-Type text/html\n\n <h1> {response}</h1>'.encode('utf-8'))

    print(response)
