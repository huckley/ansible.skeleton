# -*- mode: ruby -*-
# vi: set ft=ruby :
system("
    if [ #{ARGV[0]} = 'up' ]; then
        echo 'You are doing vagrant up and can execute your script'
        ansible-galaxy install -r tests/requirements.yml -p ./tests/roles -f
    fi
")

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  #config.vm.synced_folder ".", "/vagrant", type: "nfs"

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.


  config.vm.provider "virtualbox" do |v|
    v.memory = 256
    v.cpus = 1
  end

  config.vm.provision "ansible" do |ansible|
    # ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
    ansible.compatibility_mode = "2.0"
    # ansible.verbose = "vvv"
    ansible.playbook = "tests/test.yml"
    ansible.galaxy_roles_path = "../"
  end

  # config.vm.define "debian-5" do | debian5 |
  #   debian5.vm.box = "alexoleshkevich/lenny64-nn"
  # end

  config.vm.define "debian-6" do | debian6 |
    debian6.vm.box = "puppetlabs/debian-6.0.10-64-nocm"
  end

  config.vm.define "debian-7" do | debian7 |
    debian7.vm.box = "deimosfr/debian-wheezy"
  end

  config.vm.define "debian-8" do | debian8 |
    debian8.vm.box = "generic/debian8"
  end

  config.vm.define "debian-9" do | debian9 |
    debian9.vm.box = "generic/debian9"
  end

  config.vm.define "debian-10" do | debian10 |
    debian10.vm.box = "generic/debian10"
  end

  config.vm.define "debian-11" do | debian11 |
    debian11.vm.box = "generic/debian11"
  end
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y python3-pip
  # SHELL
  #
  # config.vm.provision "shell", inline: <<-SHELL
  #   pip3 install pytest-testinfra==6.4.0
  # SHELL
  #
  # config.vm.provision "file", source: "./tests/test.py", destination: "test.py"
  # config.vm.provision "shell", inline: <<-SHELL
  #   py.test -v test.py
  # SHELL

end
