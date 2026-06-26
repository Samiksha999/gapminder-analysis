import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # no display needed
from pipeline import run_pipeline

def generate_charts():
    data = run_pipeline(2007)
    continents = [d["continent"] for d in data]
    life_exps = [d["avg_life_exp"] for d in data]
    gdps = [d["avg_gdp"] for d in data]

    # Chart 1 - Life Expectancy
    plt.figure(figsize=(10, 5))
    plt.bar(continents, life_exps, color="steelblue")
    plt.title("Average Life Expectancy by Continent (2007)")
    plt.ylabel("Life Expectancy (years)")
    plt.savefig("life_expectancy.png")
    plt.close()

    # Chart 2 - GDP
    plt.figure(figsize=(10, 5))
    plt.bar(continents, gdps, color="coral")
    plt.title("Average GDP per Capita by Continent (2007)")
    plt.ylabel("GDP per Capita (USD)")
    plt.savefig("gdp_per_capita.png")
    plt.close()

if __name__ == "__main__":
    generate_charts()
    print("Charts saved!")