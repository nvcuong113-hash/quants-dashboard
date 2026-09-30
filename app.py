import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Smart Money Quants Pro", layout="wide")
st.title("Smart Money & Quants Pro")

st.info("Đang kết nối Google Sheets...")

try:
    # Kết nối Google Sheets bằng service account
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = Credentials.from_service_account_file(
        "service_account.json",
        scopes=scopes
    )
    
    client = gspread.authorize(creds)
    
    # Mở Google Sheet bằng URL
    sheet_url = "https://docs.google.com/spreadsheets/d/1581rcHwai-O4gVnJr3vwnWidqq0BIdrCl9ucrNX-iFY/edit"
    spreadsheet = client.open_by_url(sheet_url)
    
    # Lấy dữ liệu từ tab TheoDoi_DongTien
    worksheet = spreadsheet.worksheet("TheoDoi_DongTien")
    data = worksheet.get_all_records()
    
    df = pd.DataFrame(data)
    
    st.success(f"Kết nối thành công! Đã lấy được {len(df)} dòng dữ liệu.")
    
    # Hiển thị bảng dữ liệu
    st.subheader("Bảng theo dõi dòng tiền")
    st.dataframe(df, use_container_width=True, height=500)
    
except Exception as e:
    st.error("Kết nối thất bại. Lỗi chi tiết:")
    st.write(e)
    st.warning("Hãy kiểm tra lại: 1) File service_account.json đã nằm đúng thư mục chưa 2) Đã share Sheet cho email Service Account chưa")