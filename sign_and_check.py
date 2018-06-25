#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from web3 import Web3, HTTPProvider
import bitcoin as b
import codecs
import sha3


class EthSigner:

    w3 = None

    def __init__(self, ipc=None, url=None):
        if ipc is not None:
            self.w3 = Web3(Web3.IPCProvider(ipc))
        elif url is not None:
            self.w3 = Web3(HTTPProvider(url))

    def sign_message(self, message, address, password):
        sha = self.w3.sha3(text=message)
        self.w3.personal.unlockAccount(address, password)
        signature = self.w3.eth.sign(address, hexstr=sha)
        return signature

    def bytes_to_hex(self, string):
        hex_str = ''
        for let in string:
            hex_str += format(ord(let), "02x")
        return hex_str

    def sha3(self, text=None, hexstr=None):
        k = sha3.keccak_256()
        if text is not None:
            k.update(text.encode('utf-8'))
        elif hexstr is not None:
            k.update(codecs.decode(hexstr, 'hex'))

        return k.hexdigest()

    def check_sign(self, message, signature):
        prefix = '\x19Ethereum Signed Message:\n32'
        msghash = self.sha3(text=message)
        full_message = self.bytes_to_hex(prefix) + msghash
        full_hash = self.sha3(hexstr=full_message)

        r = int(signature[0:66], 16)
        s = int('0x'+signature[66:130], 16)
        v = int('0x'+signature[130:132], 16)
        if not v == 27 and not v == 28:
            v += 27

        recovered_addr = b.ecdsa_raw_recover(full_hash, (v, r, s))
        pub = b.encode_pubkey(recovered_addr, 'bin')
        address = self.sha3(hexstr=pub[1:].hex())[24:64]
        return '0x' + address


