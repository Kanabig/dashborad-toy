from db.memberAccountDb import memberAccountDb as members
from db.backAccountDb import bankAccountDb as bankAccounts
from db.memoDb import memoDb as memos
from db.todoListDb import todoListDb as todoLists
from db import config

from datetime import datetime


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
def createMemo(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memo = {config.MEMO_DATE: time, config.MEMO_TEXT: text}

    memos[id].append(memo)


# ------ todolist ------
def createTodo(workNote, finishDay):
    now = datetime.datetime.now()
    expired_time = now + datetime.timedelta(days=finishDay)

    inforMationBox = {
        config.TODO_TEXT: workNote,
        config.REGISTER_DAY: now.strftime("%Y-%m-%d %H:%M:%S"),
        config.EXPIRED_DAY: expired_time.strftime("%Y-%m-%d %H:%M:%S"),
        config.REMAINING: str(finishDay),
        config.SUCCESS: False,
    }

    todoLists["ID"].append(inforMationBox)
