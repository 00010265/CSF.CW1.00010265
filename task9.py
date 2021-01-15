import functools
# To see the difference between the two, I will show how to solve one task on both of them
# We should calculate sum of the following list
the_list = [1, 2, 3, 4, 5]
# Functional programming aims to convert everything to math equation


def functional_programming(x, y):
    return x + y


sum_list = functools.reduce(add_it, the_list)
print(sum_list)

# Object oriented programming


class SumList(object):
    def __init__(self, any_list):
        self.any_list = any_list

    def do_add(self):
      self.sum = sum(self.any_list)


sum_of_list = SumList(the_list)
sum_of_list.do_add()
print(sum_of_list.sum)