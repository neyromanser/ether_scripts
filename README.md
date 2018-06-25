# Sign And Check Ethereum Message With Python 3

Simple Python class for signing message with Ethereum private key and check signature without use of solidity contract  

# usage  
```
message = 'Lorem ipsum...'   
address = '0xe838256da78fD4206B85363424525791f12555f0'   
```
### sign message
```
signer = EthSigner(ipc='\\\\.\\pipe\\geth.ipc')   
signature = signer.sign_message(message, address, 'YOUR_PASSWORD')   
print("sign: " + signature)   
```
### verify signature
```
signer = EthSigner()   
owner = signer.check_sign(message, signature)   
print("owner: " + owner)   
```

### DONATE
Script absolutely free, but any support is appreciated ;)
```
ETH: 0xe838256da78fD4206B85363424525791f12555f0
```