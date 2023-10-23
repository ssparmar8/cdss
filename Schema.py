from pydantic import BaseModel
from typing import Optional


class PatientModel(BaseModel):
    mrn: int
    name: str
    age: int
    sex: str


class RiskScoreModel(BaseModel):
    ascvd_score: float = None


class ResponseRiskScoreModel(BaseModel):
    ascvd_score: float
    ascvd_risk: str


class LipidBiomarkersModel(BaseModel):
    id: Optional[int] = None
    hdl_c: float = None
    ldl_c: float = None
    lp_a: float = None
    triglycerides: float = None
    apo_b: float = None
    apo_a1: float = None
    hs_crp: float = None
    units: str = None


class ResponseLipidBiomarkersModel(BaseModel):
    hdl_c_risk: str
    ldl_c_risk: str
    lp_a_risk: str
    triglycerides_risk: str
    apo_b_risk: str
    apo_a1_risk: str
    hs_crp_risk: str
    units: str


class CarePlanModel(BaseModel):
    id: Optional[int] = None
    actions: str = None
    medications: str = None
    rationale: str = None
    recommendations: str = None
    alternatives: str = None
