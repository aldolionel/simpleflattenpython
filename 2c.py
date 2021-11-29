import json
import nomor1 as module

def cetak(x, name = ''):
    if type(x) is dict:
        for a in x:
            cetak(x[a], name + ' ')
    elif type(x) is list:
        for a in x:
            cetak(a, name + ' ')
    else:
        return print(name, x)        

if __name__ == '__main__':
    with open('2b.json', "r") as myfile:
        json_data = json.load(myfile)
    if module.check(json_data):
        print("Kategori")
        print("=======")
        cetak(json_data)