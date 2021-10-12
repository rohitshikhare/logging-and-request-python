import logging

logging.basicConfig(filename='example.log', format='%(levelname)s : %(asctime)s: %(message)s: %(lineno)d',
                    level=logging.DEBUG)


class Solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a == 0 or b == 0:
            logging.warning('number zero found...')

    def sum(self):
        ans = self.a + self.b
        logging.debug(f"sum of {self.a, self.b} is {ans}")

    def subtraction(self):
        ans = self.a - self.b
        logging.debug(f"subtraction of {self.a, self.b} is {ans}")

    def multiplication(self):
        ans = self.a * self.b
        logging.debug(f"multiplication of {self.a, self.b} is {ans}")

    def division(self):
        ans = self.a / self.b
        logging.debug(f"division of {self.a, self.b} is {ans}")


obj = None
try:
    obj = Solution(2, 0)
except:
    logging.critical('object not created...')
    exit(0)

logging.info('Object created...')

obj.sum()
obj.subtraction()
obj.multiplication()

try:
    obj.division()
except:
    logging.error(' number divide by Zero...')

logging.info('Program successfully completed...')
