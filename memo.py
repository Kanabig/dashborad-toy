from db import config   # 사용할 이름 기초틀
from db import memoDb   # 메모리에 저장할 더미
import datetime         # 시간
import session          # 현재 로그인의 아이디 상태


def writeMemo():        # 메모에 저장할 함수

    id = session.loginId   # 현재 로그인 가져오기

    memoText = input('메모 입력: ')

    # 딕셔너리를 이용
    memo = {
        config.MEMO_DATE: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        config.MEMO_TEXT: memoText
    }

    if id not in memoDb.memoDb:       # 현재 아이디의 더미를 생성
        memoDb.memoDb[id] = []

    memoDb.memoDb[id].append(memo)    # 만든 더미에 로그인한 아이디의 메모를 등록

    print('메모 저장 완료')


def readMemo():       # 그동안 등록한 메모 출력하는 함수

    id = session.loginId     # 똑같이 현재 아이디 가져오기

    # 메모가 있는지 체크해서 없으면 없다고 알려주기
    if id not in memoDb.memoDb or len(memoDb.memoDb[id]) == 0:
        print('등록된 메모가 없습니다.')
        return

    # 각 메모에 번호를 등록해주는 단계 > 각 작성물에 인덱스 부여
    for idx, memo in enumerate(memoDb.memoDb[id]):

        print(f'\n{idx + 1}번 메모')   # 번호가 늘어나게 + 1
        print(f'날짜: {memo[config.MEMO_DATE]}')
        print(f'내용: {memo[config.MEMO_TEXT]}')


def updateMemo():      # 기존 메모를 수정해줄 함수

    id = session.loginId  #위와 똑같이 현재 아이디 가져오기

    # 여기도 수정가능하게 있는지 체크 단계 없으면 끝
    if id not in memoDb.memoDb or len(memoDb.memoDb[id]) == 0:
        print('수정할 메모가 없습니다.')
        return

    readMemo()    # 메모를 다시 보고 수정할수 있게

    try:
        num = int(input('수정할 메모 번호 입력하세요: ')) - 1  # 리스트를 사용했기때문에 -1 추가

    except:
        print('숫자만 입력하세요.')
        return

    # 등록한 숫자만큼 보다 높게 입력하는걸 방지
    if num < 0 or num >= len(memoDb.memoDb[id]):
        print("잘못된 번호입니다.")
        return

    newText = input("새 메모 입력: ")

    memoDb.memoDb[id][num][config.MEMO_TEXT] = newText # 내용을 변경

    memoDb.memoDb[id][num][config.MEMO_DATE] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 수정할때 현재 시간으로 변경

    print("메모 수정 완료")


def deleteMemo():     # 말 그대로 삭제하는 함수

    id = session.loginId

    # 삭제 내용없으면 종료
    if id not in memoDb.memoDb or len(memoDb.memoDb[id]) == 0:
        print('삭제할 메모가 없습니다.')
        return

    readMemo()

    try:
        num = int(input('삭제할 메모 번호 입력하세요: ')) - 1   # 리스트번호로 인해서 -1

    except:
        print('숫자만 입력하세요.')
        return

    # 없는 번호 검사
    if num < 0 or num >= len(memoDb.memoDb[id]):
        print("잘못된 번호입니다.")
        return

    del memoDb.memoDb[id][num]

    print("메모 삭제 완료")


def searchMemo():      # 키워드를 찾기위한 함수

    id = session.loginId

    if id not in memoDb.memoDb or len(memoDb.memoDb[id]) == 0:
        print('찾고자 하는 메모내용이 없습니다.')
        return

    keyword = input('검색할 키워드 입력: ')   #찾고 싶은 단어입력

    count = 0

    for idx, memo in enumerate(memoDb.memoDb[id]):       #메모에서 등록된 인덱스 체크

        if keyword in memo[config.MEMO_TEXT]:      #메모내용에 찾고자하는 키워드 확인

            print(f'\n{idx + 1}번 메모')
            print(f'날짜: {memo[config.MEMO_DATE]}')
            print(f'내용: {memo[config.MEMO_TEXT]}')

            count += 1

    if count == 0:                  # 반복문으로 얻는 결과가 없으면 출력
        print('검색 결과가 없습니다.')