from models import DBPatientModel, DBRiskScoreModel, DBLipidBiomarkersModel, DBPrimaryCarePlanModel, DBBiomarkerCarePlanModel
from Schema import ResponseRiskScoreModel, ResponseLipidBiomarkersModel
from Schema import PatientModel, RiskScoreModel, LipidBiomarkersModel, CarePlanModel
from src.components.careplan import CarePlan
from src.components.lipid_biomarkers import Lipid_Biomarkers
from src.components.risk_category import Risk_Category
from src.components.patient import Patient
from middleware import log_request_middleware
from exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import uvicorn
import os


load_dotenv(".env")

app = FastAPI()

app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError,
                          request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.post("/patient", response_model=PatientModel)
async def get_patient(patient_data: PatientModel):
    patient_data = Patient(
        mrn=patient_data.mrn,
        name=patient_data.name,
        age=patient_data.age,
        sex=patient_data.sex
    )
    db_patient = DBPatientModel(
        mrn=patient_data.mrn,
        name=patient_data.name,
        age=patient_data.age,
        sex=patient_data.sex
    )
    db.session.add(db_patient)
    db.session.commit()
    items = {
        "mrn": (patient_data.mrn),
        "name": (patient_data.name),
    }
    return JSONResponse(content=items)


@app.post("/ascvd_risk", response_model=ResponseRiskScoreModel)
async def get_ascvd_risk(ascvd_data: RiskScoreModel):
    risk_category = Risk_Category(
        ascvd_score=ascvd_data.ascvd_score,
    )

    careplan = CarePlan(
        actions=" ",
        medications=" ",
        rationale=" ",
        recommendations=" ",
        alternatives=" "
    )
    risk_category.cvd_risk()
    careplan.ascvd_careplan(risk_category)

    db_risk_category = DBRiskScoreModel(
        ascvd_score=ascvd_data.ascvd_score,
        ascvd_risk=risk_category.ascvd_risk
    )
    db_ascvd_careplan = DBPrimaryCarePlanModel(
        actions=careplan.actions,
        medications=careplan.medications,
        rationale=careplan.rationale,
        recommendations=careplan.recommendations,
        alternatives=careplan.alternatives
    )
    db.session.add(db_risk_category)
    db.session.add(db_ascvd_careplan)
    db.session.commit()
    items = {
        "ascvd_score": (risk_category.ascvd_score),
        "ascvd_risk": (risk_category.ascvd_risk),
        "actions": (careplan.actions),
        "medications": (careplan.medications),
        "rationale": (careplan.rationale),
        "recommendations": (careplan.recommendations),
        "alternatives": (careplan.alternatives)
    }
    return JSONResponse(content=items)


@app.post("/lipid_biomarkers", response_model=ResponseLipidBiomarkersModel)
async def get_lipid_biomarkers_risk(lipid_biomarkers_data: LipidBiomarkersModel):
    biomarkers_risk = Lipid_Biomarkers(
        hdl_c=lipid_biomarkers_data.hdl_c,
        ldl_c=lipid_biomarkers_data.ldl_c,
        lp_a=lipid_biomarkers_data.lp_a,
        triglycerides=lipid_biomarkers_data.triglycerides,
        apo_b=lipid_biomarkers_data.apo_b,
        apo_a1=lipid_biomarkers_data.apo_a1,
        hs_crp=lipid_biomarkers_data.hs_crp,
        units=lipid_biomarkers_data.units
    )
    careplan = CarePlan(
        actions="",
        medications="",
        rationale="",
        recommendations="",
        alternatives=""
    )

    biomarkers_risk.check_and_convert_units()
    biomarkers_risk.biomarker_risk()
    careplan.biomarker_careplan(biomarkers_risk)

    # Saving biomarkers risk to database
    db_biomarkers_risk = DBLipidBiomarkersModel(
        hdl_c=lipid_biomarkers_data.hdl_c,
        ldl_c=lipid_biomarkers_data.ldl_c,
        lp_a=lipid_biomarkers_data.lp_a,
        triglycerides=lipid_biomarkers_data.triglycerides,
        apo_b=lipid_biomarkers_data.apo_b,
        apo_a1=lipid_biomarkers_data.apo_a1,
        hs_crp=lipid_biomarkers_data.hs_crp,

        hdl_c_risk=biomarkers_risk.hdl_c_risk,
        ldl_c_risk=biomarkers_risk.ldl_c_risk,
        lp_a_risk=biomarkers_risk.lp_a_risk,
        triglycerides_risk=biomarkers_risk.triglycerides_risk,
        apo_b_risk=biomarkers_risk.apo_b_risk,
        apo_a1_risk=biomarkers_risk.apo_a1_risk,
        hs_crp_risk=biomarkers_risk.hs_crp_risk,
        units=biomarkers_risk.units
    )
    db_biomarker_careplan = DBBiomarkerCarePlanModel(
        actions=careplan.actions,
        medications=careplan.medications,
        rationale=careplan.rationale,
        recommendations=careplan.recommendations,
        alternatives=careplan.alternatives
    )

    db.session.add(db_biomarkers_risk)
    db.session.add(db_biomarker_careplan)
    db.session.commit()

    items = {
        "hdl_c_risk": (biomarkers_risk.hdl_c_risk),
        "ldl_c_risk": (biomarkers_risk.ldl_c_risk),
        "lp_a_risk": (biomarkers_risk.lp_a_risk),
        "triglycerides_risk": (biomarkers_risk.triglycerides_risk),
        "apo_b_risk": (biomarkers_risk.apo_b_risk),
        "apo_a1_risk": (biomarkers_risk.apo_a1_risk),
        "hs_crp_risk": (biomarkers_risk.hs_crp_risk),
        "units": (biomarkers_risk.units),
        "actions": (careplan.actions),
        "medications": (careplan.medications),
        "rationale": (careplan.rationale),
        "recommendations": (careplan.recommendations),
        "alternatives": (careplan.alternatives),
    }
    return JSONResponse(content=items)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0 ", port=8000)
