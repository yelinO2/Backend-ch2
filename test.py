stores = [
   {
       "name": "Apple",
       "items": [
           {
               "name": "iphone13",
               "price": 1299.99
           }
       ]
   },
   {
       "name": "Microsoft",
       "items": [
           {
               "name": "SurfacePro",
               "price": 1399.99
           }
       ]
   },
]

item = 'SurfacePro'
for store in stores:
    for items in store['items']:
        if item == items['name']:
            print(items)


