# Tao matran
L =[[0,0,0,0,0,0,0,0,0,0]]
for k in range(1,11):
    L.append([0,0,0,0,0,0,0,0,0,0])
    
# Cach danh so
print("Co 10x10 o, gom 9 hang va 9 cot, cot va hang dau tien duoc danh so 0 !\n")

# Nhap vi tri dat boom
i,j = 0,0
while i != -1 and j != -1:
    i,j = int(input("Nhap vao vi tri dat boom va ket thuc bang -1 -1, i j = \n")),int(input())
    L[i][j] = 1
    
# Giai thuat de qui
def Boom(i,j):
    while i <= 10 and i >= 0 and j <= 10 and j >= 0 and L[i][j] != 0: # Dieu kien de (i,j) khong vuot qua 10x10 va vi tri (i,j) co bom
        L[i][j] = 0                             # Bom no
        print('(',i,' ',j,')')                  # in ra vi tri no theo thu tu truoc sau
        Boom(i+1,j)                             # xet cac o ke ben
        Boom(i,j-1)
        Boom(i-1,j)
        Boom(i,j+1)
        
                    
# Phan chuong trinh chinh
if __name__ == '__main__':
    i,j = int(input("Nhap vao cac vi tri cho no dau tien boom: i j = \n")),int(input())
    if L[i][j] == 1:
        Boom(i,j)
    else:
        print("Khong co vu no nao xay ra")
        
