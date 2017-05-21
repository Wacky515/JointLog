# import os
import linecache

def select_tail(data):
    line_no = sum(1 for line in open(data))
    tail = str(linecache.getline(data, int(line_no))).strip()
    print(tail)
    return tail, line_no

plc_data = select_tail("sample_csv_a.csv")
recorder_data = select_tail("sample_csv_b.csv")
join = plc_data[0] + "," + recorder_data[0]

# print(plc_data)
# print(recorder_data)
print(join)
