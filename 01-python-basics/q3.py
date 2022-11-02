import json

# def sort_data_structure(ds):
#     match str(type(ds)):
#         case "<class 'list'>":
#             ds.sort()
#             return ds
#         case "<class 'tuple'>":
#             sorted_tuple = tuple(sorted(ds))
#             return sorted_tuple
#         case "<class 'dict'>":
#             sorted_dict = dict(sorted(ds.items()))
#             return sorted_dict
#         case "<class 'set'>":
#             sorted_set = dict.fromkeys(sorted(ds))
#             return sorted_set
#         case _:
#             return ds

def convert_to_str_then_sort(ds):
    match str(type(ds)):
        case "<class 'list'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = list(ds.split(" "))
            return ds
        case "<class 'tuple'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = tuple(ds.split(" "))
            return ds
        case "<class 'dict'>":
            ds = json.dumps(ds)
            print(ds)
            ds = json.loads(ds)
            print(ds)
            return ds
        case "<class 'set'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = set(ds.split(" "))
            return ds
        case _:
            return ds

def iterate(ds):
    match str(type(ds)):
        case "<class 'list'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
        case "<class 'tuple'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
        case "<class 'dict'>":
            for key, value in ds.items():
                ds[key] = convert_to_str_then_sort(value)
        case "<class 'set'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
        case _:
            return ds

def print_sorted(x):
    updated_ds = convert_to_str_then_sort(x)
    ans = iterate(updated_ds)
    print(type(ans))
    print(ans)


def main():
    # x = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    # x = {"a": 5, "c": 6, "b": [1, 3, "dog", 2, "cat", 4]}
    x = {"a": 5, "c": [{"b": 1, "a": 2}, {"d": 3, "c": 4}], "b": [1, 3, "dog", 2, "cat", 4]}
    # x = [[2,1],[4,3],[[6,5],[0,1]]]
    print_sorted(x)

if __name__ == "__main__":
    main()
