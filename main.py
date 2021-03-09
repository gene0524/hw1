
import csv 

cwb_filename = '107030027.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)


target_data = list(filter(lambda item: item['HUMD'] != ('-99.000' or '-999.000'), data))
st1 = list(filter(lambda item: item['station_id'] == 'C0A880', target_data))
st2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', target_data))
st3 = list(filter(lambda item: item['station_id'] == 'C0G640', target_data))
st4 = list(filter(lambda item: item['station_id'] == 'C0R190', target_data))
st5 = list(filter(lambda item: item['station_id'] == 'C0X260', target_data))


get_Data = lambda title, Data_list: [sub_Data[title] for sub_Data in Data_list if title in sub_Data]


def humd_sum(station):
   h_sum = sum(map(float,get_Data('HUMD', station)))
   if h_sum == 0:
      return 'NONE'
   else:
      return h_sum

final_data = [['C0A880', round(humd_sum(st1),3)], ['C0F9A0', round(humd_sum(st2),3)], 
['C0G640', round(humd_sum(st3),3)], ['C0R190', round(humd_sum(st4),3)], ['C0X260', round(humd_sum(st2),3)]]

print(final_data)
