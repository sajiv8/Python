row,colum=map(int,input("Enter the dimension: ").split(','))     
      
#creating an empty list to store my input matirx
def get_input(row, col, matr, matrix):
    print(f'Enter Matrix {matr}: ')
    for i in range(row):        
        
    #running loop for gettin inputs for matrix row by row
        try:
            rows=list(map(int,input().split()))
        except:
            print('Error')
            quit()
        #grttti input seperated by white spaces
        
        if len(rows)==col:       
            #giving a constraint to check the matrix have correct count of colums that by the input given
            matrix.append(rows)
        else:
            print("Invalid Matrix")
            quit()
        
            
            
                
    return(matrix)
matrix_a = []
matrix_b = []
matrix_a = get_input(row, colum, 'A', matrix_a)
matrix_b = get_input(row, colum, 'B', matrix_b)
print(matrix_a)
print(matrix_b)
