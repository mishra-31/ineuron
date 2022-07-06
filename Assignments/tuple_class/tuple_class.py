import logging

logging.basicConfig(filename='tuple.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

class Tuple:

    def __init__(self,collection):
        self.collection = collection

    # Try to extract all the tuple entities
    def extract_tuple_ent(self):

        try:
            logging.info('Extracting tuple entities')
            tup_ent=[]
            for i in self.collection:
                if type(i) == tuple:
                    for j in i:
                        tup_ent.append(j)
            logging.info(tup_ent)
            return tup_ent

        except Exception as e:
            logging.exception(e)

if __name__ == '__main__':
    l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7,8), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
         {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
    obj = Tuple(l)
    print(obj.extract_tuple_ent())
