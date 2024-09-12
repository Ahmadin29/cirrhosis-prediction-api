from fastapi import FastAPI, Request # type: ignore
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from helpers.request import Request as ModelRequest
import pandas as pd
from helpers.feature_engine import FeatureEngine
import joblib
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post("/predict")
async def predict(request: ModelRequest):

    basic_features = request.dict()
    feature_engine = FeatureEngine(basic_features)

    Bilirubin_Albumin_Ratio         = feature_engine.calculate_bilirubin_albumin_ratio()
    SGOT_Ratio                      = feature_engine.calculate_sgot_ratio()
    Copper_Albumin_Ratio            = feature_engine.calculate_copper_albumin_ratio()
    Platelets_Bilirubin_Ratio       = feature_engine.calculate_platelets_bilirubin_ratio()
    Tryglicerides_Albumin_Ratio     = feature_engine.calculate_troglicerides_albumin_ratio()
    Age_Category                    = feature_engine.calculate_age_category()
    Bilirubin_Category              = feature_engine.calculate_bilirubin_category()
    Albumin_Category                = feature_engine.calculate_albumin_category()
    Copper_Category                 = feature_engine.calculate_copper_category()
    Tryglicerides_Category          = feature_engine.calculate_tryglicerides_category()
    Platelets_Category              = feature_engine.calculate_platelets_category()
    Prothrombin_Category            = feature_engine.calculate_prothrombin_category()

    data_to_predict = {
        **basic_features,
        "Bilirubin_Albumin_Ratio": Bilirubin_Albumin_Ratio,
        "SGOT_Ratio": SGOT_Ratio,
        "Copper_Albumin_Ratio": Copper_Albumin_Ratio,
        "Platelets_Bilirubin_Ratio": Platelets_Bilirubin_Ratio,
        "Tryglicerides_Albumin_Ratio": Tryglicerides_Albumin_Ratio,
        "Age_Category": Age_Category,
        "Bilirubin_Category": Bilirubin_Category,
        "Albumin_Category": Albumin_Category,
        "Copper_Category": Copper_Category,
        "Tryglicerides_Category": Tryglicerides_Category,
        "Platelets_Category": Platelets_Category,
        "Prothrombin_Category": Prothrombin_Category
    }

    dataframe_to_predict = pd.DataFrame([data_to_predict])
    model = joblib.load('./models/xgb_best.pkl')
    prediction = model.predict(dataframe_to_predict)

    return {
        "status":"success",
        "message":"Prediction Successful",
        "prediction":prediction.tolist(),
        "data":{
            **basic_features,
            "Bilirubin_Albumin_Ratio": Bilirubin_Albumin_Ratio,
            "SGOT_Ratio": SGOT_Ratio,
            "Copper_Albumin_Ratio": Copper_Albumin_Ratio,
            "Platelets_Bilirubin_Ratio": Platelets_Bilirubin_Ratio,
            "Tryglicerides_Albumin_Ratio": Tryglicerides_Albumin_Ratio,
            "Age_Category": Age_Category,
            "Bilirubin_Category": Bilirubin_Category,
            "Albumin_Category": Albumin_Category,
            "Copper_Category": Copper_Category,
            "Tryglicerides_Category": Tryglicerides_Category,
            "Platelets_Category": Platelets_Category,
            "Prothrombin_Category": Prothrombin_Category
        }
    }