import streamlit as st

# Tiêu đề ứng dụng
st.set_page_config(page_title="VP-AI", layout="wide")
st.title("AI hỗ trợ chẩn đoán viêm phổi")

# Nhập các triệu chứng lâm sàng và cận lâm sàng
st.subheader("Nhập dữ liệu bệnh nhi:")
age = st.number_input("Tuổi", min_value=0, max_value=18, value=1)
fever = st.checkbox("Sốt")
cough = st.checkbox("Ho")
difficulty_breathing = st.checkbox("Khó thở")
wheezing = st.checkbox("Rì rào phế nang giảm")
crp = st.number_input("CRP (mg/L)", min_value=0.0, step=0.1)
wbc = st.number_input("Số lượng bạch cầu (G/L)", min_value=0.0, step=0.1)

# Nút dự đoán
if st.button("Dự đoán vi khuẩn gây bệnh"):
    st.success("🦠 Khả năng cao là *Haemophilus influenzae* hoặc *Streptococcus pneumoniae*")
    st.info("💊 Gợi ý kháng sinh: Ceftriaxone, Ampicillin, hoặc Levofloxacin (tùy tình huống lâm sàng)")
