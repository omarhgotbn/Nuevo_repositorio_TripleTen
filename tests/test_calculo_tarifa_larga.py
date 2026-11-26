def test_calculo_tarifa_larga():
    distancia = 15
    tarifa_por_km = 3

    tarifa_total = distancia * tarifa_por_km
    assert tarifa_total == 45