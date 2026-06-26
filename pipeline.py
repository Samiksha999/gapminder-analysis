import pandas as pd
from gapminder import gapminder
from concurrent.futures import ThreadPoolExecutor

def analyze_continent(args):
    continent, group = args
    return {
        "continent": continent,
        "avg_life_exp": round(group["lifeExp"].mean(), 2),
        "avg_gdp": round(group["gdpPercap"].mean(), 2),
        "total_pop": int(group["pop"].sum())
    }

def run_pipeline(year=2007):
    df = gapminder[gapminder["year"] == year]
    groups = list(df.groupby("continent"))
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(analyze_continent, groups))
    return results

if __name__ == "__main__":
    data = run_pipeline()
    for item in data:
        print(item)