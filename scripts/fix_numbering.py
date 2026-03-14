with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

import re

# 1. KHUNG NHAN DANG - make unnumbered but keep in bookmarks
content = content.replace(
    r'\section{KHUNG NHẬN DẠNG ĐỀ THI' + '\n' + r'NHANH}\label{khung-nhux1eadn-dux1ea1ng-ux111ux1ec1-thi-nhanh}',
    r'\section*{KHUNG NHẬN DẠNG ĐỀ THI NHANH}\addcontentsline{toc}{section}{KHUNG NHẬN DẠNG ĐỀ THI NHANH}\label{khung-nhux1eadn-dux1ea1ng-ux111ux1ec1-thi-nhanh}'
)

# 2. BAI TAP MAU
content = content.replace(
    r'\section{BÀI TẬP MẪU CÓ LỜI GIẢI}\label{bai-tap-mau}',
    r'\section*{BÀI TẬP MẪU CÓ LỜI GIẢI}\addcontentsline{toc}{section}{BÀI TẬP MẪU CÓ LỜI GIẢI}\label{bai-tap-mau}'
)

# 3. CHEAT SHEET
content = content.replace(
    r'\section{CHEAT SHEET -- TỔNG HỢP}\label{cheat-sheet-tux1ed5ng-hux1ee3p}',
    r'\section*{CHEAT SHEET -- TỔNG HỢP}\addcontentsline{toc}{section}{CHEAT SHEET -- TỔNG HỢP}\label{cheat-sheet-tux1ed5ng-hux1ee3p}'
)

# 4. Loi giai
content = content.replace(
    r'\section{Lời giải -- Tại sao? \& Tự Trace}\label{loi-giai-tai-sao-va-tu-trace}',
    r'\section*{Lời giải -- Tại sao? \& Tự Trace}\addcontentsline{toc}{section}{Lời giải -- Tại sao? \& Tự Trace}\label{loi-giai-tai-sao-va-tu-trace}'
)

# 5. Phu luc
content = content.replace(
    r'\section{Phụ lục: Bảng tên gọi ký hiệu toán học}',
    r'\section*{Phụ lục: Bảng tên gọi ký hiệu toán học}\addcontentsline{toc}{section}{Phụ lục: Bảng tên gọi ký hiệu toán học}'
)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("Done - 5 sections made unnumbered")
