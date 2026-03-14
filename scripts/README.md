# Scripts — Công cụ Python cho Lecture Notes Thuật Toán

Tổng hợp 32 script Python được viết trong quá trình xây dựng `LECTURE_NOTES_ALGORITHMS.tex`.

## 📊 Thêm nội dung (Content Generation)

| Script | Chức năng |
|---|---|
| `add_solutions.py` | Thêm lời giải mẫu vào chương bài tập |
| `add_cx_tables.py` | Thêm bảng complexity cho các thuật toán |
| `add_table_captions.py` | Thêm caption và label cho bảng |
| `add_li_cx.py` | Thêm complexity vào list items |
| `add_paradigms.py` | Thêm so sánh paradigms (Greedy/D&C/DP) |
| `add_dp_tables.py` | Thêm bảng Dynamic Programming |
| `add_greedy_tables.py` | Thêm bảng Greedy |
| `add_fib_tables.py` | Thêm bảng Fibonacci |

## 🔧 Sửa lỗi (Fixes)

| Script | Chức năng |
|---|---|
| `fix_tables2.py` / `fix_tables3.py` | Sửa format bảng LaTeX |
| `fix_labels.py` | Sửa label trùng lặp |
| `fix_numbering.py` | Sửa đánh số section |
| `fix_cellcolor.py` / `fix_cellcolor2.py` | Sửa cellcolor trong bảng |
| `fix_dup.py` | Xóa nội dung trùng lặp |

## 🔄 Chuyển đổi (Conversion)

| Script | Chức năng |
|---|---|
| `replace_dijkstra.py` | Thay thế đồ thị Dijkstra |
| `merge_dijkstra.py` | Gộp phần Dijkstra |
| `standardize_sort.py` | Chuẩn hóa format sorting sections |
| `convert_pseudocode.py` | Chuyển đổi format pseudocode |
| `number_subsubs.py` / `number_subsubs2.py` | Đánh số subsubsection |
| `find_pairs.py` | Tìm cặp vertex cho đồ thị |

## 🔍 Kiểm tra (Verification)

| Script | Chức năng |
|---|---|
| `verify_kruskal.py` / `verify_kruskal2.py` | Verify Kruskal algorithm trace |
| `verify_prim.py` | Verify Prim algorithm trace |
| `audit_cx_tables.py` | Audit bảng complexity |
| `audit_math.py` → `audit_math4.py` | Audit ký hiệu toán học |
| `check_mcm.py` | Check Matrix Chain Multiplication |

## 🎙️ Audio

| Script | Chức năng |
|---|---|
| `tts_demo.py` | Demo TTS Heap Sort (file gốc) |

> **Lưu ý:** Pipeline audio chính là `../tex_to_audio.py` (ở thư mục gốc).

## Cách dùng

Các script này được thiết kế để chạy 1 lần trên file `.tex`. Nếu cần dùng lại:

```bash
cd ~/Downloads/thuattoan
python3 scripts/verify_kruskal2.py   # ví dụ
```
