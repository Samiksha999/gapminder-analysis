from fastapi import FastAPI
from pipeline import run_pipeline
from ml_model import predict_life_exp

app = FastAPI(title="Gapminder Analysis API")

@app.get("/")
def root():
    return {"message": "Gapminder Analysis API is running!"}

@app.get("/analysis")
def get_analysis(year: int = 2007):
    results = run_pipeline(year=year)
    return {"year": year, "data": results}

@app.get("/continents")
def get_continents():
    all_years = [1952, 1957, 1962, 1967, 1972, 1977,
                 1982, 1987, 1992, 1997, 2002, 2007]
    return {"available_years": all_years}

@app.get("/predict")
def predict(gdp_per_cap: float):
    life_exp = predict_life_exp(gdp_per_cap)
    return {
        "gdp_per_capita": gdp_per_cap,
        "predicted_life_expectancy": life_exp
    }