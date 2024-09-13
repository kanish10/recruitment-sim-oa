import numpy as np


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    if (height < 0):
        raise Exception("Height must not be negative.")

    g = 9.81
    final_velocity_bottom = np.sqrt(((4/3) * g * height))
    return final_velocity_bottom

# test function
def test_func_1():
    assert final_disk_speed(0, 0, 0, 0, 0, 0) == 0.0
def test_func_2():
    assert np.isclose(final_disk_speed(1, 1, 1, 1, 1, 1), 3.616628264, atol=1e-6)

# test exception
def test_exception():
    try:
        final_disk_speed(-1, 0, 0, 0, 0, 0)
    except Exception as e:
        assert str(e) == "Height must not be negative."
        print("Test passed: Exception correctly raised.")
    else:
        assert False, "Test failed: Exception was not raised."

def tests():
    test_func_1()
    test_func_2()
    test_exception()
    print("All tests passed!")

if __name__ == "__main__":
    tests()