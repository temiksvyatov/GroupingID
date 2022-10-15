# Python 3.10.5
# Made by Artem S.

# WARNING: Keys in dictionaries are not sorted

# Grouping Ids of customers starting from zero index
def zeroStart(n_customers):
    groups = {}
    for i in range(n_customers):
        converted = sum(list(map(int, str(i))))
        if groups.get(converted) == None:
            groups[converted] = [i]
        else:
            groups[converted].append(i)
    return groups

# Grouping Ids of customers starting from fixed index
def fixedStart(n_customers, n_first_id):
    groups = {}
    for i in range(n_first_id, n_first_id + n_customers):
        converted = sum(list(map(int, str(i))))
        if groups.get(converted) == None:
            groups[converted] = [i]
        else:
            groups[converted].append(i)
    return groups


def main():
    pass
    


if __name__ == '__main__':
    main()
