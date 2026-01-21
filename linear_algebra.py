
loop=0
arr_1 = [[1,0,0],
        [0,1,0],
        [0,0,1]]

arr_2 = [[1,3,6],
        [12,1,9],
        [4,5,6]]
new_matrix = []
for row in range(len(arr_1)):
    for col in range(len(arr_2)):
        sub_result = 0
        for j in range(len(arr_2[0])):
            sub_result += arr_1[row][j] * arr_2[j][col]
        print(sub_result)
        new_matrix.append(sub_result)
        
    #new_el = 0
print(new_matrix)