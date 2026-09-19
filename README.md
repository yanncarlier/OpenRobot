# Open robot


<https://vimeo.com/showcase/5792761/video/319684031>

This was developed in openlab @ HSBC during a weekend hackathon 

##### App Description

Open Robot its integration between HSBC API, blockchain and robots. 
To function a robot has to have assets in the bank account.

#####1. Install multichain blockchain

#####2. Connecting to the blockchain
multichaind asimov start

cat multichain.conf
rpcuser=XXXXXX
rpcpassword=XXXXXXXXXXXX

multichain-cli asimov

create stream funds-available false

asimov: liststream
{"method":"liststream","params":[],"id":"74723210-1567847018","chain_name":"asimov"}

asimov: listpermissions funds-available.*
{"method":"listpermissions","params":["funds-available.*"],"id":"26254798-1567846952","chain_name":"asimov"}

Examples:
> multichain-cli asimov liststreamkeys "test-stream"
> multichain-cli asimov liststreamkeys "test-stream" "key01"
> multichain-cli asimov liststreamkeys "test-stream" "*" true 10 100
> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "liststreamkeys", "params": ["test-stream", "key01"] }' -H 'content-type: text/plain;' http://127.0.0.1:6268



publish funds-available key1 

curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"key1", "method": "publish", "params": ["stream", "funds-available", false] }' -H 'content-type: text/plain;' http://127.0.0.1:6268



You can connect to this node using:

multichaind asimov@openrobotmoney.org:6269

Send an  email including your node address to grant you access and stream permissions


