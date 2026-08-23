# 🚀 End-to-End E-Commerce Data Pipeline (Tiki API to BigQuery & Looker Studio)
📊 **Live Dashboard**: [Bấm vào đây để xem báo cáo Looker Studio](https://datastudio.google.com/reporting/4f94eae8-0790-4d4f-a892-2e33156f901a)
Dự án xây dựng luồng tự động hóa dữ liệu (ETL Pipeline) cào dữ liệu từ Tiki API, làm sạch dữ liệu bằng Python (Pandas), lưu trữ tại kho dữ liệu đám mây Google BigQuery và trực quan hóa báo cáo trên Looker Studio.

---

## 🏗️ Kiến trúc Pipeline (Architecture)

```text
[Tiki API] ➡️ (Extract) ➡️ [Raw Data / CSV] ➡️ (Transform) ➡️ [Pandas Cleaned Data] ➡️ (Load) ➡️ [Google BigQuery] ➡️ [Looker Studio Dashboard]