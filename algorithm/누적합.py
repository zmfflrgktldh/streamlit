import streamlit as st
st.header("누적합")
st.subheader("문제 설명")
number=[5,2,7,6,1,8,3,9,4,10]
st.code('''number=[5,2,7,6,1,8,3,9,4,10]''')
st.markdown('''질문을 합니다.
1. 3~7번의 합
2. 5~10번의 합
3. 2~6번의 합
4. 1~10번의 합
''')
st.divider()
st.subheader("범부의 풀이")
with st.echo():
    number=[5,2,7,6,1,8,3,9,4,10]
    quiz=[
        [3,7],
        [5,10],
        [2,6],
        [1,10]
    ]
    for s,e in quiz:
        result=0
        for i in range(s-1,e):
            result+=number[i]
        st.write(result)
st.divider()
st.subheader("천재의 풀이")
with st.echo():
    number=[5,2,7,6,1,8,3,9,4,10]
    quiz=[
        [3,7],
        [5,10],
        [2,6],
        [1,10]
    ]
    누적합=[0]
    for num in number:
        누적합.append(누적합[-1]+num)

    for s,e in quiz:
        st.write(누적합[e]-누적합[s-1])
    print(누적합)