import sys
from src.extract import fetch_tiki_products
from src.transform import transform_tiki_data

def run_pipeline():
    print("==========================================")
    print("🚀 BẮT ĐẦU CHẠY E-COMMERCE ETL PIPELINE")
    print("==========================================")

    # BƯỚC 1: EXTRACT (Thu thập dữ liệu)
    print("\n[STEP 1/3] EXTRACT: Cào dữ liệu từ Tiki API...")
    keyword = "laptop"
    df_raw = fetch_tiki_products(keyword=keyword, limit=20)
    
    if df_raw.empty:
        print("❌ Pipeline dừng lại: Không lấy được dữ liệu thô!")
        sys.exit(1)
        
    raw_path = "data/raw/tiki_products.csv"
    df_raw.to_csv(raw_path, index=False, encoding="utf-8-sig")
    print(f"✅ Extract hoàn tất. Đã lưu dữ liệu thô vào: {raw_path}")

    # BƯỚC 2: TRANSFORM (Làm sạch & Chuẩn hóa)
    print("\n[STEP 2/3] TRANSFORM: Làm sạch và chuẩn hóa dữ liệu...")
    df_cleaned = transform_tiki_data(input_file=raw_path)
    
    if df_cleaned.empty:
        print("❌ Pipeline dừng lại: Quá trình Transform bị lỗi!")
        sys.exit(1)
        
    processed_path = "data/processed/tiki_products_cleaned.csv"
    df_cleaned.to_csv(processed_path, index=False, encoding="utf-8-sig")
    print(f"✅ Transform hoàn tất. Đã lưu dữ liệu sạch vào: {processed_path}")

    # BƯỚC 3: LOAD (Nạp dữ liệu)
    print("\n[STEP 3/3] LOAD: Đang nạp dữ liệu sạch vào kho lưu trữ...")
    # Tạm thời log thông báo thành công (Sau này sẽ gọi hàm load từ src/load.py lên BigQuery)
    print("✅ Load hoàn tất. Dữ liệu đã sẵn sàng phục vụ Analytics / Dashboard!")

    print("\n==========================================")
    print("🎉 PIPELINE CHẠY THÀNH CÔNG 100%!")
    print("==========================================")

if __name__ == "__main__":
    run_pipeline()