import xlrd
import json
from collections import OrderedDict

xlfile = input('please enter name of workbook, include extension')
wb = xlrd.open_workbook(xlfile)
sh = wb.sheet_by_index(0)

return_data = []
for row in range(0,sh.nrows):
    datpt = OrderedDict()
    rowdat = sh.row_values(row)
    datpt['descrptn'] = rowdat[0]
    datpt['link'] = rowdat[1]
    datpt['notes1'] = rowdat[2]
    datpt['notes2'] = rowdat[3]
    return_data.append(datpt)

j_dump = json.dumps(return_data)
xlfile = xlfile.split('.')[0]
with open(xlfile + '.json', 'w') as file:
    file.write(j_dump)
