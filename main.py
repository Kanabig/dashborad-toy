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
