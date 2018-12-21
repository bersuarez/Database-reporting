#!/usr/bin/env python3

import psycopg2


def connect(news):
    """
     Connect to the PostgreSQL database.
     Return a database connection.
    """
    try:
        db = psycopg2.connect("dbname={}".format(news))
        create_views = open("create_views.sql").read()
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("\n"+"Connected! Performing query")
    cursor = db.cursor()
    return db, cursor, create_views


def busqueda(pregunta, titulo, unidad):
    conn, cursor, create_views = connect("news")
    if __name__ == '__main__':
        cursor.execute(create_views)
        cursor.execute("select * from "+pregunta)
        results = cursor.fetchall()
        formated_results = "\n".join(
            [str(result[0])+" - "+str(result[1])+unidad for result in results])
        print("\n"+(titulo))
        print(formated_results)
        conn.close()
    else:
        print("Import")


get_popular_articles = busqueda(
    'question1', 'Most popular articles: ', ' views')
get_popular_authors = busqueda(
    'question2', 'Most popular authors: ', ' views')
get_buggy_days = busqueda(
    'question3', 'Buggy days: ', ' errors')
