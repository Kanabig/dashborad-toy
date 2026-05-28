import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import session
import datetime
import copy
import json
from db import config
from db import backAccountDb

ADD_MONEY = 1
SUB_MONEY = 2
MONEY_FLOW = 3
SELECT_END = 99

flag = True
accountBalance = 0


def startLoop():
    if session.onSignIned:
        if config.BANK_ACNT:
            setMoneyFlow()

        else:
            setBankAccount()
            return
        
    else:
        print('로그인을 진행한 다음, 진행하세요.')
        return


def setBankAccount():
    fixedNumber = '101-77'
    userAccount = 'id'
    bankAccount = f'{fixedNumber}-{userAccount}'
    config.BANK_ACNT = bankAccount
    try:
        inputAccountPw = int(input('계좌 비밀번호 입력: '))
        print('계좌 비밀번호가 설정되었습니다.')
        config.BANK_PW = inputAccountPw

    except ValueError:
        print('비밀번호를 다시 입력하세요.')

    backAccountDb.bankAccountDb[config.BANK_ACNT] = {
        config.BANK_ACNT: {
        config.BANK_ACNT: bankAccount,
        config.BANK_PW: inputAccountPw,
        config.BANK_LOG: []
        }
    }

    print(f'Bank_Account created: {config.BANK_ACNT}')
    return config.BANK_ACNT


def addMoney():
    global accountBalance

    try:
        plus = int(input('금액을 입력하세요, 입금 금액: '))
        if plus <= 0:
            print('0원 이하 금액은 입금할 수 없습니다.')
            return
        else:
            print('입금 중입니다.')
            accountBalance += plus
            now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG].append(
                (now, plus, '입금')
            )
            print(f'입금 완료, 현재 잔액: {accountBalance:,}원')

    except ValueError:
        print('[금액만] 다시 입력하세요.')
        return


def subMoney():
    global accountBalance
    try:
        minus = int(input('금액을 입력하세요, 출금 금액: '))
        if minus <= 0:
            print('0원 이하 금액은 출금할 수 없습니다.')
            return
        
        elif minus > accountBalance:
            print('출금 금액이 계좌 잔액보다 많습니다.')
            return
            
        elif minus <= accountBalance:
            print('출금 중입니다.')
            accountBalance -= minus
            now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG].append(
                (now, minus, '출금')
            )
            print(f'출금 완료, 현재 잔액: {accountBalance:,}원')

    except ValueError:
        print('[금액만] 다시 입력하세요.')
        return 


def moneyFlow():
    global accountBalance
    myMoneyFlow = backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG]
    deepcopieFlow = copy.deepcopy(myMoneyFlow)
    deepcopieFlow.reverse()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    print(f'\n조회 일시: {now}')
    if len(deepcopieFlow) == 0:
        print('거래내역이 없습니다.')
        return
    
    else:
        for idx, flow in enumerate(deepcopieFlow):
            date, money, kind = flow
            print(f'[{date} / {idx+1}] {kind} {money:,}원')


def saveJson():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    fileName = f'{now}_balance_data.json'
    history = backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG]
    save_data = {
        "account_number": config.BANK_ACNT,
        "current_balance": accountBalance,
        "transaction_history": history
        }

    with open(fileName, 'w', encoding='utf8') as f:
        jsonFile = json.dumps(save_data, indent=4, sort_keys=True, ensure_ascii=False)
        f.write(jsonFile)
    

def setMoneyFlow():
    global flag
    while flag:
        try:
            inputData = int(input('메뉴를 선택하세요, 1.입금    2.출금    3.내역    99.종료'))
            if inputData == ADD_MONEY:
                addMoney()
                saveJson()

            elif inputData == SUB_MONEY:
                subMoney()
                saveJson()

            elif inputData == MONEY_FLOW:
                moneyFlow()

            elif inputData == SELECT_END:
                print('종료합니다.')
                flag = False
            
            else:
                print('잘못된 메뉴선택입니다.')

        except ValueError:
            print('[올바른] 메뉴를 선택하세요.')
            return

