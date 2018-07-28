from osgeo import gdal
m=int(input("Enter the rows"))
n=int(input("enter the column"))
for i in range(0,m):
    for j in range(0,n):
        print(i*j,end=' ')
    print()   
