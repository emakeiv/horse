from enum import Enum

class Status(str, Enum):
    PENDING = "pending"
    PASS    = "pass"
    FAIL    = "fail"
    OK      = "ok"