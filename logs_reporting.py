#!/usr/bin/env python3

# Udacity FSND Project 3: Logs Analysis
# David Cohen

import psycopg2

DB_NAME = "news"


def popular_articles():
    """Find three most popular articles of all time"""

    connection = psycopg2.connect(database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """select articles.title, count(log.path)
        from articles, log
        where log.path = '/article/' || articles.slug
          and log.status = '200 OK'
        group by articles.title
        order by count(log.path) desc limit 3;"""
    )
    results = cursor.fetchall()
    print('\n\n' + "Most popular three articles of all time:" + '\n')
    for item in results:
        print("\"" + item[0].title() + "\": " + str("{:,}".format(item[1])) +
              " views")
    connection.close()


def popular_authors():
    """List authors in order of popularity based on total article views"""

    connection = psycopg2.connect(database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """select author_slug.name, count(log.path)
        from author_slug, log
        where log.path = '/article/' || author_slug.slug
          and log.status = '200 OK'
        group by author_slug.name
        order by count(log.path) desc;"""
    )
    results = cursor.fetchall()
    print('\n\n' + "Authors listed by popularity as defined by "
                   "total article views:" + '\n')
    for item in results:
        print(item[0] + ": " + str("{:,}".format(item[1])) + " views")
    connection.close()


def error_days():
    """List days that had >1% 404 errors"""

    connection = psycopg2.connect(database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """select total_view.day, (error_view.num/total_view.num)*100 as pct
        from total_view
        join error_view on total_view.day=error_view.day
        where (error_view.num/total_view.num)*100 > 1;"""
    )
    results = cursor.fetchall()
    print('\n\n' + "Days in which 404 errors accounted for >1% of "
                   "requests:" + '\n')
    for errday, errpercent in results:
        print(str(errday) + ": " + str(round(errpercent, 2)) + "%")
    print('\n')


if __name__ == "__main__":
    print('\n' + "-----------------------------------")
    popular_articles()
    popular_authors()
    error_days()
    print("-----------------------------------" + '\n')
