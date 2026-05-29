from db.memberAccountDb import memberAccountDb as members
from db.backAccountDb import bankAccountDb as bankAccounts
from db.memoDb import memoDb as memos
from db.todoListDb import todoListDb as todoLists
from db import config

import datetime


# ------ member ------
def createMember(id, pw, mail, phone, bankAcnt):
    members[id] = {
        config.ID: id,
        config.PW: pw,
        config.MAIL: mail,
        config.PHONE: phone,
        config.BANK_ACNT: bankAcnt,
    }

    memos[id] = []
    todoLists[id] = []


def getMemberIds():
    return members.keys()


def getMemberPw(id):
    return members[id][config.PW]


# ------ bank ------
def getMemberBankAcnt(id):
    return members[id][config.BANK_ACNT]


def createBankAccount(id, pw):
    bankAccounts[getMemberBankAcnt()] = {
        config.BANK_ACNT: f"101-77-{id}",
        config.BANK_PW: pw,
        config.BANK_LOG: [],
    }


# ------ memo ------
def getMemoList(id):
    return memos[id]


def hasMemo(id):
    return id in memos and len(memos[id]) > 0

def createMemo(id, text):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memo = {config.MEMO_DATE: time, config.MEMO_TEXT: text}

    memos[id].append(memo)

def updateMemo(id, num, newText):
    memos[id][num][config.MEMO_TEXT] = newText
    memos[id][num][config.MEMO_DATE] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def deleteMemo(id, num):
    del memos[id][num]

    
# ------ todolist ------
def createTodo(id, workNote, finishDay):
    now = datetime.datetime.now()
    expired_time = now + datetime.timedelta(days=finishDay)

    inforMationBox = {
        config.TODO_TEXT: workNote,
        config.REGISTER_DAY: now.strftime("%Y-%m-%d %H:%M:%S"),
        config.EXPIRED_DAY: expired_time.strftime("%Y-%m-%d %H:%M:%S"),
        config.REMAINING: str(finishDay),
        config.SUCCESS: False,
    }

    todoLists[id].append(inforMationBox)
