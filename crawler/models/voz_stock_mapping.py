from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String, create_engine
from sqlalchemy.orm import relationship
from crawler.models.voz_rawcomment import VOZRawComment
from crawler.utils.model import Base


class VOZStockMapping(Base):
    __tablename__ = 'voz_stockmapping'
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock = Column(String)
    spider_id = Column(Integer, ForeignKey(
        'voz_spider.id', ondelete='cascade'), nullable=False)
    voz_commentid = Column(String, ForeignKey(
        'voz_rawcomment.id', ondelete='cascade'), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    time = Column(DateTime)
    voz_comment = relationship(VOZRawComment)
