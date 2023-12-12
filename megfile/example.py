import getpass
import os
import socket

import ssh2
from ssh2.session import Session

host = 'localhost'

pubkey = "~/.ssh/id_rsa.pub"
privkey = "~/.ssh/id_rsa"
username = "testuser"
password = "testuser"

import pdb

pdb.set_trace()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 22))

session = Session()
session.handshake(sock)
hostkey_tuple = session.hostkey()
pdb.set_trace()
fingerprint = session.hostkey_hash(ssh2.session.LIBSSH2_HOSTKEY_HASH_SHA1)
userauthlist = session.userauth_list(username)

auth = session.userauth_password(username, password)
key_with_types = [
    session.LIBSSH2_HOSTKEY_TYPE_UNKNOWN,
    session.LIBSSH2_HOSTKEY_TYPE_RSA,
    session.LIBSSH2_HOSTKEY_TYPE_DSS,
    session.LIBSSH2_HOSTKEY_TYPE_ECDSA_256,
    session.LIBSSH2_HOSTKEY_TYPE_ECDSA_384,
    session.LIBSSH2_HOSTKEY_TYPE_ECDSA_521,
    session.LIBSSH2_HOSTKEY_TYPE_ED25519,
]