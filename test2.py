from ultralytics import YOLO
import streamlit as st
from PIL import Image
import pandas as pd

#画像アップロード
uploaded_file = st.file_uploader("画像を選択", type=["csv"])

if uploaded_file is not None:
      # 画像の表示
      csv = pd.DataFrame(uploaded_file)
      st.dataframe(csv)

else :
       pass