import pyhidra
from os import environ
from sys import exit

username = environ.get("GHIDRA_USER")
password = environ.get("GHIDRA_PASSWD")
host = environ.get("GHIDRA_SERVER_HOST")
port = int(environ.get("GHIDRA_SERVER_PORT"))
base_url = f"ghidra://{host}:{port}/"


#pyhidra.start()
headless = pyhidra.HeadlessPyhidraLauncher()

headless.verbose = True

headless.start()

import ghidra
from ghidra.framework.client import ClientUtil, PasswordClientAuthenticator
from ghidra.app.util.headless import HeadlessAnalyzer

from ghidra.framework.client import RepositoryNotFoundException

from java.util import LinkedList
from java.net import URL
from java.io import IOException, File

auth = PasswordClientAuthenticator(username, password)
analyzer = HeadlessAnalyzer.getInstance()

ClientUtil.setClientAuthenticator(auth)
ServerAdapter = ClientUtil.getRepositoryServer(host, port, False)


if not ServerAdapter.isConnected():
    print("Connection Failed!!")
    exit(-1)


Repo = ServerAdapter.getRepository("test")


try:
    Repo.connect()

except RepositoryNotFoundException:
    ServerAdapter.createRepository("test")
    Repo.connect()


analyzer.options.enableAnalysis(True)

files = LinkedList([File("/path/to/file")])

analyzer.options.setMaxCpu(3)
analyzer.options.setCommitFiles(True, "some commit msg")
analyzer.options.enableAnalysis(True)
analyzer.options.enableRecursiveProcessing(True)
analyzer.options.setPerFileAnalysisTimeout(200)


analyzer.processURL(URL(base_url + "reponame/path/to/subfolder/or/file"), files)

Repo.disconnect()