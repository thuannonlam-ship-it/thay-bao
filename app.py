import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Thầy Bảo Đuổi Học Sinh",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 Game: Thầy Bảo Đuổi Học Sinh")
st.caption("Ứng dụng chạy trên Streamlit & Python")

# --- TRẠNG THÁI GAME (SESSION STATE) ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "lives" not in st.session_state:
    st.session_state.lives = 3
if "teacher_looking" not in st.session_state:
    st.session_state.teacher_looking = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "log_msg" not in st.session_state:
    st.session_state.log_msg = "Nhấn nút để bắt đầu hành động!"

# --- HÀM XỬ LÝ GAME ---
def reset_game():
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.teacher_looking = False
    st.session_state.game_over = False
    st.session_state.log_msg = "Game mới đã bắt đầu! Hãy cẩn thận với Thầy Bảo."

def change_teacher_state():
    # 40% cơ hội thầy quay lại nhìn
    st.session_state.teacher_looking = random.random() < 0.4

def play_phone():
    if st.session_state.game_over:
        return
    
    change_teacher_state()
    
    if st.session_state.teacher_looking:
        st.session_state.lives -= 1
        st.session_state.log_msg = "❌ BỊ PHÁT HIỆN! Thầy Bảo đã ghi tên bạn vào sổ đầu bài!"
        if st.session_state.lives <= 0:
            st.session_state.game_over = True
            st.session_state.log_msg = f"💀 GAME OVER! Bạn đã bị đuổi học với {st.session_state.score} điểm!"
    else:
        st.session_state.score += 10
        st.session_state.log_msg = "📱 Lướt TikTok/Chơi game an toàn! +10 điểm."

def study_hard():
    if st.session_state.game_over:
        return
    
    change_teacher_state()
    
    if st.session_state.teacher_looking:
        st.session_state.score += 5
        st.session_state.log_msg = "📚 Thầy Bảo đi qua và khen bạn chăm học! +5 điểm."
    else:
        st.session_state.log_msg = "📖 Bạn đang ngồi giả vờ học bài..."

# --- GIAO DIỆN HIỂN THỊ ---

# Bảng chỉ số
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🏆 Điểm số", value=st.session_state.score)
with col2:
    st.metric(label="❤️ Mạng còn lại", value=st.session_state.lives)

st.markdown("---")

# Cảnh báo trạng thái của Thầy
if st.session_state.teacher_looking:
    st.error("🚨 **CẢNH BÁO:** THẦY BẢO ĐANG QUAY LẠI NHÌN!")
else:
    st.success("😎 **AN TOÀN:** Thầy Bảo đang nhìn đi chỗ khác.")

st.info(st.session_state.log_msg)

st.markdown("---")

# Nút thao tác
if not st.session_state.game_over:
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.button("📱 Lướt Điện Thoại (+10 điểm)", on_click=play_phone, use_container_width=True)
    with btn_col2:
        st.button("📚 Giả Vờ Học Bài (An toàn)", on_click=study_hard, use_container_width=True)
else:
    st.button("🔄 Chơi Lại", on_click=reset_game, type="primary", use_container_width=True)

# Hướng dẫn
with st.expander("❓ Hướng dẫn cách chơi"):
    st.write("""
    1. **Lướt điện thoại:** Nhận được **10 điểm**, nhưng nếu Thầy Bảo đang nhìn thì sẽ bị **mất 1 mạng**.
    2. **Giả vờ học bài:** An toàn 100%. Nếu Thầy Bảo quay lại nhìn đúng lúc bạn đang học, bạn nhận được **5 điểm thưởng**.
    3. Mất hết **3 mạng** sẽ bị đuổi học (Game Over)!
    """)
