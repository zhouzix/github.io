data = [
    {"id": 4, "name": "name4", "pid": 1},{"id": 1, "name": "name1", "pid": 0},{"id": 2, "name": "name2", "pid": 0},{"id": 3, "name": "name3", "pid": 0},
    {"id": 5, "name": "name4", "pid": 2},{"id": 6, "name": "name5", "pid": 2},{"id": 7, "name": "name6", "pid": 4},
]

def change(data):
    leng = len(data)
    data = sorted(data,key=lambda x: x['pid'])
    result = [{"id":0,'children':[]}]
    for i in data:
        i['children']=[]
        parent = result
        pid= i['pid']
        del i['pid']
        for p in parent:
            if pid == p['id']:
                p['children'].append(i)
                break
            if p['children'] != []:
                parent.extend(p['children'])
    return result[0]['children']
[
    {'id': 1, 'name': 'name1', 
    'children':
     [{'id': 4, 'name': 'name4', 'children': [{'id': 7, 'name': 'name6', 'children': []}]}]},
     {'id': 2, 'name': 'name2', 'children': [
         {'id': 5, 'name': 'name4', 'children': []},
          {'id': 6, 'name': 'name5', 'children': []}
          ]},
      {'id': 3, 'name': 'name3', 'children': []}
    ]










