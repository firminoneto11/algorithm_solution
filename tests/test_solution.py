from main import Contract, combine_orders, get_top_N_open_contracts


def test_get_top_N_open_contracts():
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]

    renegotiated, top_n, expected_open_contracts = [3], 3, [5, 4, 2]

    assert expected_open_contracts == get_top_N_open_contracts(
        contracts, renegotiated, top_n
    )


def test_combine_orders():
    orders, n_max, expected_orders = [70, 30, 10], 100, 2

    assert combine_orders(orders, n_max) == expected_orders
