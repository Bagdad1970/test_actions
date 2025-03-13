import src.add as add


def test_add_5_to_2():
    num1 = 5
    num2 = 2

    sut = add.add(5, 2)

    assert sut == 7
