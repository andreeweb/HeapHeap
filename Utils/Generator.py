import random


class Generator:

    @classmethod
    def generate(cls, seed, input_size):
        """
        Generate input_size random numbers with the seed specified

        :param seed:
        :param count:
        :return:
        """
        random.seed(seed)
        random_numbers = []
        for i in range(input_size):
            k = random.randint(0, input_size)
            j = random.randint(0, input_size)
            random_numbers.append([k, j])
        return random_numbers


