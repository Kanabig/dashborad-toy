from memberService import session
from memberService import memberService

# import memo

OPT_EXIT = "0"
OPT_SIGN_UP = "1"
OPT_SIGN_IN = "2"
OPT_SIGN_OUT = "3"
OPT_MODIFY = "4"
OPT_BANK = "5"
OPT_MEMO = "6"
OPT_TODO = "7"

onRunning = True


def exit():
    global onRunning
    onRunning = False


def notImplemented():
    print("아직 구현되지 않은 기능입니다.")


# def memoLoop():
#     while True:
#         print("\n===== 메모 메뉴 =====")
#         print("1. 메모 작성")
#         print("2. 메모 조회")
#         print("3. 메모 수정")
#         print("4. 메모 삭제")
#         print("5. 키워드 검색")
#         print("0. 종료")

#         menu = input("메뉴 선택: ")

#         if menu == "1":
#             memo.writeMemo()
#             # memo_ui.writeMemoUI()   UI 버전 재미용

#         elif menu == "2":
#             memo.readMemo()

#         elif menu == "3":
#             memo.updateMemo()

#         elif menu == "4":
#             memo.deleteMemo()

#         elif menu == "5":
#             memo.searchMemo()

#         elif menu == "0":
#             break

#         else:
#             print("잘못된 입력입니다.")


signInedActions = {
    OPT_SIGN_OUT: memberService.signOut,
    OPT_MODIFY: notImplemented,
    OPT_BANK: notImplemented,
    OPT_MEMO: notImplemented,
    OPT_TODO: notImplemented,
}

signOutActions = {
    OPT_EXIT: exit,
    OPT_SIGN_UP: memberService.signUp,
    OPT_SIGN_IN: memberService.signIn,
}


def makePromptAndActions(onSignedIn):
    text = ""
    actions = {}

    if onSignedIn:
        text = (
            f"{OPT_SIGN_OUT}. 로그아웃 "
            f"| {OPT_MODIFY}. 회원 정보 수정 "
            f"| {OPT_BANK}. 계좌 "
            f"| {OPT_MEMO}. 메모 "
            f"| {OPT_TODO}. 투두리스트 "
        )
        actions = signInedActions

    else:
        text = (
            f"{OPT_SIGN_UP}. 회원가입 "
            f"| {OPT_SIGN_IN}. 로그인 "
            f"| {OPT_EXIT}. 종료 "
        )
        actions = signOutActions

    return (text, actions)


def main():
    # fileManager.dbLoadFromFile()

    while onRunning:
        prompt, actions = makePromptAndActions(session.onSignIned())
        selected = input(f"\n{prompt}\n:")

        action = actions.get(selected)
        action() if action else None


if __name__ == "__main__":
    from db_ver2 import fileManager

    main()
