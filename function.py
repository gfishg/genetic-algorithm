
class Function:

    def __init__(self, variable_config):
        self.__variable_config = variable_config

    @staticmethod
    def functionEvaluate(data):
        x1, x2 = data

        return (1.5-x1 + x1 * x2) ** 2 + (2.25 - x1 + x1 * x2 ** 2) ** 2 + (2.625 - x1 + x1 * x2 ** 3) ** 2
