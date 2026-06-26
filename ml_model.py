import numpy as np
from gapminder import gapminder
from sklearn.linear_model import LinearRegression

def train_model():
    df = gapminder[["gdpPercap", "lifeExp"]].dropna()
    X = np.log(df[["gdpPercap"]])  # log scale for GDP
    y = df["lifeExp"]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_life_exp(gdp_per_cap: float):
    model = train_model()
    X_input = np.log([[gdp_per_cap]])
    prediction = model.predict(X_input)[0]
    return round(float(prediction), 2)

if __name__ == "__main__":
    print(predict_life_exp(5000))
    print(predict_life_exp(40000))