from . import db, datetime
from werkzeug.security import generate_password_hash, check_password_hash


class ServiceProfessional(db.Model):
    __tablename__ = 'service_professional'
    
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    experience = db.Column(db.Integer, nullable=False)  # in years
    verified_status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    service = db.relationship('Service', backref='service_professional')

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<ServiceProfessional {self.username}>'