from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(998.2000000, 9.8066500, 0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(998.2000000, 9.8066500, 30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(998.2000000, 9.8066500, 50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 998.2000000, 0.018, 1.75) == approx(0.000, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 998.2000000, 0.000, 1.75) == approx(0.000, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 998.2000000, 0.018, 0.00) == approx(0.000, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 998.2000000, 0.018, 1.75) == approx(-113.008, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 998.2000000, 0.018, 1.65) == approx(-100.462, 0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 998.2000000, 0.013, 1.65) == approx(-61.576, 0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 998.2000000, 0.013, 1.65) == approx(-110.884, 0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(998.2000000, 0.00, 3) == approx(0.000, 0.001)
    assert pressure_loss_from_fittings(998.2000000, 1.65, 0) == approx(0.000, 0.001)
    assert pressure_loss_from_fittings(998.2000000, 1.65, 2) == approx(-0.109, 0.001)
    assert pressure_loss_from_fittings(998.2000000, 1.75, 2) == approx(-0.122, 0.001)
    assert pressure_loss_from_fittings(998.2000000, 1.75, 5) == approx(-0.306, 0.001)

def test_reynolds_number():
    assert reynolds_number(998.2000000, 0.048692, 0.00, 0.0010016) == approx(0, 1)
    assert reynolds_number(998.2000000, 0.048692, 1.65, 0.0010016) == approx(80069, 1)
    assert reynolds_number(998.2000000, 0.048692, 1.75, 0.0010016) == approx(84922, 1)
    assert reynolds_number(998.2000000, 0.286870, 1.65, 0.0010016) == approx(471729, 1)
    assert reynolds_number(998.2000000, 0.286870, 1.75, 0.0010016) == approx(500318, 1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(998.2000000, 0.28687, 0.00, 1, 0.048692) == approx(0.000, 0.001)
    assert pressure_loss_from_pipe_reduction(998.2000000, 0.28687, 1.65, 471729, 0.048692) == approx(-163.744, 0.001)
    assert pressure_loss_from_pipe_reduction(998.2000000, 0.28687, 1.75, 500318, 0.048692) == approx(-184.182, 0.001)

# Call the main function that is part of pytest so that
# the computer will execute the test functions in this file
pytest.main(["-v", "--tb=line", "-rN", __file__])
