"""This module handles all the initial database transactions"""

import os
import psycopg2

class Db:
    def __init__(self):
        self.con = psycopg2.connect(
            dbname = 'Crud',
            user = 'postgres',
            host = 'localhost',
            password = '6398litein'
        )
        self.cur = self.con.cursor()

        
    def create_tables(self):
        queries = (
             # creates users table
            """CREATE TABLE IF NOT EXISTS users( 
                id SERIAL PRIMARY KEY,
                firstname VARCHAR(255) NOT NULL,
                lastname VARCHAR(255) NOT NULL,
                othername VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phoneNumber VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                registered VARCHAR(255) NOT NULL,
                isAdmin BOOLEAN NOT NULL
            )""",
            # creates ride_offer table
            """CREATE TABLE IF NOT EXISTS incidences(
                id SERIAL PRIMARY KEY,
                createdOn VARCHAR(255) NOT NULL,
                createdBy VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                status VARCHAR(255) NOT NULL,
                comment VARCHAR(255) NOT NULL
            )""",
        )
        for q in queries:
            self.cur.execute(q)
            self.con.commit()

    def drop_all_tables(self):
        '''Deletes all the tables'''
        queries = (
            'drop table if exists "users" cascade;',
            'drop table if exists "incidences" cascade;'
        )

        for q in queries:
            self.cur.execute(q)
            self.con.commit()

