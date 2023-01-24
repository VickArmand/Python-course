def safe_print_list_integers(my_list=[], x=0):
        count = 0
        for x in my_list[0:x]:
            try:
                print("{:d}".format(x, end=''))
            except:
                break
            else:
                count += 1
        print()
        return (count)
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))