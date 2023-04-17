DEFAULT_LIST = ["foo"]

def main():
    my_list = ["foo"]
    my_list = append_bar(my_list)
    print(my_list)

    my_list = append_bar()
    print(my_list)

    my_list = append_bar([])
    print(my_list)

    my_list = append_bar()
    print(my_list)


def append_bar(my_list=None):
    if my_list is None:
        my_list = DEFAULT_LIST
    my_list.append("bar")
    return my_list


if __name__ == '__main__':
    main()
