import logging

logging.basicConfig(filename='list.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

class List:
    def __init__(self,lst):
        self.lst = lst

    # Try to extract all the list entities
    def extract_list_entity(self):
        try:
            logging.info('Extracting list entities')
            lst_ent = []
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        lst_ent.append(j)
            logging.info(lst_ent)
            return lst_ent
        except Exception as e:
            logging.exception(e)

    # Try to filter out all odd values out of all numeric data which is part of a list
    def filter_odd(self):
        try:
            logging.info('Filtering odd values from lists')
            odd_values=[]
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if type(j) == int and j % 2 != 0:
                            odd_values.append(j)
            logging.info(odd_values)
            return odd_values
        except Exception as e:
            logging.exception(e)

    # """ Extract 'ineuron' string data from collections"""
    def extract_ineuron(self):
        try:
            logging.info('Extracting ineuron from list')
            ineuron = []
            for i, j in enumerate(l):
                if type(j) != dict:
                    for n in j:
                        if type(n) == str and n == 'ineuron':
                            ineuron.append((f'collection {i} :', n))
                else:
                    for k in (j.items()):
                        for m in k:
                            if type(m) == str and m == 'ineuron':
                                ineuron.append((f'collection {i} :', m))
            logging.info(ineuron)
            return ineuron

        except Exception as e:
            logging.exception(e)

    # """ To create flat list from nested collection"""
    def flatten(self):
        try:
            logging.info('Creating a flattened list')
            all_data = []
            for i in l:
                if type(i) != dict:
                    for j in i:
                        all_data.append(j)
                else:
                    for k in (i.items()):
                        for m in k:
                            all_data.append(m)
            logging.info(all_data)
            return all_data

        except Exception as e:
            logging.exception(e)

if __name__ == '__main__':
    l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
         {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
    obj = List(l)
    print(obj.extract_list_entity())
    print(obj.filter_odd())
    print(obj.extract_ineuron())
    print(obj.flatten())
