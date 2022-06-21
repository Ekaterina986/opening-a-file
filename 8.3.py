import os
from pprint import pprint
catalog_name = 'sorted'
base_pas = os.getcwd()
list_file_names = ['1.txt', '2.txt', '3.txt']

list_file_data = []
for file_name in list_file_names:
    full_path = os.path.join(base_pas, catalog_name, file_name)
    with open(full_path) as one_file:
        list_str = one_file.readlines()

        list_file_data.append({
            'file_name': file_name,
            'list_str': list_str,
            'length': len(list_str)
        })
sorted_list_file_data = sorted(list_file_data, key = lambda data_item: data_item['length'])
res = ''
for data in sorted_list_file_data:
    res += data['file_name'] + "\n"
    res += str(data['length']) + '\n'
    res += ''.join(data['list_str']) + '\n'
print(res)