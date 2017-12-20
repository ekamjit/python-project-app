center_to_stock = {'C1': ['A', 'B', 'C'],
                   'C2': ['D', 'E', 'F'],
                   'C3': ['G', 'H', 'I']}

stock_to_weight = {
    'A': 3,
    'B': 2,
    'C': 8,
    'D': 12,
    'E': 25,
    'F': 15,
    'G': 0.5,
    'H': 0.8,
    'I': 1,
}

weight_to_cost = {
    '0-5': 10,
    '5-10': 18,
    '10-15': 25,
    '15-20': 30,
    '20-25': 34,
    '25-30': 37,
    '30-35': 39,
    '35-500': 40
}

distance_graph = {
    'C1': {'C2': 4, 'L1': 3},
    'C2': {'C1': 4, 'L1': 2.5, 'C3': 3},
    'C3': {'C3': 3, 'L1': 2},
    'L1': {'C1': 3, 'C2': 2.5, 'C3': 2}
}

pickup_cost = 10
drop_cost = 5
# as truck will be empty, so return cost is 10
return_cost = 10


def find_min_cost(packets_list):
    if len(packets_list) == 0:
        return 0
    first_location = find_pickup_point(packets_list[0])
    print "first pickup location : {}".format(first_location)

    last_pickup_location = first_location
    # first time pickup
    cost = pickup_cost
    weight = stock_to_weight[packets_list[0]]
    # start from second packet in list
    for packet in packets_list[1:]:
        location = find_pickup_point(packet)
        if location == last_pickup_location:
            weight += stock_to_weight[packet]
        else:
            cost += pickup_cost
            weight += stock_to_weight[packet]
            cost += find_weight_cost(weight) * distance_graph[location][last_pickup_location]
        last_pickup_location = location

    cost += find_weight_cost(weight) * distance_graph[last_pickup_location]['L1']
    cost += drop_cost
    # add return cost
    cost += return_cost * distance_graph['L1'][first_location]
    return cost


def find_pickup_point(packet):
    for key, value in center_to_stock.iteritems():
        if packet in value:
            return key

    return None


def find_weight_cost(weight):
    for key, value in weight_to_cost.iteritems():
        keys = key.split('-')
        if int(keys[0]) < weight <= int(keys[1]):
            return value
    return 0


if __name__ == '__main__':
    print find_min_cost(['A', 'B', 'C', 'D'])
