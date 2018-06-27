#!/usr/bin/env python3

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
#        Ethereum sign and check message          #
#              by Neyromanser 2018                #
#  https://github.com/neyromanser/ether_scripts   #
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #

from web3 import Web3, IPCProvider, HTTPProvider
import bitcoin
import codecs
import sha3


class EthSigner:

    @classmethod
    def sign_message(cls, message, address, password, ipc=None, rpc_url=None):
        if ipc is not None:
            w3 = Web3(IPCProvider(ipc))
        elif rpc_url is not None:
            w3 = Web3(HTTPProvider(rpc_url))

        sha = '0x' + cls.sha3(text=message)
        w3.personal.unlockAccount(address, password)
        signature = w3.eth.sign(address, hexstr=sha)
        return signature

    @staticmethod
    def bytes_to_hex(string):
        hex_str = ''
        for let in string:
            hex_str += format(ord(let), "02x")
        return hex_str

    @staticmethod
    def sha3(text=None, hexstr=None):
        k = sha3.keccak_256()
        if text is not None:
            k.update(text.encode('utf-8'))
        elif hexstr is not None:
            k.update(codecs.decode(hexstr, 'hex'))

        return k.hexdigest()

    @classmethod
    def check_sign(cls, message, signature):
        prefix = '\x19Ethereum Signed Message:\n32'
        message_hash = cls.sha3(text=message)
        full_message = cls.bytes_to_hex(prefix) + message_hash
        full_hash = cls.sha3(hexstr=full_message)

        r = int(signature[0:66], 16)
        s = int('0x'+signature[66:130], 16)
        v = int('0x'+signature[130:132], 16)
        if not v == 27 and not v == 28:
            v += 27

        recovered = bitcoin.ecdsa_raw_recover(full_hash, (v, r, s))
        pub = bitcoin.encode_pubkey(recovered, 'bin')
        address = cls.sha3(hexstr=pub[1:].hex())[24:64]
        return '0x' + address
