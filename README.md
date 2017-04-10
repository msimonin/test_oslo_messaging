# Installation

```
git clone https://github.com/kgiusti/oslo-messaging-clients.git
```

# Server

```
/vagrant/oslo-messaging-clients/rpc-server myserver
```

# Client

```
# call
/vagrant/oslo-messaging-clients/rpc-client --url=rabbit://test:test@192.168.11.2 echo a --repeat 100 --stats
# cast
/vagrant/oslo-messaging-clients/rpc-client --url=rabbit://test:test@192.168.11.2 echo a --repeat 100 --stats --cast

```


# Add some latency

## Client and Server

```
IF=enp0s8
# remove any previous policy
sudo tc qdisc del dev $IF root
sudo tc qdisc add dev $IF root netem delay 50ms
```


## Some results

(Min on 5 runs)

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


