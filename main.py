class Contract:
    def __init__(self, id: int, debt: float):
        self.id = id
        self.debt = debt

    def __str__(self):
        return f"id={self.id}, debt={self.debt}"


def get_top_N_open_contracts(
    open_contracts: list[Contract],
    renegotiated_contracts: list[int],
    top_n: int,
) -> list[int]:
    open_contracts.sort(key=lambda el: el.debt, reverse=True)
    renegotiated = set(renegotiated_contracts)

    counter, top_n_open_contracts = 0, []
    for el in open_contracts:
        if el.id in renegotiated:
            continue

        if counter >= top_n:
            break

        top_n_open_contracts.append(el.id)
        counter += 1

    return top_n_open_contracts


def combine_orders(requests: list[int], n_max: int):
    requests.sort(reverse=True)
    num_trips = 0

    while requests:
        if len(requests) == 1:
            num_trips += 1
            requests.pop()
        else:
            trip_capacity, trip_count = 0, 0
            while trip_capacity < n_max and trip_count < 2 and requests:
                if trip_capacity + requests[0] <= n_max:
                    trip_capacity += requests[0]
                    requests.pop(0)
                else:
                    trip_count += 1
            num_trips += 1

    return num_trips
