from dataclasses import dataclass


@dataclass
class Lipid_Biomarkers:
    # Values of the Biomarkers
    hdl_c: float = None
    ldl_c: float = None
    lp_a: float = None
    triglycerides: float = None
    apo_b: float = None
    apo_a1: float = None
    hs_crp: float = None
    units: str = None
    # Risk Categories of the Biomarkers
    hdl_c_risk: str = None
    ldl_c_risk: str = None
    lp_a_risk: str = None
    triglycerides_risk: str = None
    apo_b_risk: str = None
    apo_a1_risk: str = None
    hs_crp_risk: str = None
    # Conversion factors for units
    conversion_factors = {
        "mmol/L to mg/dl": 38.67, }

    def convert_to_mgdl(self, value, conversion_factor):
        return value * conversion_factor

    def check_and_convert_units(self):
        if self.units == 'mmol/L':
            biomarker_conversion = {
                "hdl_c": "mmol/L to mg/dl",
                "ldl_c": "mmol/L to mg/dl",
                "lp_a": "mmol/L to mg/dl",
                "triglycerides": "mmol/L to mg/dl",
                "apo_b": "mmol/L to mg/dl",
                "apo_a1": "mmol/L to mg/dl",
                "hs_crp": "mmol/L to mg/dl",
            }
            for biomarker, conversion in biomarker_conversion.items():
                if getattr(self, biomarker) is not None:
                    if conversion in self.conversion_factors:
                        conversion_factor = self.conversion_factors[conversion]
                        setattr(self, biomarker, self.convert_to_mgdl(
                            getattr(self, biomarker), conversion_factor))


# Risk Categorization of the biomakers

    def biomarker_risk(self):
        ldl_range = (100, 160)
        hdl_range = (40, 50)
        triglycerides_range = (150, 200)
        lp_a_range = (30, 50)
        apo_b_range = (80, 120)
        apo_a1_range = (120, 160)
        hs_crp_range = (1.0, 3.0)

        if self.hdl_c is not None:
            if self.hdl_c >= hdl_range[1]:
                self.hdl_c_risk = "High Risk"
            elif hdl_range[0] <= self.hdl_c < hdl_range[1]:
                self.hdl_c_risk = "Borderline Risk"
            else:
                self.hdl_c_risk = "Normal"
        if self.ldl_c is not None:
            if self.ldl_c >= ldl_range[1]:
                self.ldl_c_risk = "High Risk"
            elif ldl_range[0] <= self.ldl_c < ldl_range[1]:
                self.ldl_c_risk = "Borderline Risk"
            else:
                self.ldl_c_risk = "Normal"
        if self.triglycerides is not None:
            if self.triglycerides >= triglycerides_range[1]:
                self.triglycerides_risk = "High Risk"
            elif triglycerides_range[0] <= self.triglycerides < triglycerides_range[1]:
                self.triglycerides_risk = "Borderline Risk"
            else:
                self.triglycerides_risk = "Normal"
        if self.lp_a is not None:
            if self.lp_a >= lp_a_range[1]:
                self.lp_a_risk = "High Risk"
            elif lp_a_range[0] <= self.lp_a < lp_a_range[1]:
                self.lp_a_risk = "Borderline Risk"
            else:
                self.lp_a_risk = "Normal"
        if self.apo_b is not None:
            if self.apo_b >= apo_b_range[1]:
                self.apo_b_risk = "High Risk"
            elif apo_b_range[0] <= self.apo_b < apo_b_range[1]:
                self.apo_b_risk = "Borderline Risk"
            else:
                self.apo_b_risk = "Normal"
        if self.apo_a1 is not None:
            if self.apo_a1 >= apo_a1_range[1]:
                self.apo_a1_risk = "High Risk"
            elif apo_a1_range[0] <= self.apo_a1 < apo_a1_range[1]:
                self.apo_a1_risk = "Borderline Risk"
            else:
                self.apo_a1_risk = "Normal"
        if self.hs_crp is not None:
            if self.hs_crp >= hs_crp_range[1]:
                self.hs_crp_risk = "High Risk"
            elif hs_crp_range[0] <= self.hs_crp < hs_crp_range[1]:
                self.hs_crp_risk = "Borderline Risk"
            else:
                self.hs_crp_risk = "Normal"
