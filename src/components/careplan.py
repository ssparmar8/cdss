from dataclasses import dataclass


@dataclass
class CarePlan:
    actions: str
    medications: str
    rationale: str
    recommendations: str
    alternatives: str

    def ascvd_careplan(self, risk):
        if risk.ascvd_risk == 'High Risk':
            self.actions = "Consider lipid Screening annually if not on statin therapy\n For patients with type 2 diabetes at high risk of ASCVD or with heart failure or chronic kidney disease,consider use of SGLT2 inhibitor after metformin to reduce cardiorenal events"
            self.medications = " Initiate on moderate-intensity statins, defined as those lowering LDL cholesterol by an average of 30–49%.\nPatients with questionable ability to tolerate moderate-intensity statins—the frail/age over 75, those taking interacting drugs, and those with hepatic/renal impairment or untreated hypothyroidism—should be initiated on reduced doses.\nPatients with a history of statin intolerance should be rechallenged with a statin, preferably a different one, at a reduced dose."
            self.rationale = "Individuals with a calculated ASCVD risk exceeding 20 percent over a decade face significantly higher chances of experiencing cardiovascular events, warranting proactive interventions to mitigate these risks and improve long-term health outcomes."
            self.recommendations = "Lifestyle modifications are crucial:\nThe American Heart Association recommends the following physical activity goals:\nAt least 30 minutes of moderate-intensity aerobic activity 5 or more days per week.\nModerate- to high-intensity muscle-strengthening activity 2 or more days per week.\nWeight loss through an appropriate balance of caloric intake and adopting an anti-inflammatory diet, such as the Mediterranean diet, can lower hs-CRP levels."
            self.alternatives = "Apart from statins, aspirin possesses anti-inflammatory properties and may reduce hs-CRP levels, but the overall risk-benefit profile must be considered.\nAngiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) could also impact inflammation and potentially lower hs-CRP."

        elif risk.ascvd_risk == 'Borderline Risk':
            self.actions = "Consider Annual cardiovascular risk assessment and lipid screening every 2 years.\n Encourage lifestyle modifications: dietary improvements, regular exercise, and smoking cessation"
            self.medications = "Consider moderate-intensity statins for individuals with additional risk factors (e.g., family history, high LDL levels)\nEvaluate potential drug interactions and comorbidities"
            self.rationale = "While the ASCVD risk is moderate, proactive measures are vital to prevent future cardiovascular events. Lifestyle changes and statin therapy can help lower risk and improve long-term health."
            self.recommendations = "Promote heart-healthy behaviors:\nBalanced diet, low in saturated and trans fats\nAim for at least 150 minutes of moderate-intensity aerobic exercise per week\nSmoking cessation support\nRegular blood pressure and blood sugar monitoring"
            self.alternatives = "Consider aspirin therapy in select cases after assessing bleeding risk\nEvaluate other lipid-lowering medications, such as ezetimibe, based on individual patient factors"

        else:
            self.actions = "For low-risk individuals, prioritize heart-healthy lifestyle measures.\nRoutine lipid screening not recommended unless additional major risk factors are present(e.g., diabetes, hypertension,family history, or smoking)."
            self.medications = "Statin therapy is generally not indicated for low-risk individuals with an ASCVD risk score below 7.5%."
            self.rationale = "The AHA guidelines emphasize the importance of lifestyle modifications as the primary strategy for individuals with low ASCVD risk, while statin therapy is not typically recommended in this category."
            self.recommendations = "Promote heart-healthy behaviors:\n- Balanced diet\n- Regular exercise\n- Smoking cessation\n- Blood pressure and blood sugar monitoring as needed"
            self.alternatives = "For specific cases, consider aspirin therapy or other interventions based on individual risk factors, but exercise caution and assess the risk-benefit profile carefully."

    def biomarker_careplan(self, biomarkers):
        if biomarkers.lp_a_risk == 'High Risk' or biomarkers.lp_a_risk == 'Borderline Risk':
            self.actions = "Focus on Raising HDL,\n In high risk patients unresponsive to efforts to raise HDL consider lowering [LDL]"
            self.medications = "Niacin,\n PCSK9i,\n Estrogen,\n Aspirin,\n T3/T4,\n Omega-3FAs,\n EtOH CoEnzyme-Q10,\n Quercetin Vit-D3"
            self.rationale = "Lipoprotein[a] a.k.a. Lp(a) is The most atherogenic of the ApoB particles. It is entirely gentic/inherired; it does NOT respond to diet & exercise; statins can increase it from 11% to as much as ~75%, especially when it is severely elevated.\nVery few agents/therapies have any efficacy to lower it.\nNiacin is the best studied & can reduce it by 20% to ~80%, in the absence of statin therapy.\nThyroid supplementation is nearly as eefective as niacin.\n No currently approved Rx is available & traditionally, only niacin has been used to successfully decrease it. \nInterestingly, statins are ApoB drugs & since they increase Lp(a) [o benefit & evidence risk is increased], the only current, rationale option is a lowest-dose statin PLUS niacin &/or T4 [with/without T3]."
            self.recommendations = "If patient is an African-American no treatment needed,\n Thyroid hormone replacement to normalize TSH if hypothyroid,\n ACE/ARB therapy in diabetics with microalbuminuria / proteinuria\nrestriction of dietary trans-fatty acids"
            self.alternatives = "Alternative approach to lowering [Lp(a)] is to lower the [LDL] below current NCEP guidelines.\n Lp(a) loses predictive value if [LDL]<70 mg%\n If the patient is on a statin consider the use of rosuvastatin, simvastatin or pravastatin which do not raise Lp(a)"

        elif biomarkers.apo_b_risk == 'High Risk' or biomarkers.apo_b_risk == 'Borderline Risk':
            self.actions = "ApoB is elevated, 'particle- specific' therapy should be initiated."
            self.medications = "Niacin [Potent PCSK9 inhibitor],\n L-Thyroxine (T4),\n [Potent PCSK9 inhibitor],\n Triiodothyronine (T3),\n [Potent PCSK9 inhibitor],\n Glitazones-TZD’s (some),\n Omega 3 fatty acids,\n Fibrates"
            self.rationale = "ApoB is the 'Gold-Standard' measure of atherogenic particles. All subspecies are captured in one measurement: Chylomicrons; VLDL1, 2 &3; IDL, LDL * Lp(a). each paticle carries one ApoB protein, so this is the most accuarte assessment. It is superior to ALL measures of Cholesterol: LDL, Non-HDL. Equal decreases result in 20-30 percent greater risk reduction: EXAMP: 42 percent decrease in; LDL = 32% RRR, the same decreases in Non- HDl & ApoB = RRR's of 32% & 39%."
            self.recommendations = "Exercise Regularly,\n Follow a low carbohydrate diet"
            self.alternatives = "dietary modifications, reducing saturated fats."

        elif biomarkers.triglycerides_risk == 'High Risk' or biomarkers.triglycerides_risk == 'Borderline Risk':
            self.actions = "Reduce carb intake, exercise regularly, decrease weight. Consider optimizing control of A1C, FBG & PPG. Rule out SCH, & treat if present."
            self.medications = "Ranked by Efficacy:\n Niacin,\n T3 / T4,\n Fibrates,\n Insulin,\n Omega-3-FAs,\n Low carbohydrate diet"
            self.rationale = "TG's/TRIGS/TriGlycerides a.k.a. TriAcylGlycerols are a storage form of diglycerides generated in the intestine, mainly from excess dietary carbohydrates.\nExcess FFA's/Free Fatty Acids are absorbed from the serum & assembled into TG's by the liver & either used to construct LDL- Particels or when in excess stored in central adipose 'FAT' cells.\nElevated fasting measures often reflect overabundance of FFA's & excess carbohydrtae intake. Furthermore, this also reflects abnormal glucose levels, especially in the post-prandial state [after meals]."
            self.recommendations = "Lifestyle/Diet/non-pharmacological intervention: Diet with additional carbohydrate restriction & alcohol avoidance. If overweight target 5 to 10 percent reduction in body weight"
            self.alternatives = "Addressing underlying conditions like diabetes is crucial.\nEmerging therapies like ANGPTL3 inhibitors show promise but require more research."

        elif biomarkers.apo_a1_risk == 'High risk' or biomarkers.apo_a1_risk == 'Borderline risk':
            self.actions = "Reduce carb intake, exercise regularly, decrease weight. Consider optimizing control of A1C, FBG & PPG. Rule out SCH, & treat if present."
            self.medications = "Niacin 1-4 g/day\n Triiodothyronine (T3) [Potent PCSK9 inhibitor\n Glitazones-TZD’s (some)\n Fenoﬁbrate 160 mg qD with food,\n Gemﬁbrozil 600 mg bid"
            self.rationale = "Apo-A1 is now the most reliable indicator of anti-atherogenic particles, also known as HDL.\n It combines quantity and quality into a single measurement.\n Apolipoprotein A1 is found in the best functioning species of HDLs, however it is present in ALL HDLs.\n It outperforms all cholesterol and apolipoprotein measures/ratios when employed in the interheart ratio."
            self.recommendations = "Lifestyle/Diet/non-pharmacological intervention: NCEP TLC diet with additional carbohydrate restriction & alcohol avoidance. If overweight, target 5 to 10 percent reduction in body weight"
            self.alternatives = "Omega-3-fa 4-12 g/day"

        elif biomarkers.ldl_c_risk == 'High risk' or biomarkers.ldl_c_risk == 'Borderline risk':
            self.actions = "LDL-C is extremely elevated, particle-specific therapy should be initiated. Do not focus on LDL-C ONLY. Effective reduction of ApoB will achieve the lowest LDL-C."
            self.medications = "Statins,\n Statins + ezetimibe,\n Bile Acid Sequestrants [BAS/Resins],\n Estrogen replacement therapy,\n Antiretrovirals (some),\n High carbohydrate diet"
            self.rationale = "LDL-C is a cholesterol measure. It is NOT a measure of LDL-Particles.\n It varies greatly based on several of factors. Whether directly maesured, or calculated, it merely 'reflects' the volume based on density taken up by the cholesterol within the particles in that density range.\nIt is HIGHLY discordant with ApoB [~50%] & it correlates poorly with risk & the performace of treatments."
            self.recommendations = "If the Risk is high, Target triglycerides < 100mg/dl with aggressive diet.\nIf diet unsuccessful Consider speciﬁc drug therapy to shift LDL density.\nIf unable to shift LDL density consider lowering target [LDL] to <70mg/dl\nIf the Risk is Low consider Lifestyle/Diet/non-pharmacological intervention"
            self.alternatives = "Alternate Medication:\n fenoﬁbrate 160 mg qD &/or niacin 1-4 g/day &/or Ω-3- fatty acids 4-12 g/day"

        elif biomarkers.hs_crp_risk == 'High Risk' or biomarkers.hs_crp_risk == 'Borderline Risk':
            self.actions = "High-sensitivity C-reactive protein (hs-CRP) is a biomarker of inflammation associated with cardiovascular disease (CVD) risk assessment."
            self.medications = "Statins,\n Statins + ezetimibe"
            self.rationale = "Elevated hs-CRP levels indicate systemic inflammation, which plays a role in atherosclerosis progression and plaque instability.\n Addressing inflammation, along with lipid management, is crucial for comprehensive CVD prevention."
            self.recommendations = "Lifestyle modifications are crucial:\nWeight loss, regular exercise, and adopting an anti-inflammatory diet, such as the Mediterranean diet, can lower hs-CRP levels.\n These measures contribute to overall CVD risk reduction."
            self.alternatives = "Apart from statins, aspirin possesses anti-inflammatory properties and may reduce hs-CRP levels, but the overall risk-benefit profile must be considered.\n Angiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) could also impact inflammation and potentially lower hs-CRP."

        elif biomarkers.hdl_c_risk == 'High risk' or biomarkers.hdl_c_risk == 'Borderline risk':
            self.actions = "Target [total HDL] > 45 mg/dl in men / >55 mg/dl in women"
            self.medications = "Niacin 1 to 2 g/day"
            self.rationale = "HDL cholesterol serves as a protective factor against cardiovascular diseases by promoting the removal of excess cholesterol, reducing inflammation and oxidative stress, improving blood vessel function, and inhibiting clot formation."
            self.recommendations = "Lifestyle interventions: Aerobic exercise and Smoking cessation"
            self.alternatives = "Rosuvastatin 10 mg qD,\n Simvastatin 40 or 80 mg qD,\n Fenoﬁbrate 160 mg qD,\n In high risk patients unresponsive to efforts to raise HDL consider lowering [LDL] to below NCEP target"
