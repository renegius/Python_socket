# Socket Programming Report

This document summarizes the behaviour observed for each programming step.

## Step 1 - Basic TCP
A single client connects to `step1_server.py` and sends a message. The server
accepts one connection and prints the received data. Communication succeeds
without issues.

## Step 2 - Multiple TCP Clients
`step2_server.py` uses threads to handle clients. Running `step2_client.py`
launches 10 client threads concurrently. All clients connect successfully and
the server prints each message. Because the server handles connections in
separate threads, the clients do not block each other and all connections
succeed.

## Step 3 - Server Replies
`step3_server.py` extends the previous server by sending a reply whenever it
receives data. `step3_client.py` prints the response from the server. Each of
the 10 clients receives a `"Message received"` reply confirming that the server
processed their message.

## Step 4 - UDP Version
`step4_server.py` and `step4_client.py` switch to UDP sockets. UDP is
connectionless, so clients send datagrams without establishing a persistent
connection. All clients send messages almost simultaneously and the server
replies with a datagram to each sender. Because UDP does not guarantee
ordering or delivery, packets could be lost in a congested environment, but in
local testing each client receives a response.
