from db import config   # 사용할 이름 기초틀
from db import memoDb   # 메모리에 저장할 더미
from db import dbManager
from memberService import session          # 현재 로그인의 아이디 상태
from memoService import memoUI
import datetime         # 시간


def getLoginId():
    return session.signinedId

def printMemoList(id):
    memoList = dbManager.getMemoList(id)

    for idx, memo in enumerate(memoList):
        print(f'\n{idx + 1}번 메모')
        print(f'날짜: {memo[config.MEMO_DATE]}')
        print(f'내용: {memo[config.MEMO_TEXT]}')

def inputMemoNumber(id, text):
    num = input(text)
        
    if not num.isdigit():
        print('숫자만 입력하세요.')
        return None
    
    num = int(num) - 1

    memoList = dbManager.getMemoList(id)

    if num < 0 or num >= len(memoList):
        print('잘못된 번호입니다.')
        return None

    return num

def writeMemo():        # 메모에 저장할 함수
    id = getLoginId()   # 현재 로그인 가져오기

    memoText = input('메모 입력: ')
    dbManager.createMemo(id, memoText)
    print('메모 저장 완료')


def readMemo():       # 그동안 등록한 메모 출력하는 함수
    id = getLoginId()     # 똑같이 현재 아이디 가져오기

    # 메모가 있는지 체크해서 없으면 없다고 알려주기
    if not dbManager.hasMemo(id):
        print('등록된 메모가 없습니다.')
        return

    printMemoList(id)

    input("계속하려면 아무 키나 입력하십시오: ")


def updateMemo():      # 기존 메모를 수정해줄 함수
    id = getLoginId()

    if not dbManager.hasMemo(id):
        print('수정할 메모가 없습니다.')
        return

    printMemoList(id)

    num = inputMemoNumber(id, '수정할 메모 번호 입력하세요: ')

    if num is None:
        return

    newText = input('새 메모 입력: ')

    dbManager.updateMemo(id, num, newText)

    print('메모 수정 완료')


def deleteMemo():     # 말 그대로 삭제하는 함수
    id = getLoginId()

    if not dbManager.hasMemo(id):
        print('삭제할 메모가 없습니다.')
        return

    printMemoList(id)

    num = inputMemoNumber(id, '삭제할 메모 번호 입력하세요: ')

    if num is None:
        return

    dbManager.deleteMemo(id, num)

    print('메모 삭제 완료')


def searchMemo():      # 키워드를 찾기위한 함수
    id = getLoginId()

    if not dbManager.hasMemo(id):
        print('찾고자 하는 메모내용이 없습니다.')
        return

    keyword = input('검색할 키워드 입력: ')   #찾고 싶은 단어입력

    count = 0

    memoList = dbManager.getMemoList(id)

    for idx, memo in enumerate(memoList):
        if keyword in memo[config.MEMO_TEXT]:
            print(f'\n{idx + 1}번 메모')
            print(f'날짜: {memo[config.MEMO_DATE]}')
            print(f'내용: {memo[config.MEMO_TEXT]}')
            count += 1

    if count == 0:
        print('검색 결과가 없습니다.')

def memoLoop():
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
            writeMemo()
            #memoUI.writeMemoUI()   ###UI 버전 재미용

        elif menu == "2":
            readMemo()

        elif menu == "3":
            updateMemo()

        elif menu == "4":
            deleteMemo()

        elif menu == "5":
            searchMemo()

        elif menu == "0":
            break

        else:
            print("잘못된 입력입니다.")