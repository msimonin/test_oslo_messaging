# Installation

```
git clone https://github.com/kgiusti/oslo-messaging-clients.git
```

Thanks @kgiusti :)


```
vagrant up [--provider=g5k]
```

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

* Virtualbox : 1 core/512 MRAM
* G5K : 8 cores/24GRAM

### RPC Server, RPC client and broker collocated

* Min on 5 runs

```
call -> Messages per second: 96.3317 
(g5k) call -> Messages per second: 224.1414 
cast -> Messages per second: 593.5845
(g5k) cast -> Messages per second: 1119.7083
```

### Server and broker collocated and remote client

* Min on 5 runs

```
Default latency : 0.300 ms

call -> Messages per second: 109.4419
(g5k) call -> Messages per second: 218.7064
cast -> Messages per second: 511.7233
(g5k) cast -> Messages per second: 1062.6643

Latency : 10ms

call -> Messages per second: 47.8049
(g5k) call -> Messages per second: 62.4751
cast -> Messages per second: 76.4053
(g5k) cast -> Messages per second: 84.8528

Latency : 50ms

call -> Messages per second: 14.9477
(g5k) -> Messages per second: 16.1241
cast -> Messages per second: 17.7845
(g5k) cast -> Messages per second: 18.3269
```


### Client and broker collocated and remote server

* Min on 5 runs

```
Default latency : 0.300 ms
(g5k) Default latency : 0.200 ms

call -> Messages per second: 88.6217
(g5k) call -> Messages per second: 215.6920
cast -> Messages per second: 684.3274
(g5k) cast -> Messages per second: 1129.5476

Latency : 10ms

call -> Messages per second: 37.1791
cast -> Messages per second: 688.8522

Latency : 50ms

call -> Messages per second: 13.9842
(g5k) call -> Messages per second: 14.6501
cast -> Messages per second: 1168.1541
(g5K) -> Messages per second: 1170.6581

Latency : 100ms

call -> Messages per second: 8.5113
(g5k) => Messages per second: 8.7119
cast -> Messages per second: 1092.7049
(g5k) -> Messages per second: 1205.2702

```

