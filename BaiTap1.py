import tkinter as tk
from tkinter import messagebox

def tinhDiemTotNghiep():
    try:
        toan = float(nhapDiemToan.get())
        van = float(nhapDiemVan.get())
        anh = float(nhapDiemAnh.get())
        toHop1 = float(nhapDiemMonToHop1.get())
        toHop2 = float(nhapDiemMonToHop2.get())
        toHop3 = float(nhapDiemMonToHop3.get())
        diemTB12 = float(nhapDiemTrungBinh12.get())
        diemUuTien = float(nhapDiemUuTien.get())
        diemKhuyenKhich = float(nhapDiemKhuyenKhich.get())

        if not (0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10 and
                0 <= toHop1 <= 10 and 0 <= toHop2 <= 10 and 0 <= toHop3 <= 10 and
                0 <= diemTB12 <= 10 and 0 <= diemUuTien <= 10 and 0 <= diemKhuyenKhich <= 10):
            messagebox.showwarning("Lỗi", "Vui lòng nhập điểm trong khoảng từ 0 đến 10!")
            return

        # Tính tổng điểm của 4 bài thi chính cộng với điểm khuyến khích (nếu có)
        tongDiemThi = toan + van + anh + (toHop1 + toHop2 + toHop3)/3
        diemThiTrungBinh = (tongDiemThi + diemKhuyenKhich) / 4

        # Công thức tính điểm tốt nghiệp theo yêu cầu
        diemXetTotNghiep = ((diemThiTrungBinh * 7) + (diemTB12 * 3) + diemUuTien) / 10

        # Kiểm tra học sinh có đủ điều kiện tốt nghiệp hay không (theo quy định là >= 5.0)
        thongBaoKetQua = f"Điểm xét tốt nghiệp của bạn là: {diemXetTotNghiep:.2f}\n"
        if diemXetTotNghiep >= 5.0:
            thongBaoKetQua += "Chúc mừng bạn đã đủ điều kiện tốt nghiệp!"
        else:
            thongBaoKetQua += "Rất tiếc, bạn chưa đủ điều kiện tốt nghiệp."

        messagebox.showinfo("Kết quả", thongBaoKetQua)

    except ValueError:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đúng định dạng số!")

def xoaDuLieu():
    """Xóa dữ liệu từ tất cả các ô nhập liệu."""
    nhapDiemToan.delete(0, tk.END)
    nhapDiemVan.delete(0, tk.END)
    nhapDiemAnh.delete(0, tk.END)
    nhapDiemMonToHop1.delete(0, tk.END)
    nhapDiemMonToHop2.delete(0, tk.END)
    nhapDiemMonToHop3.delete(0, tk.END)
    nhapDiemTrungBinh12.delete(0, tk.END)
    nhapDiemUuTien.delete(0, tk.END)
    nhapDiemKhuyenKhich.delete(0, tk.END)

def help():
    messagebox.showinfo("Hướng dẫn", "Nhập điểm các môn thi, điểm trung bình lớp 12, điểm ưu tiên và điểm khuyến khích (nếu có). Sau đó nhấn 'Tính điểm xét tốt nghiệp' để xem kết quả.")

def exit():
    win.quit()

# Tạo cửa sổ giao diện chính
win = tk.Tk()
win.title("Công cụ tính điểm xét tốt nghiệp trung học phổ thông")
win.iconbitmap("book.ico")
win.geometry("500x350")
win.resizable(False, False)
# Tạo MenuBar
menubar = tk.Menu(win)
# Tạo menu Hệ thống
menu = tk.Menu(menubar, tearoff=0)
menu.add_command(label="Hướng dẫn", command=help)
menu.add_separator()
menu.add_command(label="Thoát", command=exit)
# Thêm menu Hệ thống vào MenuBar
menubar.add_cascade(label="Hệ thống", menu=menu)
# Cài đặt MenuBar cho cửa sổ chính
win.config(menu=menubar)
# Tạo LabelFrame để chứa các ô nhập điểm
frameNhapDiem = tk.LabelFrame(win, text="Nhập điểm của bạn", padx=10, pady=10)
frameNhapDiem.pack(padx=10, pady=10)
# Tạo các nhãn và ô nhập cho từng môn học và điểm liên quan
tk.Label(frameNhapDiem, text="Nhập điểm môn Toán:").grid(row=0, column=0, sticky="w")
nhapDiemToan = tk.Entry(frameNhapDiem)
nhapDiemToan.grid(row=0, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm môn Ngữ văn:").grid(row=1, column=0, sticky="w")
nhapDiemVan = tk.Entry(frameNhapDiem)
nhapDiemVan.grid(row=1, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm môn Anh văn:").grid(row=2, column=0, sticky="w")
nhapDiemAnh = tk.Entry(frameNhapDiem)
nhapDiemAnh.grid(row=2, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm môn Lịch sử (hoặc Vật lí):").grid(row=3, column=0, sticky="w")
nhapDiemMonToHop1 = tk.Entry(frameNhapDiem)
nhapDiemMonToHop1.grid(row=3, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm môn Địa lí (hoặc Hóa học):").grid(row=4, column=0, sticky="w")
nhapDiemMonToHop2 = tk.Entry(frameNhapDiem)
nhapDiemMonToHop2.grid(row=4, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm môn GDCD (hoặc Sinh học):").grid(row=5, column=0, sticky="w")
nhapDiemMonToHop3 = tk.Entry(frameNhapDiem)
nhapDiemMonToHop3.grid(row=5, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm trung bình cả năm lớp 12:").grid(row=6, column=0, sticky="w")
nhapDiemTrungBinh12 = tk.Entry(frameNhapDiem)
nhapDiemTrungBinh12.grid(row=6, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm ưu tiên (nếu có):").grid(row=7, column=0, sticky="w")
nhapDiemUuTien = tk.Entry(frameNhapDiem)
nhapDiemUuTien.grid(row=7, column=1)
tk.Label(frameNhapDiem, text="Nhập điểm khuyến khích (nếu có):").grid(row=8, column=0, sticky="w")
nhapDiemKhuyenKhich = tk.Entry(frameNhapDiem)
nhapDiemKhuyenKhich.grid(row=8, column=1)

buttonFrame = tk.Frame(win)
buttonFrame.pack(pady=10)

buttonTinhDiem = tk.Button(buttonFrame, text="Tính điểm xét tốt nghiệp", command=tinhDiemTotNghiep, bg="green", fg="white")
buttonTinhDiem.grid(row=0, column=0, padx=5)

buttonXoa = tk.Button(buttonFrame, text="Xóa dữ liệu", command=xoaDuLieu, bg="red", fg="white")
buttonXoa.grid(row=0, column=1, padx=5)

win.mainloop()