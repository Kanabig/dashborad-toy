'''
-todo list 규찬
	-CRUD: wirte, read, update, delete
	-expired date
	-read할때, 해당되는 todo의 완료/미완료 여부 표시


	def(오늘)
    만료 - 오늘 = 
	datetime.datetime.day() 31 .strf(time, "%d") 
								int(28)
	 				  			strp("")

	- read하면 todoList가 쭉 만료일(만료된거, 안된거 출력하기 힘들면) 너가 이미 해결을 한거.
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import todo_constant as tc
from db.todoListDb import todoListDb
import datetime
import config


flag = True


def choiceToDoList():
   
    global flag
    print('todo list에 오신 것을 환영합니다')
    while flag:
        chooseList = int(input('1.할 일 체크리스트     2.목록 조회         99.프로그램 종료'))

        if chooseList == tc.CREATE:
            workNote = input('체크리스트를 작성하세요: ')
         
            now = datetime.datetime.now()
            inputFinishDay = int(input('마감일을 입력하세요(최대 30): 숫자만 '))
            if inputFinishDay > 30:
                print('30일 안으로 입력하세요: 숫자만 ')
                continue
            expired_time = now + datetime.timedelta(days=inputFinishDay)

            inforMationBox = {
                config.TODO_TEXT: workNote,
                config.REGISTER_DAY: now.strftime('%Y-%m-%d %H:%M:%S'),
                config.EXPIRED_DAY: expired_time.strftime('%Y-%m-%d %H:%M:%S'),
                config.REMAINING: str(inputFinishDay),
                config.SUCCESS: False
            }

            todoListDb["ID"].append(inforMationBox)

            print("\n 새로운 체크리스트가 성공적으로 등록되었습니다!")
            print(f" 할 일: {inforMationBox[config.TODO_TEXT]}")
            print(f" 등록일: {inforMationBox[config.REGISTER_DAY]}")
            print(f" 마감일: {inforMationBox[config.EXPIRED_DAY]}")
            print('--------------------------------------------------')

        elif chooseList == tc.READ:
            print()
            print()
            print()
            print()
            print('------------------------------------')
            print('------------------------------------')
            print('----[나의 체크리스트 목록 조회]----')


            if not todoListDb['ID']:
                print()
                print()
                print('등록된 체크리스트가 없습니다! 먼저 등록하세요!')
                print()
                print()
            else:
                for idx, todo in enumerate(todoListDb['ID'], start=1):
                    status = '완료!' if todo['SUCCESS'] else '미완료'
                    print(f'{idx}.체크리스트: {todo[config.TODO_TEXT]} ㅣ 상태 {status} ㅣ 마감일: {todo[config.EXPIRED_DAY]}')
                    print()
                    print()
                    print('--------------------------------------------------')    

                    
                changeInfo = int(input('1.체크리스트 완료       2.체크리스트 삭제           99.종료'))
            
                if changeInfo == tc.UPDATE:

                    while True:
                        checkChangeNum = int(input('완료처리할 체크리스트의 번호를 입력하세요: '))
                            
                        if 1 <= checkChangeNum <= len(todoListDb['ID']):

                            targetIdx = checkChangeNum - 1

                            todoListDb['ID'][targetIdx]['SUCCESS'] = True

                            print(f' {checkChangeNum}번 체크리스트가 "완료!" 상태로 변경되었습니다')
                            break
                        
                        else:
                            print('없는 번호입니다 다시 입력해 주세요')
                            continue
                
                if changeInfo == tc.DELETE:
                        checkChangeNum = int(input('삭제할 할 일의 번호를 입력하세요: '))

                        if 1 <= checkChangeNum <= len(todoListDb['ID']):

                            targetIdx = checkChangeNum - 1

                            del todoListDb['ID'][targetIdx]
                            print('삭제 완료!')

                        else:
                            print('없는 번호입니다 다시 입력해 주세요')
                            continue

                
            
    
    #         

        elif chooseList == tc.EXIT:
            print('프로그램이 종료됩니다')
            break





def mainClone():
    choiceToDoList()


if __name__ == '__main__':
    mainClone()