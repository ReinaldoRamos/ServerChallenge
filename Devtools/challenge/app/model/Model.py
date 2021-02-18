from flask import Flask
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.pool import NullPool


from datetime import datetime

import os
import sys

script_dir = os.path.dirname('../../')

sys.path.append(script_dir)
from app.model.config import app

class SQLAlchemy(SQLAlchemyBase):
    def apply_driver_hacks(self, app, info, options):
        super(SQLAlchemy, self).apply_driver_hacks(app, info, options)
        options['poolclass'] = NullPool
        options.pop('pool_size', None)

db = SQLAlchemy(app, session_options={"autoflush": True, "expire_on_commit":True})

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Server(db.Model):
    __tablename__ = 'server'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    server_type = db.Column(db.String, nullable=False)
    alerts = db.relationship('Alert', backref='server', lazy=True)

    def get_server(self):
        return self.server

class Alert(db.Model):
    __tablename__ = 'alert'

    alert = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    server_type = db.Column(db.String, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=False)


if __name__ == '__main__':
    import os
    dirname = os.path.dirname(__file__)
    manager.run()
