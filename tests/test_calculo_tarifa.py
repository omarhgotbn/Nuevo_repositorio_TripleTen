def test_calculo_tarifa():
    distancia=10
    tarifa_por_km=2

    tarifa_total= distancia * tarifa_por_km

    assert tarifa_total == 20

def test_calculo_tarifa():
    distancia=15
    tarifa_por_km=4

    tarifa_total= distancia * tarifa_por_km

    assert tarifa_total == 60