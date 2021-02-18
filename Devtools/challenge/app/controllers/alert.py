from app.model.Model import Alert
import logging

from flask import flash


logger = logging.getLogger('flask.app')


class alertController():

    def find_all(self):
        try:
            return Alert.query.all()
        except Exception as e:
            logger.error(e)
        finally:
            db.session.close()

    def find_one(self,server):
        try:
            return Alert.query.get(Alert)
        except Exception as e:
            logger.error(e)
        finally:
            db.session.close()


    def find_name(self, description):
        try:
            return Alert.query.filter_by(description=description).first()
        except Exception as e:
            logger.error(e)

    def insert_alert(self):
        try:
            alert = Alert()
            db.session.add(alert)
            db.session.commit()

            return flash('Alert added successfully.', 'success')
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            return flash('There was an error updating Alert, check the informations or contact the administrator.', 'danger')
        finally:
            db.session.close()

    def update_alert(self, alert):
        try:
            server = Alert.query.get(Alert)
            db.session.commit()

            return flash('Alert was successfully updated.', 'success')
        except Exception as e:
            db.session.rollback()
            logger.error(e)

            return flash('There was an error updating Alert, check the informations or contact the administrator.', 'danger')
        finally:
            db.session.close()