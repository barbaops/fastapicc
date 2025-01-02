from sqlalchemy import Column, String, Boolean
from app.database import Base

class Bucket(Base):
    __tablename__ = "buckets"

    id = Column(String, primary_key=True)  # Identificador único do bucket
    bucket_name = Column(String, nullable=False)  # Nome do bucket
    region = Column(String, nullable=False)  # Região AWS
    acl = Column(String, default="private")  # Controle de acesso
    storage_class = Column(String, default="STANDARD")  # Classe de armazenamento
    enable_versioning = Column(Boolean, default=False)  # Versionamento habilitado
