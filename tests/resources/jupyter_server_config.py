def mappathf(path):
    p = path + 'mapped'
    return p

c.ServerProxy.servers = {
    'python-http': {
        'command': ['python3', './tests/resources/httpinfo.py', '{port}'],
    },
    'python-http-abs': {
        'command': ['python3', './tests/resources/httpinfo.py', '{port}'],
        'absolute_url': True
    },
    'python-http-port54321': {
        'command': ['python3', './tests/resources/httpinfo.py', '{port}'],
        'port': 54321,
    },
    'python-http-mappath': {
        'command': ['python3', './tests/resources/httpinfo.py', '{port}'],
        'mappath': {
            '/': '/index.html',
        }
    },
    'python-http-mappathf': {
        'command': ['python3', './tests/resources/httpinfo.py', '{port}'],
        'mappath': mappathf,
    },
    'python-https' : {
        'command': ['python3', './tests/resources/httpinfo.py', '--keyfile=./tests/resources/key.pem', '--certfile=./tests/resources/cert.pem', '{port}'],
        'https': True,
        # Self-signed cert, use certificate as ca
        'cafile': './tests/resources/cert.pem',
        'check_hostname': True,
    },
    'python-websocket' : {
        'command': ['python3', './tests/resources/websocket.py', '--port={port}'],
    }
}

import sys
sys.path.append('./tests/resources')
c.NotebookApp.nbserver_extensions = { 'proxyextension': True }
#c.Application.log_level = 'DEBUG'
