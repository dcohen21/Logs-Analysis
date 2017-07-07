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

##### Create views:
In order to run the reporting too, you need to create a few views in the `news` database. To do so, log into vagrant using `vagrant ssh`, and then open the PostgreSQL database using `psql news`. Then execute the following SQL statements:

```sql
create view author_slug as
        select authors.name, articles.slug
        from articles, authors
        where articles.author = authors.id;
```
```sql
create view error_view as
        select count(*)::numeric as num, time::date as day
        from log
        where status != '200 OK'
        group by day
        order by day desc;
```
```sql
create view total_view as
        select count(*)::numeric as num, time::date as day
        from log
        group by day;
```

##### Run the reporting tool
1. Download/clone this GitHub repository.
2. Move `logs_reporting.py` into the vagrant folder.
3. From terminal, run: `Python3 logs_reporting.py`
