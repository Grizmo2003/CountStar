# Counting Star

###### Chương trình cho phép người dùng nhập vào bức ảnh sau đấy sẽ in ra màn hình console kết quả là số ngôi sao có trong bức ảnh đó.



### A. Logic cơ bản
#### 1. Ảnh được tạo ra như thế nào ?
Mỗi 1 bức ảnh được tạp nên từ các pixel và với mỗi pixel có các giá trị màu trong bảng màu RBG trong đoạn [0-255]. Dễ hiểu như các pixel giống như các tấm thảm trải trên 1 nền nhà to vậy bức ảnh càng sắc nét nếu có càng nhiều điểm ảnh (pixel) mỗi pixel sẽ có các màu như Xanh, Đỏ, Tím, Vàng,... và mỗi màu ấy có 1 giá trị RBG riêng ký hiệu là <Color> = [Red, Blue, Green] (Ví dụ Đen = [0, 0, 0]; Trắng [255, 255, 255]; Đỏ [255, 0, 0]...).
#### 2. Các loại ảnh
Trong cuộc sống có rất nhiều các bức ảnh như: Ảnh chân dung, ảnh núi đồi, ảnh biển, ảnh chụp bài tập, ảnh chụp giáo trình, ảnh x-quang, ảnh quân sự,... tuy nhiên có thể chia các nhóm ảnh thành các nhóm như sau:
+ Ảnh Phong cảnh: Những bức ảnh bình thường chúng ta hay chụp (Ảnh người, ảnh chó mèo, ảnh núi đồi,...)

+ Ảnh Y tế: Các bức ảnh từ y tế là những bức ảnh được sử dụng trong việc khám chữa bệnh của hệ thống y tế (Ảnh X-Quang, ảnh siêu âm,...)

+ Ảnh quân sự: Các bức ảnh dạng này cho phép nhận dạng các hoạt động của đối phương, xác định tọa độ của kẻ địch, phát hiện hầm hào, vũ khí,... nhằm giúp cải thiện khả năng chiến đấu cũng như các mục đích quân sự khác  

+ Ảnh Tài liệu: Các bức ảnh chụp có phần chữ và xử lý phần chữ trong bức ảnh (Scan chữ viết tay thành file word, Chụp màn hình tự chuyển về file text để xử lý) Hiện nay có rất nhiều chương trình tuy nhiên lại có rất ít module tiếng việt nên và hiệu quả chính xác chưa quá cao ( Chỉ khoảng 80%) nên đây vẫn là 1 trong những hướng đi khá tích cực đặc biệt là với Việt Nam

+ Ảnh vệ tinh: Những bức ảnh chụp trái đất từ các vệ tinh (Ảnh bản đồ, ảnh địa chất,...) mặc dù có thể thấy nó rất phổ biến tuy nhiên đây lại là một loại ảnh mới ở Việt Nam vì Data về ảnh còn quá ít chưa cho phép người Việt đủ điều kiện để hoàn thành. Các bức ảnh được nhìn thấy bằng mắt thường thì đều đã được qua xử lý (Loại bỏ mây, máy bay, những vật thể giảm sự quan sát tới bề mặt,...)
#### 3. Các vấn đề về cở bản của xử lý ảnh
Có 3 giai đoạn chính trong công việc xử lý ảnh:
#### *Tiền xử lý
- Ở giai đoạn này chương trình sẽ thực hiện khử nhiễu (Khử những thứ không mong muốn )
- Input: Ảnh
- Output: Ảnh

#### *Xử lý
- Ở giai đoạn này từ những bức ảnh chúng ta đưa về những đặc trưng của bức ảnh ( Dễ hiểu là những đặc điểm nhận dạng của đối tượng, Ví dụ như đặc điểm nhận dạng cơ thể của bạn)
- Input: Ảnh 
- Ouput: Vector (Matrix)

#### * Understanding
- Ở giai đoạn này chúng ta sẽ dựa vào những đặc trưng của 1 loại ảnh để tiến hành xử lý tiếp (Hiểu được vật thể trong ảnh đang làm gì: Ví dụ máy tính sẽ đưa ra được kết quả y hệt như con người nhìn vào và có thể miêu tả được chính xác truyện gì đang diễn ra trong bức ảnh)

### B. Thuật toán 
#### Bước 1: Tiền xử lý
Ở phần này chúng ta sẽ khử nhiễu hay đưa các bức ảnh có dạng [0-255] về dạng [0-1] tức chỉ bao gồm trắng đen. Khi đó bức ảnh sẽ chỉ còn lại 2 đối tượng cần xét là: Phần ngồi sao và phần bầu trời

#### Bước 2: Xử lý
Sau khi bức ảnh đã được chuyển về dạng ảnh nhị phân, chúng ta sẽ đưa chuyển các điểm ảnh hay pixel thành các phần tử trong 1 bảng giá trị qua đó chuyển về ma trận dạng đơn giản nhất. 

#### Bước 3: Xử lý
dựa vào các ma trận từ bước trên bắt đầu đếm số ngôi sao có trên bức ảnh với các thành phần trên một ngôi sao được tính là các phần nằm cạnh nhau.

#### Bước 4: Understanding
< Đang triển khai>