# Weather-app
a python application for getting the current weather

## Requirements

So far the requirements for running this application are:

* A laptop/PC with adequate CPU, RAM and storage space

* Virtualbox

* Vagrant

* Ansible

Software versions are all latest.

## Instructions

First, clone the repository and change to the weather-app directory

After successfully cloning the repository, run the following command

    vagrant up

This command will read the Vagrantfile and initiate a Virtualbox virtual machine which uses CentOS 7 as its operating system.
We have assigned Ansible as our provisioner in the Vagrantfile and we've specified the playbook for Ansible to use and configure the machine.
Ansible will copy the required files, as well as setup Docker on the machine so that we can build and run our image.
Ansible will also set Docker's log driver to syslog.
After Ansible finishes configuring the virtual machine, we can access the machine's terminal by using the following command:

    vagrant ssh

Great! We can now run commands on our VM. We have to build our image before running it, with the following commands:

    cd weather-app/
    sudo docker build . -t weather-app:dev

This will build the image and configure it for use.
Finally we just have to run our image and provide the required environment variables (make sure to replace the values inside: <>):

    sudo docker run --rm -e OWM_API_KEY="<xxxx>" -e OWM_CITY="<Desired City>" weather-app:dev

Example:

    sudo docker run --rm -e OWM_API_KEY="<xxxx>" -e OWM_CITY="Miami" weather-app:dev
    city="Miami", description="broken clouds", temp="32.48", humidity="69"

It sure is hot! Now we know what to wear today.

Continuing on our example, you can also check if your log driver is working by running the following command:

    grep "Miami" /var/log/messages

## Conclusion

This is it for our simple weather app, definitely a fun exercise for your development skills! 

