#!/usr/lib/zabbix/externalscripts/venv/bin/python
from smb.SMBConnection import SMBConnection
import socket

username = ''
password = ''
host = ''  # host_ip or dns
share_name = ''
path_in_share = ''

def is_path_accessible(server_ip, share_name, remote_path, username=None, password=None, timeout=5):
    try:
        hostname = socket.gethostname()
        conn = SMBConnection(
            username or '',
            password or '',
            hostname,
            "server",
            use_ntlm_v2=True,
            is_direct_tcp=True
        )
        if not conn.connect(server_ip, 445, timeout=timeout):
            return False

        # Проверяем, существует ли путь (попытка получить файлы или подкаталоги)
        files = conn.listPath(share_name, remote_path)
        conn.close()
        return True  # Если не было исключения — путь доступен
    except:
        return False

if is_path_accessible(
    host,
    share_name,
    path_in_share,
    username,
    password
):
    print("1")
else:
    print("0")
