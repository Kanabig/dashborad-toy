from db import dbManager
from memberService import session


def isExistsId(id):
    return id in dbManager.getMemberIds()


def isValidAccount(id, pw):
    if isExistsId(id):
        if pw == dbManager.getMemberPw(id):
            return True


def signUp():
    id = input("아이디: ")

    if isExistsId(id):
        print("중복된 아이디입니다.")
        return

    pw = input("패스워드: ")
    mail = input("이메일: ")
    phone = input("전화번호: ")
    bankAcnt = input("계좌번호: ")

    print("회원가입에 성공했습니다.")
    dbManager.createMember(id, pw, mail, phone, bankAcnt)


def signIn():
    id = input("아이디: ")
    pw = input("패스워드: ")

    if not isValidAccount(id, pw):
        print("로그인에 실패했습니다.")
        return

    print("로그인 성공.")
    session.signinedId = id


def signOut():
    print("로그아웃 완료.")
    session.signinedId = ""
