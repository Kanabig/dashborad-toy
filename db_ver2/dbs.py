from db_ver2 import configs

members = {
    "minsoo": {
        configs.ID: "minsoo",
        configs.PW: "pass123",
        configs.MAIL: "minsoo.kim@gmail.com",
        configs.PHONE: "010-1234-5678",
        configs.BANK_ACNT: "101-77-minsoo",
    },
}

bankAccounts = {
    "101-77-minsoo": {
        configs.BANK_ACNT: "101-77-minsoo",
        configs.BANK_PW: "1111",
        configs.BANK_LOG: [
            ("2026-05-25 09:00:00", 50000, "입금"),
            ("2026-05-26 14:20:15", 12000, "출금"),
        ],
    },
}

memos = {
    "minsoo": [
        {
            configs.MEMO_DATE: "2026-05-28 09:10:21",
            configs.MEMO_TEXT: "길동이에게 10,000원 보냄",
        },
    ]
}

todoLists = {
    "minsoo": [
        {
            configs.TODO_TEXT: "파이썬 알고리즘 2문제 풀기",
            configs.REGISTER_DAY: "2026-05-27 09:00:00",
            configs.EXPIRED_DAY: "2026-05-29 09:00:00",
            configs.REMAINING: "1",
            configs.SUCCESS: False,
        }
    ],
}
