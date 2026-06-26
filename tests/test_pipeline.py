from pipeline import run_pipeline

def test_pipeline_returns_5_continents():
    results = run_pipeline(2007)
    assert len(results) == 5

def test_pipeline_has_correct_keys():
    results = run_pipeline(2007)
    keys = results[0].keys()
    assert "continent" in keys
    assert "avg_life_exp" in keys
    assert "avg_gdp" in keys
    assert "total_pop" in keys

def test_different_year():
    results = run_pipeline(1952)
    assert len(results) == 5