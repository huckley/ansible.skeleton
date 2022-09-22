import requests

def test_nginx_docker(host):
    nginx = host.docker("nginx")
    assert nginx.is_running

def test_http_is_listening(host):
    http = host.socket("tcp://0.0.0.0:80")
    assert http.is_listening

def test_https_is_listening(host):
    https = host.socket("tcp://0.0.0.0:443")
    assert https.is_listening

def test_default_http_server():
    default_http = requests.get('http://127.0.0.1', allow_redirects=False)
    assert default_http.status_code == 301

