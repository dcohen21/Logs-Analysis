# Udacity FSND Logs-Analysis Project
This is the third project for the Udacity Full Stack Nanodegree.

## Project Overview
This project uses Python3 to interact with a PostgreSQL database containing information from a newspaper site. The Python3 module `logs_reporting.py` is a reporting tool that creates a report that answers the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements
##### Install the following:
- <a href="https://www.python.org">Python3</a>
- <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a>
- <a href="https://www.vagrantup.com/">Vagrant</a>

##### Set up the virtual machine:
1. Download and unzip <a href="https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip">the virtual machine configuration.</a>
2. From a terminal, change directory to the vagrant directory that you just unzipped.
3. To create virtual machine, run terminal command: `vagrant up`
4. To log into the virtual machine, run terminal command: `vagrant ssh`

##### Load the database:
1. Download and unzip <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">the data.</a>
2. Move `newsdata.sql` into the vagrant folder.
3. To load the data, run terminal command: `psql -d news -f newsdata.sql`

##### Run the reporting tool
1. Download/clone this GitHub repository.
2. Move `logs_reporting.py` into the vagrant folder.
3. From terminal, run: `Python3 logs_reporting.py`
