# -*- mode: ruby -*-
# vi: set ft=ruby :

$server = <<SCRIPT
apt-get install -y rabbitmq-server
rabbitmqctl add_user test test
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
service rabbitmq-server restart
SCRIPT

$all = <<SCRIPT
apt-get update
apt-get install -y python-pip
pip install -U pip
pip install -r /vagrant/oslo-messaging-clients/requirements.txt
SCRIPT

Vagrant.configure(2) do |config|
  # config.vm.box = "debian/contrib-jessie64"
  config.vm.box = 'boxcutter/ubuntu1610'
  # build machine
  config.vm.define "server" do |server|
    server.vm.network "private_network", ip: "192.168.11.2"
    server.vm.provision "shell", inline: $all
    server.vm.provision "shell", inline: $server
  end

  # server machine
  config.vm.define "client" do |client|
    client.vm.network "private_network", ip: "192.168.11.3"
    client.vm.provision "shell", inline: $all
  end
end
