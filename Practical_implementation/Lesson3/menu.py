def main():
    student_system = StudentManagement()
    
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ SINH VIÊN ---")
        print("1. Thêm sinh viên mới")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Sắp xếp theo GPA (Bubble Sort)")
        print("4. Sắp xếp theo tên (Insertion Sort)")
        print("5. Sắp xếp theo tuổi (Selection Sort)")
        print("6. Tìm kiếm sinh viên theo MSSV")
        print("0. Thoát")
        
        try:
            choice = input("Nhập lựa chọn của bạn: ").strip()
            
            if choice == '1':
                student_system.add_student()
            elif choice == '2':
                student_system.display_students()
            elif choice == '3':
                student_system.bubble_sort_gpa()
            elif choice == '4':
                student_system.insertion_sort_name()
            elif choice == '5':
                student_system.selection_sort_age()
            elif choice == '6':
                student_system.search_by_mssv()
            elif choice == '0':
                print("Kết thúc chương trình. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()