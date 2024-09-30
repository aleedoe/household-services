from . import db, datetime

class Review(db.Model):
    __tablename__ = 'review'
    
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('service_professional.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    comments = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime(utcnow=True))
    
    service_request = db.relationship('ServiceRequest', backref='review')
    customer = db.relationship('Customer', backref='review')
    professional = db.relationship('ServiceProfessional', backref='review')
    
    def __repr__(self):
        return f'<Review {self.id}>'