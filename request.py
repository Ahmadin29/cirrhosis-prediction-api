from pydantic import BaseModel

class Request(BaseModel):
    N_Days: int = None
    Drug: str = None
    Age: int = None
    Sex: str = None
    Ascites: str = None
    Hepatomegaly: str = None
    Spiders: str = None
    Edema: str = None
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