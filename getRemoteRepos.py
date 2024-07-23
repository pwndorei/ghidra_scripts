import pyhidra
from os import environ

username = environ.get("GHIDRA_USER")
password = environ.get("GHIDRA_PASSWD")


pyhidra.start()

import ghidra
from ghidra.framework.client import PasswordClientAuthenticator
from ghidra.framework.client import ClientUtil

auth = PasswordClientAuthenticator(username, password)

ClientUtil.setClientAuthenticator(auth)
ServerAdapter = ClientUtil.getRepositoryServer("192.168.0.11", 13100, False)


print(ServerAdapter.getRepositoryNames())