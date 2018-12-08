"""This module contains the incident model that adds a new incident to the db"""
import datetime

#local imports
from app.api.v2.models.db import Db

class Incidents():
    def __init__(self, createdBy, incidence_type, location, comment):
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = 'Draft'
        self.createdBy = createdBy
        self.db_obj = Db()
        self.location = location
        self.comment = comment
        self.incidence_type = incidence_type

    def __repr__(self):
        return {
            'username':self.createdBy,
            'createdOn':self.createdOn,
            'status': self.status
        }

    def get_all_incidents_created_by_a_user(self):
        """gets all the incidences created by a user"""
        sql = "SELECT * FROM incidences WHERE users.createdBy=\'%s\' "%(self.createdBy)
        curr = Db().cur
        curr.execute(sql)
        output =curr.fetchall()
        return output

    def create_an_incident(self):
        """Registers a new incident to the database"""
        sql = "INSERT INTO incidences (createdOn,\
                                       createdBy,\
                                       type,\
                                       location,\
                                       status,\
                                       comment)\
                                VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%(
                                self.createdOn,
                                self.createdBy,
                                self.incidence_type,
                                self.location,
                                self.status,
                                self.comment
                                )
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit()
    
    def get_an_incident(self, id):
        sql = f"SELECT * FROM incidences WHERE incidences.id={id}"
        curr = self.db_obj.cur
        curr.execute(sql)
        output = curr.fetchone()
        return output

    def get_all_incidents(self):
        sql = f"SELECT * FROM incidences"
        curr = Db().cur
        curr.execute(sql)
        output = curr.fetchall()
        return output
    
    def update_comment(self, id, comment):
        sql=f"UPDATE  incidences SET comment = \'{comment}\'\
                                    WHERE incidences.id = {id}"
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit()

    def update_location(self, id, location):
        sql=f"UPDATE  incidences SET location = \'{location}\'\
                                    WHERE incidences.id = {id}"
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit()

    def update_status(self,id,status):
        sql=f"UPDATE incidences SET status = \'{status}\' WHERE incidences.id = {id}"
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit()

    def delete_incident(self,id):
        sql = f"DELETE FROM incidences WHERE incidences.id ={id}"
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit()
    