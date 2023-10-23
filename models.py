from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class DBPatientModel(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    mrn = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String(10), nullable=False)


class DBRiskScoreModel(Base):
    __tablename__ = 'risk_scores'
    id = Column(Integer, primary_key=True)
    ascvd_score = Column(Float, nullable=True)
    ascvd_risk = Column(String(20), nullable=True)

    date_created = Column(DateTime(
        timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())

    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship(
        "DBPatientModel", backref="risk_scores", uselist=False)


class DBLipidBiomarkersModel(Base):
    __tablename__ = 'lipid_biomarkers'
    id = Column(Integer, primary_key=True)
    hdl_c = Column(Float, nullable=True)
    ldl_c = Column(Float, nullable=True)
    lp_a = Column(Float, nullable=True)
    triglycerides = Column(Float, nullable=True)
    apo_b = Column(Float, nullable=True)
    apo_a1 = Column(Float, nullable=True)
    hs_crp = Column(Float, nullable=True)
    units = Column(String(10), nullable=True)

    hdl_c_risk = Column(String(20), nullable=True)
    ldl_c_risk = Column(String(20), nullable=True)
    lp_a_risk = Column(String(20), nullable=True)
    triglycerides_risk = Column(String(20), nullable=True)
    apo_b_risk = Column(String(20), nullable=True)
    apo_a1_risk = Column(String(20), nullable=True)
    hs_crp_risk = Column(String(20), nullable=True)

    date_created = Column(DateTime(
        timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())

    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship(
        "DBPatientModel", backref="lipid_biomarkers", uselist=False)


class DBPrimaryCarePlanModel(Base):
    __tablename__ = 'ascvd_careplans'
    id = Column(Integer, primary_key=True)
    actions = Column(String(500), nullable=True)
    medications = Column(String(500), nullable=True)
    rationale = Column(String(500), nullable=True)
    recommendations = Column(String(500), nullable=True)
    alternatives = Column(String(500), nullable=True)

    date_created = Column(DateTime(
        timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())

    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship(
        "DBPatientModel", backref="ascvd_careplans", uselist=False)


class DBBiomarkerCarePlanModel(Base):
    __tablename__ = 'biomarker_careplans'
    id = Column(Integer, primary_key=True)
    actions = Column(String(1000), nullable=True)
    medications = Column(String(1000), nullable=True)
    rationale = Column(String(1000), nullable=True)
    recommendations = Column(String(1000), nullable=True)
    alternatives = Column(String(1000), nullable=True)

    date_created = Column(DateTime(
        timezone=True), server_default=func.now())
    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship(
        "DBPatientModel", backref="biomarker_careplans", uselist=False)
