import paramiko
import subprocess as sb
import pytest
import signal

# Дані вашого серверу, які будуть використовуватися для підключення по ssh до серверу.
server_ip = '172.25.112.1'
password = ''
username = 'torgm'


@pytest.fixture(scope='function')
def server():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, password=password)

    # Код для підняття iperf сервера
    process = sb.Popen("iperf3 -s")

    # Закриття ssh підключення
    yield
    process.terminate()
    ssh.close()


@pytest.fixture(scope='function')
def client(server):
    command = f'iperf3 -c {server_ip}'

    process = sb.Popen(command, shell=True, stdout=sb.PIPE, stderr=sb.PIPE)
    output, error = process.communicate()

    return output.decode(), error.decode()
