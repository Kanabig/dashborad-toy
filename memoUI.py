# 그냥 해보고 싶어서 만든 UI 사용은  memo_ui.writeMemoUI()

import tkinter as tk  # 파이썬에 창,버튼,입력칸에 쓰이는 기본틀
import memo           # 메모에 적용하기 위해서


def writeMemoUI():    # 메모 작성 창을 띄우기 위한 함수

    writeWindow = tk.Tk()   #창모양을 담는 함수

    writeWindow.title("메모 작성")  # 창 안에 title 제목안에 넣는 칸
    writeWindow.geometry("300x200")   # 가로 x 세로 크기를 정하는 부분

    textBox = tk.Text(writeWindow, width=30, height=5)  # 제목안에 넣는 부분크기
    textBox.pack(pady=10)  # 그 제목안에 여백을 얼마나 넣을것인지

    def saveMemo():   # 버튼 실행 함수

        text = textBox.get("1.0", tk.END).strip()  # 입력칸에 적은 내용가져오는 코드
        # textBox.get() 박스 크기 안에 글자를 가져온다.(첫번째 줄, 0번째 글자)

        if text:    # 입력한 내용이 있을때만 저장하는 느낌

            id = memo.session.loginId   # 현재 아이디
            
            # 딕셔너리
            memoData = {
                memo.config.MEMO_DATE:
                memo.datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),

                memo.config.MEMO_TEXT:
                text
            }

            if id not in memo.memoDb.memoDb:
                memo.memoDb.memoDb[id] = []

            memo.memoDb.memoDb[id].append(memoData)    # 메모 리스트 적용

            print("메모 저장 완료")

            writeWindow.destroy()     # 창 모양을 닫는 코드

    saveBtn = tk.Button(        # 버튼모양 만드는 부분
        writeWindow,            # 버튼 창 모양
        text="작성 완료",        # 버튼안에 보일 글자
        command=saveMemo       # 실행
    )

    saveBtn.pack(pady=10)     # 버튼이 보이게 여백을 넣는것(pady)

    writeWindow.mainloop()   # 창모양 계속 띄우기