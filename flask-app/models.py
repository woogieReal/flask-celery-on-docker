from database import Base
from sqlalchemy import Column, DateTime, String, func, DateTime, Text
import uuid

class APILog(Base):
    __tablename__ = 'api_log'
    
    log_id = Column(String(36), primary_key=True, default=(lambda: uuid.uuid4()))
    api_request = Column(Text, nullable=False)
    api_response = Column(Text, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    
    def __repr__(self):
        return (f"<APILog(log_id='{self.log_id}', "
                f"api_request='{self.api_request}', "
                f"api_response='{self.api_response}', "
                f"creation_date='{self.creation_date}')>")
