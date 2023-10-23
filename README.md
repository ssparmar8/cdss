# CDSS_Labs

- This is a CVD risk interpreter based on the ASCVD risk score and CVD lab results of a Patient.
  The application is built using Python, FastAPI and Postgresql database. The end points accept patient's data and has following fields:

1. MRN: Medical Record Number
2. Name of the Patient
3. Age of the patient
4. Sex of the patient

- It accepts the ASCVD Risk score of the patient and a primary careplan is generated based on the risk score,

5. Ascvd risk

- The primary care plan includes,
  Actions: Directive Actions to be taken for writing prescriptions
  Medications: Decision support for Medicines, In order to which to target and modifications to be done
  Rationale: rationale for the recommendations
  Recommendations: lifestyle and treatment changes
  Alternatives: Alternative medications/Lifestyle modifications to be considered

It accepts the Biomarkers of the patient and a Biomarker careplan is generated based on the biomarker risk category,
-List of Biomarkers accepted:

1. hdl cholesterol
2. ldl cholesterol
3. lipoprotein-a (lp(a))
4. apolipoprotein-b(apob)
5. triglycerides
6. high-sensitivity c-reactive protein
7. units: mg/dl

- The application includes a method to check and convert the units from mmol/L to mg/dl if needed.

- The biomarker care plan includes,
  Actions: Directive Actions to be taken for writing prescriptions
  Medications: Decision support for Medicines, In order to which to target and modifications to be done
  Rationale: rationale for the recommendations
  Recommendations: lifestyle and treatment changes
  Alternatives: Alternative medications/Lifestyle modifications to be considered

- This FastAPI application contains the following endpoints:

1. POST /patient

URL: /patient
HTTP Method: POST
Request Model: PatientModel
Response Model: PatientModel
Description: This endpoint is used to create a new patient record. It expects a JSON request with patient details including MRN (Medical Record Number), name, age, and sex. It then stores the patient data in the database and returns the created patient's details as a response.
POST /ascvd_risk

2. URL: /ascvd_risk
   HTTP Method: POST
   Request Model: RiskScoreModel
   Response Model: ResponseRiskScoreModel
   Description: This endpoint calculates and stores the ASCVD (Atherosclerotic Cardiovascular Disease) risk score for a patient. It takes the ASCVD score as input, calculates the risk category, and generates a care plan. The risk score and care plan are then stored in the database, and the response includes the calculated risk score and category.
   POST /lipid_biomarkers

3. URL: /lipid_biomarkers
   HTTP Method: POST
   Request Model: LipidBiomarkersModel
   Response Model: ResponseLipidBiomarkersModel
   Description: This endpoint receives lipid biomarker data, including HDL-C, LDL-C, LP(a), triglycerides, Apo B, Apo A1, hs-CRP, and units. It calculates risk categories for each biomarker, generates a care plan, and stores both the biomarker data and care plan in the database. The response includes the calculated risk categories.
   These endpoints handle different aspects of patient data, cardiovascular risk calculation, and lipid biomarker analysis, allowing users to interact with the application by submitting data and receiving calculated results and care plans. The application also includes exception handling for request validation errors, HTTP exceptions, and unhandled exceptions, ensuring robust error handling.

### Prerequisites

Ensure you have Docker installed on your system.

### Building the Docker Image

1. Open a terminal or command prompt.
2. Navigate to the root directory of your project, where the `Dockerfile` and `docker-compose.yml` files are located.
3. Run the following command to build the Docker image:
   -docker-compose build
   -docker-compose up
4. for postgresql database:
   -docker-compose run app alembic revision --autogenerate -m "New Migration"
   -docker-compose run app alembic upgrade head

### Database Connection Details:

You will need the following details to connect to your PostgreSQL database:

URL (Database Connection URL): postgresql+psycopg2://postgres:password@db:5432/labs
Database Username: postgres
Database Password: password
Database Name: labs

PGadmin username: admin@admin.com
Password: password
