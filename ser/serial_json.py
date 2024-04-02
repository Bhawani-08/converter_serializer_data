#don't take this seriously 

import json
from .models import Table2,Table1
from .serializer import Table1serializer,table2serializer

table1_instance = Table1.objects.get(pk = 1)
table2_instance = Table2.objects.get(pk = 1)

table1_serializer = Table1serializer(table1_instance)
table2_serializer = table2serializer(table2_instance)

print("Serialized Table1 data:")
print(json.dumps(table1_serializer.data,indent=2))

print("Serialized Table2 data:")
print(json.dumps(table2_serializer.data,indent=2))