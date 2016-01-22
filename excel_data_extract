# used to extract all data within excel sheet, including title cols
# results returned as an array. each index is a new row.
def excel_data_extract(excel_workbook):
    """Grab data from an excel workbook and push into a python list"""
    workbook = xlrd.open_workbook(excel_workbook)
    #workbook.nsheets  #gives you the number of sheet
    worksheet = workbook.sheet_by_index(0)
    #print 'worksheet:\n', worksheet
    srows = worksheet.nrows  #provides total number of rows, -1 to use in loop
    #print 'rows:    ', srows
    scols = worksheet.ncols#provides total number of cols, -1 to use in loop
    #print 'cols:    ', scols
    a = []
    print "Processing %s records" % ((srows-1))
    for row in range(0,srows):
        for c in worksheet.row(row):
           entry = [c.value.encode('ascii','ignore') if type(c.value) == unicode else str(c.value) for c in worksheet.row(row)]
        a.append(entry)
        #sleep(0.05)
        update_progress(float(row)/float(srows-1))
    #a = [str(c.value) for r in xrange(srows) for c in worksheet.row(r)])
    #reshape the array to "match" the rows and columns found in the worksheet
    #a = a.reshape((srows,scols))
    return a

# used to match data with proper col titles.
# col titles are grabbed from the array[0] and zippered together with
# remaining indexes in array.
def dictionary_merge (array):
    """Takes a python list, which has header columns in index 0 and turns results into a list of dictionaries"""
    col_title = array[0]
    total_rows = len(array)
    total_cols = len(array[0])
    combined_fields = []
    #for colname in array[0]: #to determine what columns have been designated by that array exit comment
    #   print colname
    for r in range(0,total_rows):
        tmpdict = {}
        for c in xrange(total_cols):
            tmpdict[col_title[c]] = array[r][c]
        combined_fields.append(tmpdict)
    return combined_fields

# if header == 1, then main will return a dictionary
# if header == 0, then main will return an array
def main(excel_workbook, header):
  excel_data = excel_data_extract(excel_workbook)
  if header == 1:
    return dictionary_merge(excel_data)
  else:
    return excel_data
