from pydantic import BaseModel

class Request(BaseModel):
    N_Days: int = None
    Drug: int = None
    Age: int = None
    Sex: int = None
    Ascites: int = None
    Hepatomegaly: int = None
    Spiders: int = None
    Edema: int = None
    Bilirubin: float = None
    Cholesterol: float = None
    Albumin: float = None
    Copper: float = None
    Alk_Phos: float = None
    SGOT: float = None
    Tryglicerides: float = None
    Platelets: float = None
    Prothrombin: float = None
    Stage: float = None