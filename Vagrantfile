required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

#required_variable = ["export DB_HOST=mongodb://192.168.10.150:27017/posts"]
# required_plugins.each do |variable|
  #  exec "echo #{variable} >> /home/ubuntu/.bashrc" >> /environment/app/provision.sh
# end


Vagrant.configure("2") do |config|
  config.vm.define "python" do |python|
    python.vm.box = "ubuntu/bionic64"
    python.vm.network "private_network", ip: "192.168.10.200"
    python.hostsupdater.aliases = ["python.local"]
    python.vm.synced_folder ".", "/home/vagrant/python"
    python.vm.provision "shell", path: "provision.sh", privileged: false
    python.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
  end


end
