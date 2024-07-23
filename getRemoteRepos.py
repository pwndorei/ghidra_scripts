import pyhidra
from os import environ

username = environ.get("GHIDRA_USER")
password = environ.get("GHIDRA_PASSWD")
host = environ.get("GHIDRA_SERVER_HOST")
port = int(environ.get("GHIDRA_SERVER_PORT"))


pyhidra.start()

import ghidra
from ghidra.framework.client import PasswordClientAuthenticator
from ghidra.framework.client import ClientUtil

auth = PasswordClientAuthenticator(username, password)

ClientUtil.setClientAuthenticator(auth)
ServerAdapter = ClientUtil.getRepositoryServer(host, port, False)


print(ServerAdapter.getRepositoryNames())