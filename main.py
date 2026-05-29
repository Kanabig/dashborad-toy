from memberService import session
from memberService import memberService
from memoService import memo
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


def exit():
    global onRunning
    onRunning = False
    fileManager.dbSaveAllAtFile()


def notImplemented():
    print("아직 구현되지 않은 기능입니다.")


signInedActions = {
    OPT_SIGN_OUT: memberService.signOut,
    OPT_MODIFY: notImplemented,
    OPT_BANK: notImplemented,
    OPT_MEMO: memo.memoLoop,
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
    fileManager.dbLoadAllFromFile()

    while onRunning:
        prompt, actions = makePromptAndActions(session.onSignIned())
        selected = input(f"\n{prompt}\n:")

        action = actions.get(selected)
        action() if action else None

    fileManager.dbSaveAllAtFile()


if __name__ == "__main__":
    from db import fileManager

    main()
