import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Stream 入門')

st.write('Displa Image')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.write(df) #ノーマル表
st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000) #いろいろ機能ある
st.table(df.style.highlight_max(axis=0)) #静的表(ソート機能なし)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df3)

if st.checkbox('show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='beautiful scene', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))

)

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.3)
'done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容書く')

#text = st.text_input('あなたの趣味を教えてください。')
#condition = st.slider('あなたの調子は？',0,100,1)


#'あなたの趣味は', option1, 'です。'
#'コンディション：', condtion