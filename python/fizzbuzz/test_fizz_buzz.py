from python.fizzbuzz.fizz_buzz import fizz_buzz


def test_fizz_buzz_empty_list():
    expected_list = []

    return_value = fizz_buzz(0)

    assert expected_list == return_value


def test_fizz_buzz_with_a_one():
    expected_list = [1]

    return_value = fizz_buzz(1)

    assert expected_list == return_value


def test_fizz_buzz_with_a_two():
    expected_list = [1, 2]

    return_value = fizz_buzz(2)

    assert expected_list == return_value


