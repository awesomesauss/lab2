import Lab2 as lab2
import statistics as stats

def test_find_min_max():
    result = []
    inar = [3,1,4,5]

    result = lab2.calc_min_max_temperature(inar)

    assert result == [1,5]


def test_calc_average():
    inar = [3,4,1,2,3]
    result = lab2.calc_average_temperature(inar)
    assert result == 2.6


def test_calc_median_temperature():
    inar = [3,123,412321,421321421]
    result = lab2.calc_median_temperature(inar)
    assert result == stats.median(inar)