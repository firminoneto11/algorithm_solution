from pytest import mark

from main import Contract, combine_orders, get_top_N_open_contracts


@mark.parametrize(
    argnames="contracts,renegotiated,top_n,expected_open_contracts",
    argvalues=(
        (
            [
                Contract(1, 1),
                Contract(2, 2),
                Contract(3, 3),
                Contract(4, 4),
                Contract(5, 5),
            ],
            [3],
            3,
            [5, 4, 2],
        ),
        (
            [
                Contract(1, 1),
                Contract(2, 2),
                Contract(3, 3),
                Contract(4, 4),
                Contract(5, 5),
            ],
            [3],
            1,
            [5],
        ),
        (
            [
                Contract(1, 1),
                Contract(2, 2),
                Contract(3, 3),
                Contract(4, 4),
                Contract(5, 5),
            ],
            [3, 4],
            2,
            [5, 2],
        ),
        (
            [
                Contract(1, 1),
                Contract(2, 2),
                Contract(3, 3),
                Contract(4, 4),
                Contract(5, 5),
            ],
            [3, 4],
            3,
            [5, 2, 1],
        ),
    ),
)
def test_get_top_N_open_contracts(
    contracts: list[Contract],
    renegotiated: list[int],
    top_n: int,
    expected_open_contracts: list[int],
):
    assert expected_open_contracts == get_top_N_open_contracts(
        contracts, renegotiated, top_n
    )


@mark.parametrize(
    argnames="orders,n_max,expected_orders",
    argvalues=[
        ([70, 30, 10], 100, 2),
        ([100, 100, 100], 100, 3),
        ([100, 100, 99, 5], 100, 4),
        ([100, 100, 99, 96, 10, 5], 100, 5),
    ],
)
def test_combine_orders(orders: list[int], n_max: int, expected_orders: int):
    assert combine_orders(orders, n_max) == expected_orders
