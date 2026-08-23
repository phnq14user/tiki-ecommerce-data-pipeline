import os
import pandas as pd

def transform_tiki_data(input_file="data/raw/tiki_products.csv"):
    """
    Hàm làm sạch và chuẩn hóa dữ liệu thô từ Tiki
    """
    if not os.path.exists(input_file):
        print(f"❌ Không tìm thấy file dữ liệu thô: {input_file}")
        return pd.DataFrame()

    print(f"--> Đang đọc và làm sạch dữ liệu từ: {input_file}...")
    df = pd.read_csv(input_file)

    # 1. Loại bỏ các dòng trùng lặp (nếu có)
    df = df.drop_duplicates(subset=["id"])

    # 2. Xử lý giá trị bị thiếu (Missing values / NULL)
    df["rating"] = df["rating"].fillna(0.0)
    df["discount_rate"] = df["discount_rate"].fillna(0)
    df["quantity_sold"] = df["quantity_sold"].fillna(0)

    # 3. Chuẩn hóa kiểu dữ liệu
    df["id"] = df["id"].astype(str)
    df["price"] = df["price"].astype(float)
    df["rating"] = df["rating"].astype(float)
    df["discount_rate"] = df["discount_rate"].astype(int)
    df["quantity_sold"] = df["quantity_sold"].astype(int)

    # 4. Tính toán thêm cột chỉ số kinh doanh (Feature Engineering)
    # Tính doanh thu ước tính = giá bán * số lượng đã bán
    df["estimated_revenue"] = df["price"] * df["quantity_sold"]

    print("✅ Đã hoàn thành quá trình Transform dữ liệu!")
    return df

if __name__ == "__main__":
    # 1. Chạy hàm biến đổi dữ liệu
    df_cleaned = transform_tiki_data()

    if not df_cleaned.empty:
        # 2. Tạo thư mục data/processed nếu chưa có
        os.makedirs("data/processed", exist_ok=True)

        # 3. Lưu file CSV dữ liệu sạch
        output_path = "data/processed/tiki_products_cleaned.csv"
        df_cleaned.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f"✅ Đã lưu dữ liệu sạch vào: {output_path}")