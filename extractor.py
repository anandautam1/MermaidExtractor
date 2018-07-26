import xlsxwriter 
import re
import operator

#open the 
file = open('timeLine.md','r')

result = []
for line in file.readlines():
    if re.search('section',line, re.I):
        result.append([])
        result[-1].append(line)
    elif re.search('title',line, re.I):
        result.append([])
        result[-1].append(line)
    else:
        designatedIndex = len(result)-1
        #print(designatedIndex)
        if designatedIndex == -1:
            result.append(line)
        else:
            if designatedIndex >= 1:
                result[designatedIndex].append(line)
            #print(result[designatedIndex])
file.close()           
    
#print(result)

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

i = 0
offset = 1
while i < len(result):
    #print(result[i])
    #print('\n')
    if (type(result[i]) is str):
        print("\n")
    elif(type(result[i]) is list):

        # print(result[i][0])
        # check the first element for keyword 
        if re.search('title',result[i][0], re.I):
            ExcelIndex = 'A' + str(offset)
            worksheet.write(ExcelIndex, result[i][0])   
            offset += 3

        #start 2 onwards 
        elif re.search('section', result[i][0], re.I):
            length = len(result[i])
            
            ExcelIndex = 'A' + str(offset)
            worksheet.write(ExcelIndex, 'Activity Name')
            ExcelIndex = 'B' + str(offset)
            worksheet.write(ExcelIndex, 'State Of The Activity') 
            ExcelIndex = 'C' + str(offset)
            worksheet.write(ExcelIndex, 'Nickname')  
            ExcelIndex = 'D' + str(offset)
            worksheet.write(ExcelIndex, 'Date')  
            ExcelIndex = 'E' + str(offset)
            worksheet.write(ExcelIndex, 'Length Of Activity')
            offset += 1

            for j in range(len(result[i])):
                if(j == 0):
                    print(offset)
                    spaceDelimit = re.split(r'[^\S\n\t]+',result[i][j])
                    print(spaceDelimit)
                    #input start at 1 and 2 
                    ExcelIndex = 'A' + str(offset-2)
                    worksheet.write(ExcelIndex, spaceDelimit[1])
                    ExcelIndex = 'B' + str(offset-2)
                    worksheet.write(ExcelIndex, spaceDelimit[2]) 
                else:
                    commaColonDelimit = re.split(':|,|\n',result[i][j])
                    #strip white spaces arrays
                    commaColonDelimit = [x for x in commaColonDelimit if x.strip()] # fastest
                    print(commaColonDelimit)

                    if len(commaColonDelimit) == 2:
                        ExcelIndex = 'A' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[0])
                        ExcelIndex = 'B' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[1]) 

                    if len(commaColonDelimit) == 3:
                        ExcelIndex = 'A' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[0])
                        ExcelIndex = 'B' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[1]) 
                        ExcelIndex = 'E' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[2])  

                    if len(commaColonDelimit) == 4:
                        ExcelIndex = 'A' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[0])
                        ExcelIndex = 'B' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[1]) 
                        ExcelIndex = 'C' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[2])  
                        ExcelIndex = 'E' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[3])  

                    if len(commaColonDelimit) == 5:
                        ExcelIndex = 'A' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[0])
                        ExcelIndex = 'B' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[1]) 
                        ExcelIndex = 'C' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[2])  
                        ExcelIndex = 'D' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[3])  
                        ExcelIndex = 'E' + str(offset)
                        worksheet.write(ExcelIndex, commaColonDelimit[4])

                    offset += 1
            
            offset += 2

    i += 1

#worksheet.write('A1','Hello World')
#worksheet.write('A2','Hello World')

workbook.close()
