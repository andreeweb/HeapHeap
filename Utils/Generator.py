import random


class Generator:

    @classmethod
    def generate(cls, seed, count):
        """
        Generate count random numbers with the seed specified

        :param seed:
        :param count:
        :return:
        """
        random.seed(seed)
        random_numbers = []
        for i in range(count):
            k = random.randint(0, count)
            j = random.randint(0, count)
            random_numbers.append([k, j])
        return random_numbers


