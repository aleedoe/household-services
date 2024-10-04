from . import db, datetime

class ServiceRequest(db.Model):
    __tablename__ = 'service_request'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('service_professional.id'), nullable=True)
    date_of_request = db.Column(db.DateTime, default=datetime.now)
    date_of_request = db.Column(db.DateTime, default=datetime.now)
    date_of_completion = db.Column(db.DateTime, nullable=True)
    service_status = db.Column(db.String(50), nullable=False)  # e.g., requested, assigned, closed
    remarks = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    
    customer = db.relationship('Customer', backref='service_request')
    service = db.relationship('Service', backref='service_request')
    professional = db.relationship('ServiceProfessional', backref='service_request')
    
    def __repr__(self):
        return f'<ServiceRequest {self.id}>'