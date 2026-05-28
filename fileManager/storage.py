import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import json

import db.backAccountDb as bDb
import db.memberAccountDb as mDb
import db.memoDb as mmDb
import db.todoListDb as tDb

PATH = "C:/pjh/python/dashborad-toy/fileManager/"

BANK_ACCOUNT_PATH = f"{PATH}/bank.json"
MEMBER_ACCOUNT_PATH = f"{PATH}/member.json"
MEMO_PATH = f"{PATH}/memo.json"
TODO_LIST_PATH = f"{PATH}/todo.json"


def saveBankAccount(db):
    saveAtFile(BANK_ACCOUNT_PATH, db)


def saveMemberAccount(db):
    saveAtFile(MEMBER_ACCOUNT_PATH, db)


def saveMemo(db):
    saveAtFile(MEMO_PATH, db)


def saveTodoList(db):
    saveAtFile(TODO_LIST_PATH, db)


def saveAtFile(path, data):
    with open(f"{path}", "a", encoding="utf-8") as file:
        json.dump(data, file)


def loadFromFile(path):
    data = None

    return data


def testMain():
    saveBankAccount(bDb.bankAccountDb)
    saveMemberAccount(mDb.memberAccountDb)
    saveMemo(mmDb.memoDb)
    saveTodoList(tDb.todoListDb)


if __name__ == "__main__":
    testMain()
