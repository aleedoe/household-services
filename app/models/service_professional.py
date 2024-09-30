from . import db, datetime


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
    created_at = db.Column(db.DateTime, default=datetime(utcnow=True))

    service = db.relationship('Service', backref='service_professional')

    def __repr__(self):
        return f'<ServiceProfessional {self.username}>'