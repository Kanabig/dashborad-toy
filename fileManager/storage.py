import json

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
    with open(f"{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def loadFromFile(path):
    data = None
    return data


if __name__ == "__main__":

    def testMain():
        import os
        import sys

        sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

        import db.backAccountDb as bDb
        import db.memberAccountDb as mDb
        import db.memoDb as mmDb
        import db.todoListDb as tDb

        saveBankAccount(bDb.bankAccountDb)
        saveMemberAccount(mDb.memberAccountDb)
        saveMemo(mmDb.memoDb)
        saveTodoList(tDb.todoListDb)

    testMain()
