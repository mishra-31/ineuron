import logging

logging.basicConfig(filename='dict.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

class Dict:

    def __init__(self,collection):
        self.collection = collection

    # Extract all the dict entities
    def extract_dct_ent(self):
        try:
            logging.info('Extracting dict entities')

            dict_ent=[]
            for i in self.collection:
                if type(i) == dict:
                    for j in i.items():
                        dict_ent.append(j)
            logging.info(dict_ent)
            return dict_ent

        except Exception as e:
            logging.exception(e)

    # Find no of keys in dict element
    def no_of_keys(self):
        try:
            logging.info('Counting dict keys')
            dict_keys = []
            for i in self.collection:
                if type(i) == dict:
                    for j in i.keys():
                        dict_keys.append(j)
            keys=f'Number of keys : {len(dict_keys)}'
            logging.info(keys)
            return keys
        except Exception as e:
            logging.exception(e)

    ## Extract all numerical data that is a part of dict key and values

    def extract_num(self):

        try:
            logging.info('Extracting num data')
            num = []
            for i in self.collection:
                if type(i) == dict:
                    for k in (i.items()):
                        for m in k:
                            if type(m) == int:
                                num.append(m)
                            if type(m) == dict:
                                for j in (m.items()):
                                    for r in j:
                                        if type(r) == int:
                                            num.append(r)
            logging.info(num)
            return num
        except Exception as e:
            logging.exception(e)

    # fun which will take input as a dict and give me out as a list of all the values
    # even in case of 2 level nesting it should work .

    def values_list(self,dct):
        try:
            logging.info('Creating list of values')
            new_list = []
            for i in dct.values():
                if type(i) != dict:
                    new_list.append(i)
                else:
                    for j in i.values():
                        new_list.append(j)
            logging.info(new_list)
            return new_list

        except Exception as e:
            logging.exception(e)

if __name__ == '__main__':
    l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
         {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 'k4':{1:'value',3: 6, 7: 8}}, ["ineuron", "data science"]]
    d = {'1': [1, 2, 3], '2': {'3': [1, 2, 3], 'a': ['b', 'c', 'd']}}
    obj = Dict(l)
    print(obj.extract_dct_ent())
    print(obj.extract_num())
    print(obj.no_of_keys())
    print(obj.values_list(d))