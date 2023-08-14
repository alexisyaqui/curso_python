import datetime
from datetime import datetime as d

d = datetime.datetime(2021, 1,13,2,34,35, 22222)
print(d)

print("para obtener el tiempo real")
dt = d.now()
print(dt)

print("para obtener el separadado")
dt.year
dt.month
dt.day
dt.hour
dt.minute
dt.second

print(f'año: {dt.year} mes: {dt.month},dia: {dt.day}, hora: {dt.hour} minutos: {dt.minute},segundos: {dt.second}')