import os
import requests
import pandas as pd

def fetch_tiki_products(keyword="laptop", limit=10):
    """
    Hàm gọi API của Tiki để lấy thông tin sản phẩm thực tế
    """
    url = f"https://tiki.vn/api/v2/products?limit={limit}&q={keyword}"
    
    # Giả lập Header trình duyệt để tránh bị chặn
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"--> Đang cào dữ liệu cho từ khóa: '{keyword}'...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", [])
        
        # Bóc tách các trường dữ liệu cần thiết
        products = []
        for item in data:
            products.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "price": item.get("price"),
                "rating": item.get("rating_average"),
                "discount_rate": item.get("discount_rate"),
                "quantity_sold": item.get("quantity_sold", {}).get("value", 0)
            })
            
        df = pd.DataFrame(products)
        return df
    else:
        print(f"Lỗi khi gọi API: {response.status_code}")
        return pd.DataFrame()

if __name__ == "__main__":
    # 1. Gọi hàm cào dữ liệu
    df_raw = fetch_tiki_products(keyword="laptop", limit=20)
    
    if not df_raw.empty:
        # 2. Tạo thư mục data/raw nếu chưa có
        os.makedirs("data/raw", exist_ok=True)
        
        # 3. Lưu file CSV vào thư mục data/raw/
        output_path = "data/raw/tiki_products.csv"
        df_raw.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f"✅ Đã lưu {len(df_raw)} sản phẩm vào: {output_path}")