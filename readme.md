# TEST CASE THE BEST VIETNAM WORD SEGMENT TOOL

## Để chạy được chương trình cần cài đặt:
	* Java Runtime Environment
	* Windows Runtime Environment
## Dữ liệu
Dữ liệu để test gồm 2 bộ :
	* 7.000 câu Tiếng Việt (khoảng 2 triệu âm tiết).
	* 70.000 câu Tiếng Việt.
lấy từ VLSP

## Chạy chương trình:

Đê format dataset chạy:
    ```
    cd testcaseVN
    ./formatDataset.exe -i [input-dataset-folder] -o [output-dataset-folder]
    ```
Trong đó:
    * input-dataset-folder là folder cần format.
    * output-dataset-folder là folder lưu kết quả sau khi format.

Ví dụ:
    ```
    ./formatDataset.exe -i Input -o Output
    ```

Để chạy chương trình đánh giá:
    ```
    cd testcaseVN
    ./testcase.exe -i [input-dataset-folder] -o [output-dataset-folder] -t [tool]
    ```

Trong đó:
    * [input-dataset-folder] là folder input datasets.
    * [output-dataset-folder] là folder output datasets.
    * [tool] là tên tool gồm : dongdu, jvntextpro, vntokenizer, all

Ví dụ:
    ```
    ./testcase.exe -i Data\Input -o Data\Output -t dongdu
    ```

Kết quả sẽ được lưu vào file tương ứng:
    * Với opt -t all kết quả được lưu vào file "ketqua.txt".
    * Với opt -t jvntextpro kết quả được lưu vào file "jvntextpro.txt".
    * Với opt -t vntokenizer kết quả được lưu vào file "vntokenizer.txt".
    * Với opt -t dongdu kết quả được lưu vào file "dongdu.txt".

Về RAM:
    * vnTokenizer: 535mb
    * Dongdu: 19 mb
    * JVnTextpro: 550mb