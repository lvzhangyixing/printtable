#! python3
# printTable 将每列最长的单词放在右边，右对齐

def getColWidth(table, widths):
    for each_table in range(len(table)):
        for item in table[each_table]:
            widths[each_table] = max(len(item), widths[each_table])  # width[]默认是0，获取每行最长单词

def printTable(table, widths):
    rowNums = len(table)
    colNums = len(table[0])
    for colNum in range(colNums):
        # print(table[0][colNum].ljust(widths[0], end=' '))
        for rowNum in range(rowNums):
            print(table[rowNum][colNum].ljust(widths[rowNum]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

getColWidth(tableData, colWidths)
printTable(tableData, colWidths)
