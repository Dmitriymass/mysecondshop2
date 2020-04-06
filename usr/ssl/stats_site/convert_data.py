import json

fn = 'data/users.json'
out_fn = 'data/users_conv.json'

"""
{"id": 1, "first_name": "Christie", "last_name": "Gann", "email": "cgann0@hostgator.com", "gender": "Female", "ip_address": "57.14.195.231"}
  {
    "model": "stats_app.User",
    "pk": 1,
    "fields": {
      "first_name": "Christie",
      "last_name": "Gann",
      "email": "cgann0@hostgator.com",
      "gender": "Female",
      "ip_address": "57.14.195.231"
    }
  },

"""


with open(fn) as f, open(out_fn, 'w') as out_f:
    data = json.load(f)
    out_data = []
    for record in data:
        out_record = {"model": "stats_app.User", "pk":record['id']}
        #del record['id']
        #out_record['fields'] = record
        out_record['fields'] = {k:v for k,v in record.items() if k!='id'}
        out_data += out_record,
        #break


    json.dump(out_data, out_f, indent=2)


fn = 'data/users_statistic.json'
out_fn = 'data/users_statistic_conv.json'

with open(fn) as f, open(out_fn, 'w') as out_f:
    data = json.load(f)
    out_data = []
    for record in data:
        out_record = {"model": "stats_app.Statistic"}
        out_record['fields'] = record
        out_data += out_record,


    json.dump(out_data, out_f, indent=2)




