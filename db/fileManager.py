import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from db import memberAccountDb as memberDb
from db import backAccountDb as bankDb
from db import memoDb as memoDb
from db import todoListDb as todoDb
from db import config

STORAGE_PATH = "C:/pjh/python/dashborad-toy/db/storage"

PATH_MEMBER = f"{STORAGE_PATH}/member.json"
PATH_BANK = f"{STORAGE_PATH}/bank.json"
PATH_MEMO = f"{STORAGE_PATH}/memo.json"
PATH_TODO = f"{STORAGE_PATH}/todo.json"


def saveAtFile(path, data):
    # 암호화?
    with open(f"{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# TODO: 데이터가 많아질 때를 대비해 캐싱해야함
# FIXME: storage에 없는 정보만 저장 (새로 생긴 데이터, 수정된 데이터, 원래 있었다가 삭제된거?)
def saveMemberAccount():
    saveAtFile(PATH_MEMBER, memberDb.memberAccountDb)


def saveBankAccount():
    saveAtFile(PATH_BANK, bankDb.bankAccountDb)


def saveMemo():
    saveAtFile(PATH_MEMO, memoDb.memoDb)


def saveTodoList():
    saveAtFile(PATH_TODO, todoDb.todoListDb)


def loadFromFile(path, hook=None):
    with open(f"{path}", encoding="utf-8") as file:
        data = json.load(file, object_hook=hook)
        return data


def restoreBankLog(dct):
    # json에 데이터를 저장할 때 튜플->리스트가 되므로 로드할 때 리스트를 튜플로 바꿔줌
    if config.BANK_LOG in dct:
        for idx, item in enumerate(dct[config.BANK_LOG]):
            dct[config.BANK_LOG][idx] = tuple(item)

    return dct


def startCaching():
    memberDb.memberAccountDb = loadFromFile(PATH_MEMBER)
    bankDb.bankAccountDb = loadFromFile(PATH_BANK, restoreBankLog)
    memoDb.memoDb = loadFromFile(PATH_MEMO)
    todoDb.todoListDb = loadFromFile(PATH_TODO)


# if __name__ == "__main__":

#     def printInfo(dct):
#         print(dct)

#     def printAll():
#         printInfo(memberDb.memberAccountDb)
#         printInfo(bankDb.bankAccountDb)
#         printInfo(memoDb.memoDb)
#         printInfo(todoDb.todoListDb)

#     saveBankAccount()
#     saveMemberAccount()
#     saveMemo()
#     saveTodoList()

#     print("=" * 100)

#     memberDb.memberAccountDb = None
#     bankDb.bankAccountDb = None
#     memoDb.memoDb = None
#     todoDb.todoListDb = None

#     startCaching()
