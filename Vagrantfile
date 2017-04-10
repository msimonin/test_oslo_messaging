# -*- mode: ruby -*-
# vi: set ft=ruby :

$rabbit = <<SCRIPT
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
  config.vm.box = 'boxcutter/ubuntu1610'

  config.vm.define "machine01" do |machine|
    machine.vm.network "private_network", ip: "192.168.11.2"
    machine.vm.provision "shell", inline: $all
    machine.vm.provision "shell", inline: $rabbit
  end

  config.vm.define "machine02" do |machine|
    machine.vm.network "private_network", ip: "192.168.11.3"
    machine.vm.provision "shell", inline: $all
  end
end
