import streamlit as st
from PIL import Image, ImageOps

# 페이지 설정에서 favicon.ico 변경
st.set_page_config(
    page_title="Verde",  # 페이지 제목 설정
    page_icon="images/icon.ico",  # 아이콘 파일 경로 설정
    layout="centered"  # 레이아웃 설정 (옵션)
)

# 로고 이미지 불러오기
logo = Image.open("images/logo.jpg")

# 중앙에 배치할 수 있도록 열을 설정
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")  # 왼쪽 빈 공간
with col2:
    st.image(logo, use_column_width=True)  # 중앙 열에 이미지 배치
with col3:
    st.write("")  # 오른쪽 빈 공간

# Streamlit 헤더와 메뉴를 숨기는 CSS
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 이미지 파일 불러오기
img1 = Image.open("images/img1.jpg")
img2 = Image.open("images/img2.jpg")
img3 = Image.open("images/img3.jpg")

# img4의 크기와 동일하게 만들기 위해 크기 가져오기
target_width, target_height = img2.size

# img3을 90도 회전시키기
img3_rotated = img3.rotate(-90, expand=True)

# img1과 img3_rotated를 img2의 크기에 맞추기 위해 확대
new_img1_final = ImageOps.fit(img1, (target_width, target_height), method=Image.Resampling.LANCZOS)
img3_rotated_final = ImageOps.fit(img3_rotated, (target_width, target_height), method=Image.Resampling.LANCZOS)


# 이미지를 중앙에 정렬하여 나열
col1, col2, col3 = st.columns(3)
with col1:
    st.image(new_img1_final, use_column_width=True)
with col2:
    st.image(img2, use_column_width=True)
with col3:
    st.image(img3_rotated_final, use_column_width=True)


# 이미지 파일 불러오기
img4 = Image.open("images/img4.jpg")
img5 = Image.open("images/img5.jpg")
img6 = Image.open("images/img6.jpg")

# img4의 크기와 동일하게 만들기 위해 크기 가져오기
target_width, target_height = img4.size

# img2를 세로로 늘리기 위해 위아래에 검정색 배경 추가
new_height = img5.height + 555  # 기존 높이에서  추가
new_img5 = Image.new("RGB", (img5.width, new_height), (0, 0, 0))  # 검정색 배경 생성
new_img5.paste(img5, (0, 275))  # 중앙에 원본 이미지 붙여넣기

# img1의 윗부분을 자르기 (이미지 높이의 1/4를 자른다고 가정)
crop_height = img6.height // 5  # 윗부분 1/4 자르기
img6_cropped = img6.crop((0, crop_height, img6.width, img6.height))

# img5와 img6_cropped을 img4의 크기에 맞추기
new_img5_final = ImageOps.pad(new_img5, (target_width, target_height), color=(0, 0, 0))
img6_cropped_final = ImageOps.pad(img6_cropped, (target_width, target_height), color=(0, 0, 0))

# 이미지를 중앙에 정렬하여 나열
col1, col2, col3 = st.columns(3)
with col1:
    st.image(img4, use_column_width=True)
with col2:
    st.image(new_img5_final, use_column_width=True)
with col3:
    st.image(img6_cropped_final, use_column_width=True)

insta = Image.open("images/insta.jpg")

width, height = insta.size

# 위아래로 여백 추가 (총 이미지 높이의 두 배 만큼)
new_height = height * 3  # 이미지 위와 아래에 이미지 높이만큼 추가
new_image = Image.new("RGB", (width, new_height), (255, 255, 255))  # 흰색 배경 생성 (또는 원하는 색상)
new_image.paste(insta, (0, height))  # 가운데에 원본 이미지 붙여넣기

# 이미지 출력
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")  # 왼쪽 빈 공간
with col2:
    st.image(new_image, use_column_width=True)
with col3:
    st.write("")  # 오른쪽 빈 공간



# 링크가 포함된 텍스트를 Markdown으로 작성
st.markdown(
    """<div style="text-align: center;">
     <a href="https://www.instagram.com/vesverde?igsh=MW5hdHJucWN6dmx6bA%3D%3D&utm_source=qr" target="_blank ">instagram.com/vesverde</a>
    </div><br><br>
    """, unsafe_allow_html=True)

img10 = Image.open("images/img10.jpg")
img11 = Image.open("images/img11.jpg")
img12 = Image.open("images/img12.jpg")

col1, col2, col3 = st.columns(3)
with col1:
    st.image(img10, use_column_width=True)
with col2:
    st.image(img11, use_column_width=True)
with col3:
    st.image(img12, use_column_width=True)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.markdown(
"""
<div style="font-size:12px;">
✿ 아이폰 15pro<br><br>
✿ 당일 카톡 전송<br><br>
✿ 예약 인스타그램 DM<br><br>
✿ 후기 작성시 디카로 5장 이상 찍어드리고, 감사카드를 만들어 드립니다.<br><br>
✿ 초상권 비동의시 얼굴을 제외한 모습이 게시될 수 있습니다.<br><br>
✿ 계약 후 예식 7일 전 유선상담, 당일 예식 1시간 전 도착입니다.<br><br>
✿ 본스냅 업체에 아이폰스냅 가능여부 확인 후 예약 부탁드립니다.
</div>
""", unsafe_allow_html=True)

# 여러 줄의 빈 공간 추가
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

img8 = Image.open("images/img8.jpg")

# 이미지를 중앙에 정렬하여 나열
col1, col2 = st.columns([1, 2])  # 두 개의 열로 나누고, col2를 더 넓게 설정

with col1:
    st.image(img8, use_column_width=True)


with col2:
    st.markdown(
        """
        <div style="font-size:12px;">
        <b>Seoul, iPhone</b><br>
        We provide iPhone photography service.<br><br>
        © 2024. Verde all photos shall not be copied without permission.<br>
        </div>
        """, unsafe_allow_html=True)






