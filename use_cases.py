from time import time


def time_it(function, timers={}):
    """Decorator function to time the duration and number of function calls.

    :param function: function do be decorated
    :type function: function
    :param timers: storage for cumulated time and call number
    :type timers: dict
    :return: decorated function or timer if given function is None
    :rtype function or dict

    """
    if function:
        def decorated_function(*this_args, **kwargs):
            key = function.__name__
            start_time = time()
            return_value = function(*this_args, **kwargs)
            delta_time = time() - start_time
            try:
                timers[key]["time"] += delta_time
                timers[key]["calls"] += 1
            except KeyError:
                timers[key] = dict(time=0, calls=1)
                timers[key]["time"] += delta_time
            return return_value

        return decorated_function

    sorted_timer = dict(sorted(timers.items(), key=lambda x: x[1]["time"] / x[1]["calls"]))
    return sorted_timer


def main():
    my_list = ["foo"]
    my_list = append_bar_with_cache(my_list)
    print(my_list)

    my_list = append_bar_with_cache(my_list)
    print(my_list)

    count_to_num(10_000)

    my_list = append_bar_with_cache([])
    print(my_list)

    my_list = append_bar_with_cache(["hello", "world"])
    print(my_list)

    count_to_num(10_000_000)

    print(append_bar_with_cache(dump_cache=True))

    print(time_it(None))


@time_it
def append_bar_with_cache(my_list=None, cache=[], dump_cache=False):
    if dump_cache:
        return cache
    cache.append(my_list.copy())
    if my_list is None:
        my_list = []
    my_list.append("bar")
    return my_list


@time_it
def count_to_num(num):
    counter = 0
    for i in range(num):
        counter = i


if __name__ == '__main__':
    main()
