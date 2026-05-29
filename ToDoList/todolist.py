import os
import sys
import datetime

# 프로젝트 구조에 맞게 경로 설정
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ToDoList import todo_constant as tc
from db import dbManager
from db import config
from memberService import session

# ----------------------------------------------------
# [CREATE] 1. 새로운 할 일 등록 함수
# ----------------------------------------------------
def create_todo():
    workNote = input('체크리스트를 작성하세요: ')
    now = datetime.datetime.now()
    
    inputFinishDay = input('마감일까지 남은 일수를 입력하세요 (최대 30일): ')
    if inputFinishDay.isdigit():
        inputFinishDay = int(inputFinishDay)
    else:
        print('숫자만 입력 가능합니다. 처음으로 돌아갑니다.')
        return
        
    if not (0 <= inputFinishDay <= 30):
        print('0일 이상 30일 이하로 입력하세요. 처음으로 돌아갑니다.')
        return
        
    dbManager.createTodo(session.signinedId, workNote, inputFinishDay)

    # expired_time = now + datetime.timedelta(days=inputFinishDay)
    # id = session.signinedId

    # if id not in todoListDb:
    #     todoListDb[id] = []  # session.signinedId 키가 없으면 빈 리스트를 새로 만들어라!

    # inforMationBox = {
    #     config.TODO_TEXT: workNote,
    #     config.REGISTER_DAY: now.strftime('%Y-%m-%d %H:%M:%S'),
    #     config.EXPIRED_DAY: expired_time.strftime('%Y-%m-%d %H:%M:%S'),
    #     config.REMAINING: str(inputFinishDay),
    #     config.SUCCESS: False
    # }


    # todoListDb[id].append(inforMationBox)

    # print("\n새로운 체크리스트가 성공적으로 등록되었습니다!")
    # # print(f" 할 일: {inforMationBox[config.TODO_TEXT]}")
    # # print(f" 등록일: {inforMationBox[config.REGISTER_DAY]}")
    # # print(f" 마감일: {inforMationBox[config.EXPIRED_DAY]}")
    # print('-' * 50)


# ----------------------------------------------------
# [READ] 2. 목록 출력 함수 (만료 여부 실시간 계산)
# ----------------------------------------------------
def read_todo_list():
    print('\n' + '-' * 20)
    print('----[나의 체크리스트 목록 조회]----')
    print('-' * 20)

    if session.signinedId not in dbManager.todoLists:
        print('등록된 체크리스트가 없습니다! 먼저 등록하세요!')
        return False
    
    now = datetime.datetime.now()
    for idx, todo in enumerate(dbManager.todoLists[session.signinedId], start=1):
        # 완료 여부 표시
        status = '완료!' if todo[config.SUCCESS] else '미완료'
        
        # 만료 여부 계산 (문자열을 datetime 객체로 변환하여 비교)
        expired_date = datetime.datetime.strptime(todo[config.EXPIRED_DAY], '%Y-%m-%d %H:%M:%S')
        if now > expired_date:
            time_status = '[기간만료]'
        else:
            time_status = '[진행중]'
        
        print(f'{idx}. {time_status} 할일: {todo[config.TODO_TEXT]} | 상태: {status} | 마감일: {todo[config.EXPIRED_DAY]}')
    print('-' * 50)
    return True  # 목록이 정상적으로 존재함


# ----------------------------------------------------
# [UPDATE] 3. 완료 처리 함수
# ----------------------------------------------------
def update_todo_status():
    checkChangeNum = (input('완료처리할 체크리스트의 번호를 입력하세요: '))
    if checkChangeNum.isdigit():
        checkChangeNum = int(checkChangeNum)
    else:
        print('숫자만 입력 가능합니다. 처음으로 돌아갑니다.')
        return
        
    if 1 <= checkChangeNum <= len(dbManager.todoLists[session.signinedId]):
        targetIdx = checkChangeNum - 1
        dbManager.todoLists[session.signinedId][targetIdx][config.SUCCESS] = True
        print(f'{checkChangeNum}번 체크리스트가 "완료!" 상태로 변경되었습니다.')
    else:
        print('존재하지 않는 번호입니다.')


# ----------------------------------------------------
# [CHANGE] 4. 할 일 내용 수정 함수
# ----------------------------------------------------
def change_todo_text():
    checkChangeNum = (input('수정할 체크리스트의 번호를 입력하세요: '))
    if checkChangeNum.isdigit():
        checkChangeNum = int(checkChangeNum)
    else:
        print('숫자만 입력 가능합니다. 처음으로 돌아갑니다.')
        return


    if 1 <= checkChangeNum <= len(dbManager.todoLists[session.signinedId]):
        targetIdx = checkChangeNum - 1
        changeChecklist = input('수정할 체크리스트의 새 내용을 입력하세요: ')
        dbManager.todoLists[session.signinedId][targetIdx][config.TODO_TEXT] = changeChecklist
        print(f'{checkChangeNum}번 체크리스트 내용이 "{changeChecklist}"(으)로 수정되었습니다!')
    else:
        print('존재하지 않는 번호입니다.')


# ----------------------------------------------------
# [DELETE] 5. 할 일 삭제 함수
# ----------------------------------------------------
def delete_todo():
    checkChangeNum = (input('삭제할 할 일의 번호를 입력하세요: '))
    if checkChangeNum.isdigit():
        checkChangeNum = int(checkChangeNum)
    else:
        print('숫자만 입력 가능합니다. 처음으로 돌아갑니다.')
        return

    if 1 <= checkChangeNum <= len(dbManager.todoLists[session.signinedId]):
        targetIdx = checkChangeNum - 1
        del dbManager.todoLists[session.signinedId][targetIdx]
        print('삭제 완료!')
    else:
        print('존재하지 않는 번호입니다.')


# ----------------------------------------------------
# [MAIN] 프로그램 메인 루프 제어 함수
# ----------------------------------------------------

def handleRead():
    if read_todo_list():

        changeInfo = input('1.완료처리   2.내용수정   3.삭제   99.이전 메뉴로 이동\n관리 선택: ')

        if changeInfo == tc.UPDATE:
            update_todo_status()
        elif changeInfo == tc.CHANGE:
            change_todo_text()
        elif changeInfo == tc.DELETE:
            delete_todo()
        elif changeInfo == tc.EXIT:
            print('이전 메뉴로 돌아갑니다.')
        else:
            print('올바른 관리 번호를 선택해주세요.')

def startLoop():
    print('Todo List 프로그램에 오신 것을 환영합니다 ')
    
    while True:
        print('\n' + '=' * 50)
        chooseList = input('1.할 일 체크리스트 등록    2.목록 조회/관리       99.프로그램 종료\n메뉴 선택: ')

        # 1. 할 일 등록
        if chooseList == tc.CREATE:
            create_todo()
        
        # 2. 목록 조회 및 서브 메뉴(수정/삭제/완료) 관리
        elif chooseList == tc.READ:
            # 목록이 있을 때만 서브 메뉴를 보여줍니다.
            handleRead()
        
        # 99. 프로그램 종료
        elif chooseList == tc.EXIT:
            print('프로그램이 종료됩니다. 이용해주셔서 감사합니다.')
            break
        
        else:
            print('올바른 메뉴 번호를 선택해주세요.')

if __name__ == '__main__':
    # session.signinedId = "minsoo"
    startLoop()