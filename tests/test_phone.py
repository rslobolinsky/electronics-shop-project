from src.phone import Phone


def test_get_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)

    assert phone.number_of_sim == 2