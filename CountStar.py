import cv2

# Xác định các vùng thuộc cùng 1 ngôi sao
def partOfStar(check: list, matrix: list, row: int, col: int):
    index = []
    for i in range(-1,2):
        r = row + i
        if r >= 0 and r < len(matrix):
            for j in range(-1,2):
                c = col + j
                if c >= 0 and c < len(matrix[0]):
                    if i != 0 or j!= 0:
                        if matrix[r][c] and check[r][c]:
                            index.append([r, c])
                        check[r][c] = False
    return index

# Đếm số ngôi sao
def countStar(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    check = [[True for _ in range(n)] for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if matrix[row][col] and check[row][col]:
                count += 1
                index = partOfStar(check, matrix , row, col)
                for k in index:
                    r, c = map(int, k)
                    index.extend(partOfStar(check, matrix, r, c))
            check[row][col] = False
    return count

# Mã hóa ảnh [0-255] về dạng và chuyển ảnh [0-1] ảnh nhị phân
def convertToBinaryPicture(rbgPicPath: str = ..., binaryPicPath: str = ...):
    img = cv2.imread(rbgPicPath, 2)
    ret, star = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imwrite(binaryPicPath, star)
    return binaryPicPath

# Chuyển ảnh về về dạng ma trận 0-1
def convetToBinaryMatrix(pathname: str =...):
    img = cv2.imread(pathname)
    matrix = []
    for i in img:
        star =[]
        for j in i:
            if str(j) == "[255 255 255]": # Màu trắng tương đương với ngôi sao
                star.append(1)
            else: # Màu đen tương đương với 1 phần của bàu trời
                star.append(0)
        matrix.append(star)
    return matrix

if __name__ =="__main__":
    pathname = "Simple.png" # Đường link ảnh bầu trời sao
    binarypath = "Star.png" # Nơi muốn lưu bức ảnh bầu trời sao

    # B1 Mã hóa ảnh màu [0-255] về ảnh nhị phân
    star = convertToBinaryPicture(pathname, binarypath) 

    # B2 Chuyển ảnh về dạng ma trận có các giá trị 0-1
    matrix = convetToBinaryMatrix(star)

    # B3 Đếm số ngôi sao trong bức ảnh
    print("Star in picture:",countStar(matrix)) 
    
    
