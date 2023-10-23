from dataclasses import dataclass


@dataclass
class Risk_Category:
    ascvd_score: float = None
    ascvd_risk: str = None

    def cvd_risk(self):
        if self.ascvd_score is not None:
            if self.ascvd_score >= 20:
                self.ascvd_risk = "High Risk"
            elif 7.5 <= self.ascvd_score < 20:
                self.ascvd_risk = "Borderline Risk"
            else:
                self.ascvd_risk = "Normal"
        else:
            # Setting ascvd_risk to None or any other default value if score not available
            self.ascvd_risk = None
