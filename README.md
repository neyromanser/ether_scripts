# Sign And Check Ethereum Message With Python 3

Simple Python class for signing message with Ethereum private key and check signature without use of solidity contract  

# usage  
```
message_to_sign = 'Lorem ipsum...'   
address = '0xe838256da78fD4206B85363424525791f12555f0'   
password = 'Pa55w0r'
```
### sign message  
```
# using http rpc   
signature = EthSigner.sign_message(message_to_sign, address, password, rpc_url='http://127.0.0.1:8545')  

# or using ipc on windows  
signature = EthSigner.sign_message(message_to_sign, address, password, ipc='\\\\.\\pipe\\geth.ipc')  
 
print("signature: " + signature)   
```
### verify signature
```
owner_address = EthSigner.check_sign(message_to_sign, signature)  
print("owner_address: " + owner_address)  
 
if owner_address == address:   
    print("OK!")  
```

### DONATE
Script absolutely free, but any support is appreciated ;)
```
ETH: 0xe838256da78fD4206B85363424525791f12555f0
```