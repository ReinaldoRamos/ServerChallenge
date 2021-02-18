from app.model.Model import Server
import logging

from flask import flash


logger = logging.getLogger('flask.app')


class serverController():

    def find_all(self):
        try:
            return Server.query.all()
        except Exception as e:
            logger.error(e)
        finally:
            db.session.close()

    def find_one(self,server):
        try:
            return Server.query.get(Server)
        except Exception as e:
            logger.error(e)
        finally:
            db.session.close()


    def find_name(self, description):
        try:
            return Server.query.filter_by(description=description).first()
        except Exception as e:
            logger.error(e)

    def insert_server(self):
        try:
            server = Server()
            db.session.add(server)
            db.session.commit()

            return flash('Server added successfully.', 'success')
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            return flash('There was an error updating Server, check the informations or contact the administrator.', 'danger')
        finally:
            db.session.close()

    def update_server(self, server):
        try:
            server = Server.query.get(Server)
            db.session.commit()

            return flash('Server was successfully updated.', 'success')
        except Exception as e:
            db.session.rollback()
            logger.error(e)

            return flash('There was an error updating Server, check the informations or contact the administrator.', 'danger')
        finally:
            db.session.close()