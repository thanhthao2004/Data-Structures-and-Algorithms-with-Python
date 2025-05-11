class student:
    def __init__(self, masv, hoten, diemtb = None):
        self.masv = masv
        self.hoten = hoten
        self.diemtb = diemtb
    def __str__(self):
        return(f'Mã sinh viên: {self.masv}, Họ và tên: {self.hoten}, Điểm trung bình: {self.diemtb}')
class Queue: 
    def __init__(self):
        self.ds = []
    def is_empty(self):
        return len(self.ds)==0
    def push(self,item):
        self.ds.append(item)
    def pop(self):
        if self.is_empty():
            return 'Rong'
        else:
            self.ds.pop()
    def __str__(self):
        for i in self.ds:
            print(i)
class bst:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    # hướng làm, nếu node chưa có dữ liệu, gán luôn
    # nếu có rồi, so sánh left và right, trống thì gán, không trống thì đệ quy
    def add_node(self, data):
        if self.data is None:
            self.data = data
            print(f"Thêm node đầu tiên: {self.data}")
            return True
        elif self.data == data:
            print("Mã sinh viên trùng")
            return False
        elif self.data.masv > data.masv:
            if self.left is None:
                self.left = bst(data)
                print(f"Thêm vào trái của {self.data.masv}: {data}")
                return True
            else:
                self.left.add_node(data)
        elif self.data.masv < data.masv:
            if self.right is None:
                self.right = bst(data)
                print(f"Thêm vào phải của {self.data.masv}: {data}")
                return True
            else:
                self.right.add_node(data)

    # hướng làm: mở file, dùng 'r' và endcoding = 'utf-8'
    # chạy vòng lặp duyệt từng phần tử i trong file
    # trong vòng lặp, duyệt từng vòng và chia ra các phần thuộc tính bằng cách sử dụng:
            # - strip(): để bỏ qua các phần tử dư thừa
            # - split(''): ở đây cắt bằng dấu phẩy ','
    # sau khi cắt các phần, xử lý nếu giá trị None
    # thêm vào trong lớp đối tượng
    # gọi hàm add_node để thêm đối tượng vào cây
    def read_file_insert(self):
        with open('22684591.txt') as file:
            for i in file:
                part = i.strip().split(',')
                masv = int(part[0].strip())
                hoten = part[1].strip()
                diemtb = float(part[2].strip())
                sv = student(masv,hoten,diemtb)
                self.add_node(sv)

    def NLR(self):
        if self.data:
            print(self.data)
        if self.left:
            self.left.NLR()
        if self.right:
            self.right.NLR()           
    
    # hướng làm: khởi tạo biến đếm, đếm self.data, nếu có self.left và self.right thì + đếm, sau đó đệ quy 2 bên để duyệt
    def count_node_2_child(self):
        dem = 0
        if self.left and self.right:
            dem = 1
        if self.left:
            dem += self.left.count_node_2_child()
        if self.right:
            dem += self.right.count_node_2_child()
        return dem
    
    #hướng làm: nếu mà tìm thấy điểm tb > thì gọi push vào queue, k thấy thì đệ quy
    def find_sv(self,que):
        if self.data and self.data.diemtb > 5:
            que.push(self.data)
            print("đã thêm")
        if self.left:
            self.left.find_sv(que)
        if self.right:
            self.right.find_sv(que)

    # hướng làm: 
    """
        Có 3 trường hợp:
            1. Không có con
                xóa luôn
            2. Có 1 con 
                return giá trị con lên
            3. Có 2 con: tìm phần tử nhỏ nhất để thay thế giá trị
                sử dụng biến tạm:
                    + tìm
                    + gán giá trị nhỏ nhất vào giá trị cần xóa
                    + xóa giá trị nhỏ nhất đó tại cây
    """
    def delete_node(self,masv):
        # duyệt từng phần tử để tìm
        if self.left and self.data.masv > masv:
            self.left = self.left.delete_node(masv)
        elif self.right and self.data.masv < masv:
            self.right = self.right.delete_node(masv)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            elif self.left and self.right:
                temp = self.right
                while temp.left:
                    temp = temp.left
                self.data.masv = temp.data.masv
                self.data.hoten = temp.data.hoten
                self.data.diemtb = temp.data.diemtb
                self.right = self.right.delete_node(temp.data.masv)
        return self
    
    def find_node_1_child(self,ds = None):
        if ds == None:
            ds = []
        if (self.left and self.right is None) or (self.right and self.left is None):
            ds.append(self.data)
        if self.left:
            self.left.find_node_1_child(ds)
        if self.right:
            self.right.find_node_1_child(ds)
        return ds

ql = bst()
que = Queue()
while True:
    print("""
        1.	Đọc file MSSV.txt đổ vô cây nhị phân tìm kiếm (MSSV thay thành của bạn) (1đ)
        Ví dụ: (bạn cần thay đổi lại nội dung file, tối thiểu file phải có 6 dòng)
        001, Nguyen Van A, 4.5
        2.	Duyệt và xuất dữ liệu của cây nhị phân tìm kiếm theo thứ tự NLR (1đ)
        3.	Đếm số nút có 2 con của cây (1đ)
        4.	Tìm các sinh viên có điểm trung bình > 5 lưu vào Queue. (2đ)
        5.	Viết hàm in thông tin trong Queue (1đ)
        6.	Xoá một node có giá trị là MaSV do người dùng nhập (1đ)
        7.	Tìm những nút có 1 con, in ra file MSSV_FindLeaf.txt (2đ)
        8.  Thêm node
        9.	Thoát.
          """)
    choose = int(input("Nhập lựa chọn của bạn: "))
    if choose == 9:
        break
    elif choose == 1:
        ql.read_file_insert()
    elif choose == 2:
        print("Cây BST: ")
        ql.NLR()
    elif choose == 3:
        kq = ql.count_node_2_child()
        print(f'Số lương node có 2 con là: {kq}')
    elif choose == 4:
        ql.find_sv(que)
    elif choose == 5:
        que.__str__()
    elif choose == 6:
        masv = int(input("Nhập mã sinh viên muốn xóa: "))
        ql.delete_node(masv)
        print('Xóa thành công!')
    elif choose == 7:
        kq = ql.find_node_1_child()
        with open('MSSV_FindLeaf.txt','w') as file:
            for i in kq:
                file.write(str(i))
    elif choose == 8:
        n = int(input("Nhập số lượng sinh viên muốn thêm: "))
        for i in range(n):
            masv = int(input("Nhập mã sv: "))
            hoten = input("Nhập họ tên: ")
            diemtb = float(input("Nhập diem tb: "))
            ql.add_node(student(masv, hoten, diemtb))