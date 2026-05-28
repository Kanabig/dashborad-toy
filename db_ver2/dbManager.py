from datetime import datetime
from db_ver2.dbs import members, bankAccounts, memos, todoLists
from db_ver2 import configs


# ------ member ------
def createMember(id, pw, mail, phone, bankAcnt):
    members[id] = {
        configs.ID: id,
        configs.PW: pw,
        configs.MAIL: mail,
        configs.PHONE: phone,
        configs.BANK_ACNT: bankAcnt,
    }

    memos[id] = []
    todoLists[id] = []


def getMemberIds():
    return members.keys()


def getMemberPw(id):
    return members[id][configs.PW]


# ------ bank ------
def getMemberBankAcnt(id):
    return members[id][configs.BANK_ACNT]


def createBankAccount(id, pw):
    bankAccounts[getMemberBankAcnt()] = {
        configs.BANK_ACNT: f"101-77-{id}",
        configs.BANK_PW: pw,
        configs.BANK_LOG: [],
    }


# ------ memo ------
def createMemo(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memo = {configs.MEMO_DATE: time, configs.MEMO_TEXT: text}

    memos[id].append(memo)


# ------ todolist ------
def createTodo(workNote, finishDay):
    now = datetime.datetime.now()
    expired_time = now + datetime.timedelta(days=finishDay)

    inforMationBox = {
        configs.TODO_TEXT: workNote,
        configs.REGISTER_DAY: now.strftime("%Y-%m-%d %H:%M:%S"),
        configs.EXPIRED_DAY: expired_time.strftime("%Y-%m-%d %H:%M:%S"),
        configs.REMAINING: str(finishDay),
        configs.SUCCESS: False,
    }

    todoLists["ID"].append(inforMationBox)
