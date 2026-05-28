import session
from db import fileManager

OPT_EXIT = "0"
OPT_SIGN_UP = "1"
OPT_SIGN_IN = "2"
OPT_SIGN_OUT = "3"
OPT_MODIFY = "4"
OPT_BANK = "5"
OPT_MEMO = "6"
OPT_TODO = "7"

onRunning = True


def display(opt):
    text = ""
    if opt:
        text = ""
    else:
        text = (
            f"{OPT_SIGN_UP}. 회원가입 "
            f"| {OPT_SIGN_IN}. 로그인 "
            f"| {OPT_EXIT}. 종료 "
        )

    print(text)


def exit():
    global onRunning
    onRunning = False


signInActions = {
    OPT_SIGN_OUT: None,
    OPT_MODIFY: None,
    OPT_BANK: None,
    OPT_MEMO: None,
    OPT_TODO: None,
}

signOutActions = {
    OPT_EXIT: exit,
    OPT_SIGN_UP: None,
    OPT_SIGN_IN: None,
}

fileManager.startCaching()


def main():
    while onRunning:
        display(session.onSignIned())
        selected = input(": ")

        if session.onSignIned():
            action = signInActions.get(selected)
            action() if action else None

        else:
            action = signOutActions.get(selected)
            action() if action else None


if __name__ == "__main__":
    main()

"""
로그인 아닌 상태
- sign-up
- sign-in
- 뱅크 접근
- 메모 접근
- 투두 접근

로그인 중인 상태
- sing-out
- modify
- delete
- 뱅크 접근
- 메모 접근
- 투두 접근
"""
# 메모 기능 부분
import memo        # 메모의 기능(모듈)
import session     # 현재 로그인
import memoUI      # 메모장 형태 UI  테스트 단계 위험

session.loginId = "user01"

while True:
    print("\n===== 메모 메뉴 =====")
    print("1. 메모 작성")
    print("2. 메모 조회")
    print("3. 메모 수정")
    print("4. 메모 삭제")
    print("5. 키워드 검색")
    print("0. 종료")

    menu = input("메뉴 선택: ")

    if menu == "1":
        memo.writeMemo()
        # memo_ui.writeMemoUI()   UI 버전 재미용

    elif menu == "2":
        memo.readMemo()

    elif menu == "3":
        memo.updateMemo()

    elif menu == "4":
        memo.deleteMemo()

    elif menu == "5":
        memo.searchMemo()

    elif menu == "0":
        break

    else:
        print("잘못된 입력입니다.")