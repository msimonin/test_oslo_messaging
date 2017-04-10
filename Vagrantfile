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
apt-get install -y python-dev python-pip
pip install -U pip
pip install -r /vagrant/oslo-messaging-clients/requirements.txt
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = 'boxcutter/ubuntu1610'
  config.ssh.insert_key = false
  config.vm.synced_folder ".", "/vagrant", type: "rsync", disabled: false

	config.vm.provider "g5k" do |g5k, override|
		override.nfs.functional = false
		g5k.project_id = "test-vagrant-g5k"
		g5k.site = "rennes"
		g5k.username = "msimonin"
		g5k.gateway = "access.grid5000.fr"
		g5k.walltime = "01:00:00"
		g5k.image = {
			:path    => "/home/msimonin/public/ubuntu1404-9p.qcow2",
			:backing => "snapshot"
		}
		g5k.net = {
			:type => "bridge",
#            :ports => ["#{2222+i}-:22"]
		}
		g5k.oar = "virtual != 'none'"
#		g5k.resources = {
#			:cpu => 1,
#			:mem => 2048
#		}
	end #g5k
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
