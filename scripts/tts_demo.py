import edge_tts
import asyncio

# Heap Sort lecture script in Vietnamese
text = """
Heap Sort - Sắp xếp bằng Heap.

Ý tưởng chính của Heap Sort gồm 2 bước:

Bước 1: Build Max Heap. 
Biến mảng đầu vào thành một cây max-heap, trong đó phần tử lớn nhất luôn nằm ở gốc.
Tính chất quan trọng: với mảng bắt đầu từ chỉ số 0, nút cha ở vị trí i sẽ có con trái ở vị trí 2i + 1, và con phải ở vị trí 2i + 2.

Bước 2: Extract Max lặp lại.
Lấy phần tử gốc, tức phần tử lớn nhất, đặt vào cuối mảng.
Sau đó giảm kích thước heap đi 1, và gọi Max Heapify để sửa lại cây.
Lặp lại cho đến khi heap chỉ còn 1 phần tử.

Ví dụ minh họa: Cho mảng 5, 3, 8, 1, 4.

Sau bước Build Max Heap, mảng trở thành 8, 4, 5, 1, 3.
Phần tử 8 ở gốc vì nó lớn nhất.

Bước Extract Max đầu tiên: Hoán đổi 8 với phần tử cuối là 3.
Mảng thành: 3, 4, 5, 1 -- phần đang xét -- và 8 đã ở đúng vị trí.
Gọi Max Heapify: 5 đi lên gốc. Kết quả: 5, 4, 3, 1, rồi 8.

Bước Extract Max thứ hai: Hoán đổi 5 với 1.
Mảng: 1, 4, 3 -- phần đang xét -- rồi 5, 8.
Max Heapify: 4 lên gốc. Kết quả: 4, 1, 3, rồi 5, 8.

Tiếp tục cho đến khi mảng được sắp xếp hoàn toàn: 1, 3, 4, 5, 8.

Độ phức tạp: Build Max Heap mất O of n. Mỗi lần Extract Max mất O of log n, và ta làm n - 1 lần.
Tổng: O of n log n -- tương đương Merge Sort nhưng sắp xếp tại chỗ, không cần bộ nhớ phụ.

Nhận xét: Heap Sort không phải stable sort. Nếu cần stable, hãy dùng Merge Sort.
"""

async def main():
    # Vietnamese female voice - HoaiMy
    tts = edge_tts.Communicate(
        text, 
        "vi-VN-HoaiMyNeural",
        rate="-10%",  # slightly slower for lecture
        volume="+0%"
    )
    output_file = "/Users/Apple/Downloads/thuattoan/heapsort_lecture.mp3"
    await tts.save(output_file)
    print(f"✅ Audio saved to: {output_file}")

asyncio.run(main())
