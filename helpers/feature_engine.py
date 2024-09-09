# Bilirubin_Albumin_Ratio = None
# SGOT_Ratio = None
# Copper_Albumin_Ratio = None
# Platelets_Bilirubin_Ratio = None
# Tryglicerides_Albumin_Ratio = None
# Age_Category = None
# Bilirubin_Category = None
# Albumin_Category = None
# Copper_Category = None
# Tryglicerides_Category = None
# Platelets_Category = None
# Prothrombin_Category = None

class FeatureEngine:
    def __init__(self, basic_features):
        self.data = basic_features

    def calculate_bilirubin_albumin_ratio(self):
        return self.data["Bilirubin"] / self.data["Albumin"]
    
    def calculate_sgot_ratio(self):
        return self.data["SGOT"] / self.data["Alk_Phos"]
    
    def calculate_copper_albumin_ratio(self):
        return self.data["Copper"] / self.data["Albumin"]
    
    def calculate_platelets_bilirubin_ratio(self):
        return self.data["Platelets"] / self.data["Bilirubin"]
    
    def calculate_troglicerides_albumin_ratio(self):
        return self.data["Tryglicerides"] / self.data["Albumin"]
    
    def calculate_age_category(self):
        if self.data['Age'] <= 30:
            return 1
        elif self.data['Age'] <= 50:
            return 2
        else:
            return 3
        
    def calculate_bilirubin_category(self):
        if 0.3 <= self.data['Bilirubin'] <= 1.2:
            return 0
        elif self.data['Bilirubin'] > 1.2:
            return 1
        else:
            return 0
        
    def calculate_albumin_category(self):
        if 3.5 < self.data['Albumin'] <= 5:
            return 0
        elif self.data['Albumin'] <= 3.5:
            return 1
        else:
            return 0
        
    def calculate_copper_category(self):
        if 70 < self.data['Copper'] <= 140:
            return 0
        elif self.data['Copper'] <= 70 or self.data['Copper'] > 140:
            return 1
        else:
            return 0
        
    def calculate_troglicerides_category(self):
        if self.data['Tryglicerides'] <= 150:
            return 0
        elif self.data['Tryglicerides'] > 150:
            return 1
        else:
            return 0
        
    def calculate_platelets_category(self):
        if 150 < self.data['Platelets'] <= 450:
            return 0
        elif self.data['Platelets'] <= 150 or self.data['Platelets'] > 450:
            return 1
        else:
            return 0
        
    def calculate_prothrombin_category(self):
        if 11 <= self.data['Prothrombin'] <= 13.5:
            return 0
        elif self.data['Prothrombin'] < 11 or self.data['Prothrombin'] > 13.5:
            return 1
        else:
            return 0