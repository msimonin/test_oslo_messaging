# Installation

```
git clone https://github.com/kgiusti/oslo-messaging-clients.git
```

Thanks @kgiusti :)

# Topology

```
+----------------------+
|  machine 01          |
|   + rabbitmq-server  |
|   + oslo.messaging   |
+----------------------+
          ||
          ||
          ||
          ||
+----------------------+
|  machine 02          |
|   + oslo.messaging   |
+----------------------+
```


# Start an oslo RPC Server

```
/vagrant/oslo-messaging-clients/rpc-server myserver [--url=rabbit://test:test@192.168.11.x]
```

# Start an oslo RPC client

```
# call
/vagrant/oslo-messaging-clients/rpc-client [--url=rabbit://test:test@192.168.11.x] echo a --repeat 100 --stats
# cast
/vagrant/oslo-messaging-clients/rpc-client [--url=rabbit://test:test@192.168.11.x] echo a --repeat 100 --stats --cast

```

# Add some latency

## machine01 and/or machine02

```
IF=enp0s8
# remove any previous policy
sudo tc qdisc del dev $IF root
sudo tc qdisc add dev $IF root netem delay 50ms
```


## Some results


### RPC Server, RPC client and broker collocated

* Min on 5 runs

```
call -> Messages per second: 96.3317 
cast -> Messages per second: 593.5845
```

### Server and broker collocated and remote client

* Min on 5 runs

```
Default latency : 0.300 ms

call -> Messages per second: 109.4419
cast -> Messages per second: 511.7233

Latency : 10ms

call -> Messages per second: 47.8049
cast -> Messages per second: 76.4053

Latency : 50ms

call -> Messages per second: 14.9477
cast -> Messages per second: 17.7845
```


### Client and broker collocated and remote server

* Min on 5 runs

```
Default latency : 0.300 ms

call -> Messages per second: 88.6217
cast -> Messages per second: 684.3274

Latency : 10ms

call -> Messages per second: 37.1791
cast -> Messages per second: 688.8522

Latency : 50ms

call -> Messages per second: 13.9842
cast -> Messages per second: 1168.1541

Latency : 100ms

call -> Messages per second: 8.5113
cast -> Messages per second: 1092.7049

```

