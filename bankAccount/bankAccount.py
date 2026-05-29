import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from memberService import session
from memberService import memberService
import datetime
import copy
import json
from memberService import session
from db import config
from db import dbManager

ADD_SUB_MONEY = 1
MONEY_FLOW = 2
SELECT_END = 99

flag = True
accountBalance = 0


def fastBalance():
    global accountBalance
    accountBalance = 0
    accountNumber = dbManager.members[session.signinedId]["BANK_ACNT"]
    balanceLogs = dbManager.bankAccounts[accountNumber].get(config.BANK_LOG, [])
    for log in balanceLogs:
        _, amount, kind = log
        if kind == '입금':
            accountBalance += amount
        else:
            accountBalance -= amount


def setBankAccount(id):
    inputAccountPw = input('계좌 비밀번호 입력: ')

    if inputAccountPw.isdigit():
        print('계좌 비밀번호가 설정되었습니다.')
    else:
        print('비밀번호를 다시 입력하세요.')

    dbManager.createBankAccount(id, inputAccountPw)
    accountNumber = dbManager.members[id]["BANK_ACNT"]
    print(f'Bank_Account created: {accountNumber}')


def calculateMoney(kind):
    global accountBalance
    inputMoney = input(f'입금 및 출금할 금액을 입력하세요: ')

    if not inputMoney.isdigit():
        print('금액을 다시 입력하세요.')
        return None

    intMoney = int(inputMoney)
    if intMoney <= 0:
        print('0원 미만은 입금 및 출금할 수 없습니다.')
        return None
        
    if kind == '입금':
        accountBalance += intMoney
    elif kind == '출금':
        if accountBalance < intMoney:
            print('잔액이 부족합니다.')
            return None
        accountBalance -= intMoney

    print(f'입금 및 출금 완료, 현재 잔액: {accountBalance}')
    return intMoney


def moneyFlow():
    global accountBalance
    accountNumber = dbManager.members[session.signinedId]["BANK_ACNT"]

    userDonggeun = dbManager.bankAccounts.get(accountNumber)
    myMoneyFlow = userDonggeun.get(config.BANK_LOG)

    if not myMoneyFlow:
        print('거래내역이 없습니다.')
        return
    
    deepcopieFlow = copy.deepcopy(myMoneyFlow)
    deepcopieFlow.reverse()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    print(f'\n조회 일시: {now}')

    for idx, flow in enumerate(deepcopieFlow):
        date, money, kind = flow
        print(f'[{date} / {idx+1}] {kind} {money}원 / 잔액 {accountBalance}원')
    

def setMoneyFlow():
    global flag
    while flag:
        inputData = input('메뉴를 선택하세요, 1.입금 및 출금    2.내역    99.종료')
        if inputData.isdigit():
            selected1 = int(inputData)
            if selected1 == ADD_SUB_MONEY:
                selected2 = input('1.입금    2.출금')
                kind = '입금' if selected2 == '1' else '출금'
                amount = calculateMoney(kind)
                if amount:
                    dbManager.createdFlowHistory(session.signinedId, amount, kind)
                    print(f'[{kind}] 처리가 완료되었습니다.')

            elif selected1 == MONEY_FLOW:
                moneyFlow()

            elif selected1 == SELECT_END:
                print('종료합니다.')
                flag = False
                
            else:
                print('잘못된 메뉴선택입니다.')

        else:
            print('[올바른] 메뉴를 선택하세요.')
            return
        

def startLoop():
    if session.onSignIned():
        if config.BANK_ACNT:
            fastBalance()
            setMoneyFlow()

        else:
            setBankAccount()
            return
        
    else:
        print('로그인을 진행한 다음, 진행하세요.')
        return
    

