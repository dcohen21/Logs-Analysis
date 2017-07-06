#!/usr/bin/env python3


import psycopg2

DB_NAME = "news"


def popular_articles():
    """Find three most popular articles of all time"""

    connection = psycopg2.connect(database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """select articles.title, count(log.path) from articles, log 
        where log.path like '%'||articles.slug 
        group by articles.title 
        order by count(log.path) desc limit 3;""")
    results = cursor.fetchall()
    print('\n' + "Most popular three articles of all time:" + '\n')
    for item in results:
        print("\"" + item[0].title() + "\": " + str(item[1]) + " views")


if __name__ == "__main__":
    popular_articles()
